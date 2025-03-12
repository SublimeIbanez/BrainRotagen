import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.text = ""
        self.engine = pyttsx3.init()
        
        rate = self.engine.getProperty("rate")
        print(f"Current speaking rate: {rate}")
        self.engine.setProperty("rate", 190)
        
        volume = self.engine.getProperty("volume")
        print(f"Current volume: {volume}")
        self.engine.setProperty("volume", 0.5) 
        
        voices = self.engine.getProperty("voices")
        print("Available voices:")
        for index, voice in enumerate(voices):
            print(f"\tVoice {index}: {voice.name}")
        self.engine.setProperty("voice", self.engine.getProperty("voices")[0].id)

    def get_voice_options(self):
        return self.engine.getProperty("voices")
    
    def set_voice(self, voice_id):
        self.engine.setProperty("voice", voice_id)
    
    async def test_voice(self):
        text = "This is how the voice sounds"
        self.engine.say(text)
        self.engine.runAndWait()

    async def play(self):
        text = self.text or "Nothing Selected"
        self.engine.say(text)
        self.engine.runAndWait()

    async def play(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()