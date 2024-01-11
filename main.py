from FastGUI.window_opener import WindowOpener
from FastGUI.stack import Vstack, Hstack
import customtkinter


if __name__ == "__main__":
    with WindowOpener() as window:
        with Vstack(window) as vstack:
            vstack.add_stack(customtkinter.CTkLabel(window, text="Hello, world!"))
            vstack.add_stack(customtkinter.CTkButton(window, text="Hello, world!"))

        with Hstack(window) as hstack:
            hstack.add_stack(customtkinter.CTkLabel(window, text="Hello, world!"))
            hstack.add_stack(customtkinter.CTkButton(window, text="Hello, world!"))
