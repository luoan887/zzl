"""Command-line entry point."""

from zzl import __version__


def main() -> None:
    print(f"hello from zzl {__version__}")


if __name__ == "__main__":
    main()
