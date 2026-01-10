@echo off
setlocal

set "Language=%~1"
set "TextToSpeak=%~2"
rem echo %TextToSpeak%
rem pause

@REM gtts-cli --lang "%Language%" "%TextToSpeak%" | ffplay -nodisp -autoexit -
C:\Tools\gTTS\venv\Scripts\gtts-cli.exe --lang "%Language%" "%TextToSpeak%" | C:\Tools\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffplay.exe -nodisp -autoexit -


