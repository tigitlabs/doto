from invoke import Collection, task
import tasks.docker as docker


namespace = Collection()
namespace.add_collection(docker.docker_ns)