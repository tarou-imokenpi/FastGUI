from FastGUI.window_opener import WindowOpener
from FastGUI.stack import Stack
from customtkinter import CTkButton, CTkLabel


with WindowOpener(window_size=(800, 600)) as window:
    with Stack(window, direction="v") as stack:
        stack.add_stack(CTkLabel(window, text="Hello, world!"))
        stack.add_stack(CTkButton(window, text="Hello, world!"))
        stack.add_stack(CTkButton(window, text="Hello, world!"))
        stack.add_stack(CTkButton(window, text="Hello, world!"))
        stack.add_stack(CTkButton(window, text="Hello, world!"))
        stack.add_stack(CTkButton(window, text="Hello, world!"))
        stack.add_stack(CTkButton(window, text="Hello, world!"))
        stack.add_stack(CTkButton(window, text="Hello, world!"))
        stack.add_stack(CTkButton(window, text="Hello, world!"))
