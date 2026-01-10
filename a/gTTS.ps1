param (
    [string]$TextToSpeak
)

# gtts-cli --lang de "$TextToSpeak" | ffplay -nodisp -autoexit -
# $command = "gtts-cli --lang de "$TextToSpeak" | ffplay -nodisp -autoexit -"
# Invoke-Expression "$command"
$command = "gtts-cli --lang de ""$TextToSpeak"" | ffplay -nodisp -autoexit -"
Invoke-Expression "cmd /c `"$command`""