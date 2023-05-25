class Microkernel:
    def __init__(self):
        self.plugins = []

    def load_plugin(self, plugin):
        self.plugins.append(plugin)

    def run(self):
        print("Microkernel is running.")

        for plugin in self.plugins:
            plugin.execute()


class Plugin:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing plugin: {self.name}")


if __name__ == "__main__":
    kernel = Microkernel()

    # Load plugins
    plugin = Plugin("Plugin")
)

    kernel.load_plugin(plugin)

  
    # Run the microkernel
    kernel.run()
