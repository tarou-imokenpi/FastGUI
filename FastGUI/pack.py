from functools import wraps


def pack(**kwargs):
    """ウィジェットを配置するデコレーター

    parameters
    ----------
    **kwargs
        customtkinter.CTk.packの引数

    example
    --------
    ```python
    with WindowOpener(window_size=(800, 600)) as window:
        @pack(side="top")
        def ok_no_button():
            yield CTkButton(window, text="OK")
            yield CTkButton(window, text="NO")
    """

    def _stack_decorator(func):
        @wraps(func)
        def _wrapper():
            for i in func():
                i.pack(**kwargs)

        return _wrapper()

    return _stack_decorator
