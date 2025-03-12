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
        self.text = ""
        self.text_to_speech = tts.TextToSpeech()
        self.root = tkinter.Tk()
        self.build_window()

    def button_click_command(self):
        tk_async_execute.async_execute(tts.text_to_speech(), visible=False)

    def run(self):
        self.root.mainloop()

    def file_picker(self):
       filepath = tkinter.filedialog.askopenfilename() 
       self.text = pdf_reader.extract_text(filepath)
       if hasattr(self, "text_box"):
            self.text_box.delete("1.0", "end")
            self.text_box.insert("1.0", self.text)

    def export(self):
        filepath = tkinter.filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Export text as..."
        )
        if filepath: 
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(self.text)
            print(f"Text exported to {filepath}")
    
    def toggle_tts(self):
       if not self.tts_playing:
           self.tts_playing = True
           self.start_stop_button.config(text="Stop")
           tk_async_execute.async_execute(self.text_to_speech.play(self.text), visible=False)
       else:
           self.tts_playing = False
           self.start_stop_button.config(text="Start")
           self.text_to_speech.stop()

    def build_window(self):
        self.root.title("BrainRotagen")
        self.root.configure(background="#4C484D")
        self.root.geometry("800x800")  # width x height

        # Side bar
        sidebar_frame = tkinter.Frame(self.root, width=200, height=400, bg="skyblue")
        sidebar_frame.pack(padx=5, pady=5, side=tkinter.LEFT, fill=tkinter.Y)
        tkinter.Label(sidebar_frame, text="Options", bg="skyblue").pack(padx=5, pady=5)

        # voice selection menu
        voice_selection_frame_color = "#777f8c"
        voice_selection_frame = tkinter.Frame(sidebar_frame, width=100, height=50, bg=voice_selection_frame_color)
        voice_selection_frame.pack(padx=5, pady=5, fill=None, expand=False)
        tkinter.Label(voice_selection_frame, text="Voice", fg="white", bg=voice_selection_frame_color).pack(padx=5, pady=5)
        voice_options = self.text_to_speech.get_voice_options()
        voice_names = []
        voice_dict = {str.split(voice.name, "-")[0]: voice.id for voice in voice_options}
        voice_names = list(voice_dict.keys()) 
        voice_selection_var = tkinter.StringVar(value=voice_names[0])
        def voice_changed(*args):
            selected_voice = voice_selection_var.get()
            voice_id = voice_dict[selected_voice]
            self.text_to_speech.set_voice(voice_id)
            print(f"Voice changed to: {selected_voice} ({voice_id})")
        voice_selection_var.trace_add("write", lambda *args: voice_changed())
        tkinter.OptionMenu(voice_selection_frame, voice_selection_var, *voice_names).pack(padx=5, pady=2)
        voice_test_button = tkinter.Button(voice_selection_frame, text="Test", command=lambda: tk_async_execute.async_execute(self.text_to_speech.test_voice(), visible=False), width=10)
        voice_test_button.pack(padx=5, pady=2, side=tkinter.LEFT)
        
        # file selection menu
        file_selection_frame_color = "#777f8c"
        file_selection_frame = tkinter.Frame(sidebar_frame, width=100, height=50, bg=file_selection_frame_color)
        file_selection_frame.pack(padx=5, pady=5, fill=tkinter.X)
        tkinter.Label(file_selection_frame, text="PDF", fg="white", bg=file_selection_frame_color).pack(padx=5, pady=5)
        tkinter.Button(file_selection_frame, text="Select PDF", command=self.file_picker, width=20).pack(padx=5, pady=2)

        # primary frame
        primary_frame = tkinter.Frame(self.root, width=400, height=700, bg="grey")
        primary_frame.pack(padx=5, pady=5, fill=tkinter.BOTH, expand=True)
        notebook = tkinter.ttk.Notebook(primary_frame)
        notebook.pack(expand=True, fill=tkinter.BOTH)

        text_tab = tkinter.Frame(notebook, bg="lightblue")
        self.text_box = tkinter.Text(text_tab, undo=True)
        self.text_box.pack(expand=True, fill=tkinter.BOTH, padx=10, pady=10)
        self.text_box.insert("1.0", self.text)
        def on_text_modified(event):
            self.text = self.text_box.get("1.0", "end-1c")  # "end-1c" removes the trailing newline.
            self.text_box.edit_modified(False)
        self.text_box.bind("<<Modified>>", on_text_modified)
        self.tts_playing = False
        self.start_stop_button = tkinter.Button(text_tab, text="Start", command=self.toggle_tts, width=10)
        self.start_stop_button.pack(padx=5, pady=10, side=tkinter.LEFT)
        export_text_button = tkinter.Button(text_tab, text="Export", command=self.export, width=10)
        export_text_button.pack(padx=5, pady=10, side=tkinter.RIGHT)

        video_tab = tkinter.Frame(notebook, bg="lightgreen")

        notebook.add(text_tab, text="Text")
        notebook.add(video_tab, text="Video")
