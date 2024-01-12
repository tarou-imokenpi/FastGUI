from FastGUI.window_opener import WindowOpener
from FastGUI.pack import pack
from customtkinter import CTkButton


with WindowOpener(title="FastGUI", window_size=(400, 150)) as window:

    @pack(side="top")
    def button():
        def button_callback():
            print("button pushed")

        yield CTkButton(window, text="my button", command=button_callback)
