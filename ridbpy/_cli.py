"""
ridbPy: Command Line Interface
"""

import click

from ridbpy import __application__, __version__


@click.group()
@click.version_option(version=__version__, prog_name=__application__)
@click.pass_context
def command_line_interface(ctx: click.core.Context) -> None:
    """
    Welcome to ridbPy

    https://github.com/juftin/ridbpy
    """
    ctx.ensure_object(dict)


if __name__ == "__main__":
    command_line_interface()
