# -*- coding: utf-8 -*-

import urllib.request

client_id = "728CDVyQIXeF2AKYzLka"
client_secret = "p1xv_mtdew"


def tts(sentence, speaker):
    text = urllib.parse.quote(sentence)
    data = "speaker=" + speaker + "&speed=0&text=" + text
    url = "https://openapi.naver.com/v1/voice/tts.bin"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if rescode == 200:
        print("TTS mp3 저장")
        response_body = response.read()
        with open('instant.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)
