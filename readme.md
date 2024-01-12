# 直感的にGUIを作成することができます

### 従来のcustomtkinterでの書き方
```python
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()
```
### FastGUIなら
一個一個packする手間を省いて、`yield`がついた オブジェクトを一括でpackします。
```python
from FastGUI.window_opener import WindowOpener
from FastGUI.pack import pack
from customtkinter import CTkButton


with WindowOpener(title="FastGUI", window_size=(400, 150)) as window:

    @pack(side="top")
    def button():
        def button_callback():
            print("button pushed")

        yield CTkButton(window, text="my button", command=button_callback)

```