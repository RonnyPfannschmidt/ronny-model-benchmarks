
import click

import ollama

from rich.table import Table, Column
import rich.table



@click.command()
def main():
    table = rich.table.Table("Model", Column("Size", justify="left"), Column("Parameter Size", justify="left"))

    models = ollama.list().models

    for model in models:
        assert model.size is not None
        assert model.details is not None
        assert model.details.parameter_size is not None
        table.add_row(model.model, model.size.human_readable(), model.details.parameter_size)

    rich.print(table    )