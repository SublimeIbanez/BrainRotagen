import tkinter
import tk_async_execute
import tts


class Application:
    def __init__(self):
        root = tkinter.Tk()
        self.root = root
        self.build_window()

    def button_click_command(self):
        tk_async_execute.async_execute(tts.text_to_speech(), wait=True, visible=False, pop_up=False)

    def run(self):
        self.root.mainloop()
    
    def build_window(self):
        self.root.title("BrainRotagen")
        self.root.geometry("400x800")  # width x height
        tkinter.Label(self.root, text="Kekagen").pack()
        tkinter.ttk.Button(self.root, text="Playeroni", command=self.button_click_command, width=20).pack(padx=20)
