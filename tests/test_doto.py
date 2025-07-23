from doto.doto import Doto


def test_doto_init():
    """
    Test the initialization of the Doto class
    """
    doto = Doto()
    assert doto is not None

def test_add_host():
    """
    Test adding a host to the Doto instance
    """
    doto = Doto()
    doto.add_host("test-host")
    manifest = doto.manifest
    assert len(manifest.hosts) == 1
    assert manifest.hosts[0].name == "test-host"
    assert manifest.hosts[0].tags == []
    assert manifest.hosts[0].packages.source == "apt"
    print(manifest)
