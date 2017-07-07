import io
import os
import css

# Imports the Google Cloud client library
from google.cloud import vision

def vision_analysis():
	# Instantiates a client
	vision_client = vision.Client()
	
	# The name of the image file to annotate
	file_name = os.path.join(os.path.dirname(__file__),'img3.jpg')
	print('Processing Img : ' + file_name + '\n')

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()
	    image = vision_client.image(content=content)

	# Performs label detection on the image file
	labels = image.detect_labels()
	sentence = ""
	speaker = "mijin"  # mijin:미진(한국어, 여성), jinho:진호(한국어, 남성), clara:클라라(영어, 여성), matt:매튜(영어, 남성), yuri:유리(일본어, 여성),# shinji:신지(일본어, 남성), meimei:메이메이(중국어, 여성)

	print('Labels:')
	for label in labels:
		print(label.description)
		sentence += " " + label.description
	print('Sentence:')
	print(sentence)

	css.tts(sentence=sentence, speaker=speaker)
