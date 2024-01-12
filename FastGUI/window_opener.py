import customtkinter
from typing import Union, Tuple, Optional


class WindowOpener(customtkinter.CTk):
    """新しいウィンドウを作成するクラス

    Parameters
    ----------
    title : srt
        ウィンドウのタイトル
    window_size : tuple, default (400, 150)
        ウィンドウのサイズ
    fg_color : str or tuple, default None
        ウィンドウの背景色
    **kwargs
        customtkinter.CTkの引数
    """

    def __init__(
        self,
        title: str = "new window",
        window_size: tuple = (400, 150),
        fg_color: Optional[Union[str, Tuple[str, str]]] = None,
        **kwargs,
    ):
        super().__init__(fg_color, **kwargs)
        self.geometry(f"{window_size[0]}x{window_size[1]}")
        self.title(title)

    def __enter__(self) -> customtkinter.CTk:
        return self

    # withが終わったらmainloopを実行する
    def __exit__(self, *args):
        self.mainloop()
