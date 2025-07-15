import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Get list of available voices
voices = engine.getProperty('voices')

# Print details of each voice
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.name}, ID: {voice.id}")
