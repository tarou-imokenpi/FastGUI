import customtkinter


class WindowOpener(customtkinter.CTk):
    """新しいウィンドウを作成するクラス

    Parameters
    ----------
    title : srt
        ウィンドウのタイトル
    window_size : tuple, default (400, 150)
        ウィンドウのサイズ
    """

    def __init__(self, title: str = "new window", window_size: tuple = (400, 150)):
        super().__init__()
        self.geometry(f"{window_size[0]}x{window_size[1]}")
        self.title(title)

    # withで使うためのメソッド
    def __enter__(self):
        print("Entering...")
        return self

    def __exit__(self, *args):
        print("Exiting...")
        self.mainloop()
