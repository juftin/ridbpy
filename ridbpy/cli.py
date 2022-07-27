"""
ridbPy: Command Line Interface
"""

import json
import shutil
import zipfile

import click
import numpy as np
import pandas as pd
import requests
from pydantic.json import pydantic_encoder
from rich import print
from sqlmodel import SQLModel

from ridbpy import __application__, __version__
from ridbpy.application import FileConfig, SQLConfig, engine, raw_engine, session
from ridbpy.models import ALL_TABLES, RecAreas


@click.group()
@click.version_option(version=__version__, prog_name=__application__)
@click.pass_context
def command_line_interface(ctx: click.core.Context) -> None:
    """
    Welcome to ridbPy

    visit the ridbPy documentation at https://github.com/juftin/ridbpy
    """
    ctx.ensure_object(dict)


@command_line_interface.group()
def database() -> None:
    """
    Perform Actions on the Database
    """


@database.command("build")
def database_build() -> None:
    """
    Build the Database
    """
    SQLModel.metadata.create_all(engine)


@database.command("destroy")
def database_destroy() -> None:
    """
    Destroy the Database

    And also rebuild it
    """
    SQLModel.metadata.drop_all(engine)
    SQLConfig.sqlite_file.unlink()


@database.group()
def raw() -> None:
    """
    Interact with the Latest Raw RIDB Data
    """
    pass


@database.group()
def query() -> None:
    """
    Query the pyridb Database
    """
    pass


@raw.command()
def fetch() -> None:
    """
    Fetch the Raw RIDB Data into a Local SQLite Database
    """
    FileConfig.local_zip_file.parent.mkdir(exist_ok=True)
    FileConfig.local_zip_file.touch(exist_ok=True)
    zip_url = "https://ridb.recreation.gov/downloads/RIDBFullExport_V1_CSV.zip"
    with requests.get(zip_url, stream=True) as r:
        with open(FileConfig.local_zip_file, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    zipped_data = zipfile.ZipFile(file=FileConfig.local_zip_file, mode="r")
    table_names = [table.__tablename__ for table in ALL_TABLES]
    for member in zipped_data.filelist:
        member_name = member.filename.split("_")[0]
        if member_name in table_names:
            _data = zipped_data.open(member.filename)
            df = pd.read_csv(_data)
            df.to_sql(
                name=member_name, con=raw_engine, if_exists="replace", index=False
            )
            print(member_name, len(df))


@raw.command()
def ingest() -> None:
    """
    Ingest the Raw RIDB Data into the ridbPy Backing Database
    """
    engine.echo = False
    SQLModel.metadata.drop_all(engine)
    SQLConfig.sqlite_file.unlink()
    SQLModel.metadata.create_all(engine)
    for sqlmodel_class in ALL_TABLES:
        tablename: str = sqlmodel_class.__tablename__  # type: ignore
        records = (
            pd.read_sql(tablename, con=raw_engine)
            .fillna(np.nan)
            .replace([np.nan], [None])
        )
        print(tablename, len(records))
        records.to_sql(
            tablename,
            con=engine,
            if_exists="append",
            index=False,
        )


@click.option("--limit", "-l", default=5, type=int)
@query.command()
def rec_areas(limit: int) -> None:
    """
    List Recreation Areas
    """
    query = session.query(RecAreas).limit(limit).all()
    formatted_dict = json.dumps(
        [item for item in query], default=pydantic_encoder, indent=4
    )
    click.echo(formatted_dict)


if __name__ == "__main__":
    command_line_interface()
