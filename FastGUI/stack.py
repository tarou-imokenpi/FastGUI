class Vstack:
    """垂直方向にウィジェットを配置する"""

    def __init__(self, window):
        self.window = window
        self.instances = []

    def add_stack(self, instance: object) -> object:
        self.instances.append(instance)
        return instance

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print("Exiting... (Vstack)")
        [i.pack(side="top") for i in self.instances]


class Hstack:
    """垂直方向にウィジェットを配置する"""

    def __init__(self, window):
        self.window = window
        self.instances = []

    def add_stack(self, instance: object) -> object:
        self.instances.append(instance)
        return instance

    def __enter__(self):
        return self

    def __exit__(self, *args):
        [i.pack(side="left") for i in self.instances]
