from invoke import Collection, task


@task
def lint(c):
    """
    Run linting checks
    """
    c.run("poetry run ruff check --config .ruff.toml")


@task
def type_check(c):
    """
    Run type checking
    """
    c.run("poetry run mypy src --config-file .mypy.ini")


@task
def test(c):
    """
    Run tests
    """
    c.run("poetry run pytest")


@task
def ci(c):
    """
    Run all CI tasks
    """
    lint(c)
    type_check(c)
    test(c)


python_ns = Collection("python")
python_ns.add_task(lint, name="lint")
python_ns.add_task(type_check, name="type_check")
python_ns.add_task(test, name="test")
python_ns.add_task(ci, name="ci")
