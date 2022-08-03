"""
File Configuration Helpers for ridbPy
"""

import pathlib


class FileConfig:
    """
    Easy file configuration helper class
    """

    _this_file = pathlib.Path(__file__)
    _config_dir = _this_file.parent

    SOURCE_CODE_DIR = _config_dir.parent
    PROJECT_DIR = SOURCE_CODE_DIR.parent

    RIDBPY_DIR = SOURCE_CODE_DIR
    DATA_DIR = RIDBPY_DIR.joinpath("data")

    local_zip_file = DATA_DIR.joinpath("data.zip")
