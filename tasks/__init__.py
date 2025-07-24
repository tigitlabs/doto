from invoke import Collection
import tasks.python as python
import tasks.docker as docker


namespace = Collection()
namespace.add_collection(python.python_ns)
namespace.add_collection(docker.docker_ns)
