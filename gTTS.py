import sys
import subprocess

def speak(language, text_to_speak):
    # Call gtts-cli as an external command
    gtts_command = [
        "C:\\Tools\\gTTS\\venv\\Scripts\\gtts-cli.exe",
        "--lang", language,
        "--"  # Tell gtts-cli that any following arguments are not options
    ] + [text_to_speak]  # Add the text to speak as an argument

    # Execute the command and pipe the output to ffplay
    ffplay_command = [
        "C:\\Tools\\ffmpeg\\ffmpeg-7.1-essentials_build\\bin\\ffplay.exe",
        "-nodisp", "-autoexit", "-"
    ]

    # Use subprocess to pipe the output of gtts-cli to ffplay
    gtts_process = subprocess.Popen(gtts_command, stdout=subprocess.PIPE)
    ffplay_process = subprocess.Popen(ffplay_command, stdin=gtts_process.stdout)

    # Close the stdout to allow gtts_process to terminate properly
    gtts_process.stdout.close()

    # Wait for both processes to complete
    gtts_process.wait()
    ffplay_process.wait()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gTTS.py <language> <text>")
        sys.exit(1)

    language = sys.argv[1]
    text_to_speak = sys.argv[2]
    speak(language, text_to_speak)