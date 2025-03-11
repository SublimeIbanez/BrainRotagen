import pyttsx3


async def text_to_speech():
    text = "Testeroni of the voiceroni. Hello, Aster, how are you today? I hope your day is well"
    engine = pyttsx3.init()
    
    rate = engine.getProperty("rate")
    print(f"Current speaking rate: {rate}")
    engine.setProperty("rate", 170)
    
    volume = engine.getProperty("volume")
    print(f"Current volume: {volume}")
    engine.setProperty("volume", 1.0) 
    
    voices = engine.getProperty("voices")
    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"\tVoice {index}: {voice.name}")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    await engine.runAndWait()