"""
Core RIDB-PY Application Variables
"""

from os import getenv
from pathlib import Path

import sqlalchemy
from sqlmodel import Session, create_engine

from ridbpy.config import FileConfig
from ridbpy.models import ALL_TABLES  # noqa


def make_conn_str(file_path: Path) -> str:
    """
    Create a SQLite Conn String

    Parameters
    ----------
    file_path: Path
        Fiole path of the SQLite file

    Returns
    -------
    str
        SQLAlchemy connection string
    """
    return str(
        sqlalchemy.engine.url.URL.create(drivername="sqlite", host="/" + str(file_path))
    )


class SQLConfig:
    """
    SQL Connection Configuration
    """

    sqlite_file = FileConfig.DATA_DIR.joinpath("ridb.db")
    sqlite_conn_str = make_conn_str(file_path=sqlite_file)

    _environment_variable = getenv("RIDB_SQL_CONN_STR", None)
    if _environment_variable is None:
        connection_string = sqlite_conn_str
    else:
        connection_string = _environment_variable


_conn_str: str = str(SQLConfig.connection_string)
sqlalchemy_engine = sqlalchemy.create_engine(_conn_str, echo=False)
engine = create_engine(_conn_str, echo=False)
_raw_conn_str = make_conn_str(file_path=SQLConfig.sqlite_file.with_name("ridb_raw.db"))
raw_engine = sqlalchemy.create_engine(_raw_conn_str)

session = Session(engine)
