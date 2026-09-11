from zzl import __version__


def test_package_importable() -> None:
    import zzl

    assert zzl.__version__ == __version__


def test_version() -> None:
    assert __version__
    assert isinstance(__version__, str)
