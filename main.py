from core.kernel import Kernel
from plugins.plugin import Plugin


def main():
    kernel = Kernel()
    kernel.print_hello()

    plugin = Plugin()
    plugin.print_hello()

if __name__ == "__main__":
    main()
