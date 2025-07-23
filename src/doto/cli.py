import typer

app = typer.Typer(
    name="doto", help="doto - A package management tool", no_args_is_help=True
)


@app.command()
def version():
    """
    Show the version of doto
    """
    typer.echo("doto version 1.0.0")


if __name__ == "__main__":
    app()
