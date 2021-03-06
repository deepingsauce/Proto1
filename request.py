from lxml import etree
import httplib
import urllib2
import xml.dom.minidom
import base64
import json

HOST = "220.230.117.99:3000"
API_URL = ""	# nodejs: /mycallback

def save_mp3(content):
	sound = open("sound.mp3","wb")
	sound.write(content)
	sound.close()

def get_request():
	server = httplib.HTTPConnection(HOST)
	server.request('GET', '/')
	content = server.getresponse()
	#print(content)
	

	save_mp3(content)
	return content

def post_request(content):
	print("post request")
	server = httplib.HTTP(HOST)
	server.putrequest("POST",API_URL)
	server.putheader("Host",HOST)
	server.putheader("User-Agent","Python post")
	#server.putheader("Content-type","text/xml; charset=\"UTF-8\"")
	server.putheader("Content-type","application/json; charset=\"UTF-8\"")
	server.putheader("Content-length", "%d" % len(content))
	server.endheaders()
	print("header end")
	server.send(content)
	print("sent")

	statuscode, statusmessage, header = server.getreply()
	result = server.getfile().read()
	save_mp3(result)

	print(statuscode, statusmessage, header)
	#print(result)

def send_image(imgfile_name):
	with open(imgfile_name,"rb") as image_file:
	    encoded_image = base64.b64encode(image_file.read())

	#with open("imageToSave.png", "wb") as fh:
	#    fh.write(encoded_image.decode('base64'))

	root = etree.Element("dps_din", page="")	# nodejs: /mycallback
	dev_id = etree.SubElement(root, "dev_id")
	dev_id.text = "0"
	img = etree.SubElement(root, "img")
	img.text = encoded_image
	#print(etree.tostring(root))
	post_request(etree.tostring(root))
	print("end")

def send_image_json(img_name, req_num):
	print("send_image_json")
	with open(img_name,"rb") as image_file:
		encoded_image = base64.b64encode(image_file.read())
	print("encode")

	root = {}
	root["dev_id"] = 0
	root["req_num"] = req_num
	root["img"] = encoded_image
	post_request(json.dumps(root))
	print("end")

#send_image_json("2017-09-13_14:54:12.jpg",20)
#send_image_json("img3.jpg",20)

'''
url = "http://220.230.117.99:3000/mycallback"
xml = """<?xml version='1.0' encoding='utf-8'?>
<a>6</a>"""
headers = {'Content-Type': 'application/xml'}
print requests.post(url,data=xml,headers=headers).text
'''

