import customtkinter


class Stack:
    """方向を指定してウィジェットを配置する"""

    def __init__(self, window: customtkinter.CTk, direction: str = "v"):
        self.window = window
        self.instances = []
        self.direction = ["top" if direction == "v" else "left"]

    def add_stack(self, instance: object) -> object:
        self.instances.append(instance)
        return instance

    def __enter__(self):
        return self

    def __exit__(self, *args):
        [i.pack(side=self.direction) for i in self.instances]


class Vstack:
    """垂直方向にウィジェットを配置する"""

    def __init__(self, window: customtkinter.CTk):
        self.window = window
        self.instances = []

    def add_stack(self, instance: object) -> object:
        self.instances.append(instance)
        return instance

    def __enter__(self):
        return self

    def __exit__(self, *args):
        [i.pack(side="top") for i in self.instances]


class Hstack:
    """垂直方向にウィジェットを配置する"""

    def __init__(self, window: customtkinter.CTk):
        self.window = window
        self.instances = []

    def add_stack(self, instance: object) -> object:
        self.instances.append(instance)
        return instance

    def __enter__(self):
        return self

    def __exit__(self, *args):
        [i.pack(side="left") for i in self.instances]
