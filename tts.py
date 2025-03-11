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

    def set_text(self, text):
        self.text = text

    async def text_to_speech(self):
        text = ""
        if self.text:
            text = self.text
        else: 
            text = "Testeroni of the voiceroni. Hello, Aster, how are you today? I hope your day is well"
        self.engine.say(text)
        await self.engine.runAndWait()