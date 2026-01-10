param (
    [string]$VoiceName,
    [string]$TextToSpeak
)

Add-Type -AssemblyName System.Speech
$SpeechSynthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer
$SpeechSynthesizer.SelectVoice($VoiceName)
$SpeechSynthesizer.Speak($TextToSpeak)
