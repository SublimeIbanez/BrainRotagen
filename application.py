import tkinter
import tkinter.filedialog
import tk_async_execute
import pdf_reader 
import tts

# https://tkinter-async-execute.readthedocs.io/_/downloads/en/v1.0.x/pdf/
# class tk_async_execute.widget.ExecutingAsyncWindow
#       (coro: Coroutine, visible: bool = True, pop_up: bool = False, callback: Callable | None = None, *args, **kwargs)

class Application:
    def __init__(self):
        root = tkinter.Tk()
        self.root = root
        self.build_window()
        self.tts = tts.TextToSpeech()

    def button_click_command(self):
        tk_async_execute.async_execute(tts.text_to_speech(), visible=False)

    def run(self):
        self.root.mainloop()

    def file_picker(self):
       filepath = tkinter.filedialog.askopenfilename() 
       text = pdf_reader.extract_text(filepath)
       self.tts.set_text(text)
       tk_async_execute.async_execute(self.tts.text_to_speech(), visible=False)

    def build_window(self):
        self.root.title("BrainRotagen")
        self.root.geometry("400x800")  # width x height
        tkinter.Label(self.root, text="Kekagen").pack()
        tkinter.ttk.Button(self.root, text="Playeroni", command=self.button_click_command, width=20).pack(padx=20)
        tkinter.ttk.Button(self.root, text="Uploaderoni", command=self.file_picker, width=20).pack(padx=20)
