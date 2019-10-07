import click
from .command import project_group

cli=click.CommandCollection(sources=[project_group])
cli()