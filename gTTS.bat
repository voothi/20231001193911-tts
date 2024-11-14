@echo off
setlocal

set "Language=%~1"
set "TextToSpeak=%~2"
rem echo %TextToSpeak%
rem pause

gtts-cli --lang "%Language%" "%TextToSpeak%" | ffplay -nodisp -autoexit -