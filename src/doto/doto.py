from pydantic import BaseModel


class Tag(BaseModel):
    """
    Represents a tag
    """

    name: str


class Package(BaseModel):
    """
    Represents a package
    """

    name: str
    version: str


class PackageList(BaseModel):
    """
    Represents a list of packages
    """

    source: str
    packages: list[Package]


class Host(BaseModel):
    """
    Represents a host
    """

    name: str
    tags: list[Tag] = []
    packages: PackageList


class Manifest(BaseModel):
    """
    Represents a manifest
    """

    hosts: list[Host]


class Doto:
    """
    Represents the Doto application
    """

    def __init__(self):
        self.manifest : Manifest | None = None

    def add_host(self, name: str):
        """
        Add a host to the manifest
        """
        if self.manifest is None:
            host = Host(name=name, packages=PackageList(source="apt", packages=[]))
            self.manifest = Manifest(hosts=[host])
