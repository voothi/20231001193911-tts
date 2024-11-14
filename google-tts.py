import os
import sys
import json
import base64

user_input = ' '.join(sys.argv[1:])

# Payload that we should send to google api
payload = '{"input":{"text":"%s"},"voice":{"languageCode":"en-US","name":"en-US-Wavenet-D"},"audioConfig":{"audioEncoding":"LINEAR16","pitch":"0.00","speakingRate":"1.00"}}' % user_input

# I used `proxychains` because this command returns 403 in my country, You can remove it if your county is not banned :)
command = f'curl \'https://cxl-services.appspot.com/proxy?url=https%3A%2F%2Ftexttospeech.googleapis.com%2Fv1beta1%2Ftext%3Asynthesize\' -H \'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0\' -H \'Accept: */*\' -H \'Accept-Language: en-US,en;q=0.5\' -H \'Referer: https://cloud.google.com/text-to-speech/\' -H \'Content-Type: text/plain;charset=UTF-8\' -H \'Origin: https://cloud.google.com\' -H \'Connection: keep-alive\' -H \'TE: Trailers\' --data \'{payload}\''

# Run in command line and read result
response = os.popen(command).read()

# Convert json string to Dictionary and get value
base64_audio = json.loads(response).get('audioContent')

# Write voice to file
with open('file.wav', 'wb') as file:
    file.write(base64.b64decode(base64_audio))

# Play voice
os.system('play file.wav')