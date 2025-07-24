from invoke import Collection, task


@task
def lint(c):
    """
    Run linting checks
    """
    c.run("poetry run ruff check")


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
    test(c)


python_ns = Collection("python")
python_ns.add_task(lint, name="lint")
python_ns.add_task(test, name="test")
python_ns.add_task(ci, name="ci")
