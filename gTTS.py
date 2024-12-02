import sys
import subprocess
import os
from datetime import datetime
from gtts import gTTS

def speak(language, text_to_speak):
    # Create a gTTS object
    tts = gTTS(text=text_to_speak, lang=language, slow=False)
    
    # Create a unique name for the audio file using a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    audio_file = f"temp_audio_{timestamp}.mp3"
    
    # Save the audio file to a temporary file
    tts.save(audio_file)
    
    # Play the audio file using ffplay
    subprocess.run(["C:\\Tools\\ffmpeg\\ffmpeg-7.1-essentials_build\\bin\\ffplay.exe", "-nodisp", "-autoexit", audio_file])

    # Remove the audio file after playing (optional)
    os.remove(audio_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gTTS.py <language> <text>")
        sys.exit(1)

    language = sys.argv[1]
    text_to_speak = sys.argv[2]
    speak(language, text_to_speak)
