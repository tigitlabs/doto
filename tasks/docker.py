from invoke import Collection, task

CONTAINER_NAME = "doto-container"


@task
def test_package_version(c, package, command, version):
    """
    Test the package version inside the Docker container
    """
    result = c.run(f"docker run --rm --user vscode {CONTAINER_NAME} bash -c '{package} {command}'")
    if version not in result.stdout:
        raise ValueError(f"Expected {package} version {version}, but got {result.stdout.strip()}")
    else:
        print(f"✅ {package} version {version} is correctly installed.")


@task
def build_docker_image(c):
    """
    Build the Docker image
    """
    c.run(f"docker build -t {CONTAINER_NAME} .")


@task
def test_docker_image(c):
    """
    Build and Run the tests inside the Docker container
    """
    build_docker_image(c)
    test_package_version(c, "poetry", "--version", "2.1.3")


docker_ns = Collection("docker")
docker_ns.add_task(build_docker_image, name="build")
docker_ns.add_task(test_docker_image, name="test")
