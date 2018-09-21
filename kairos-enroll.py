import photos
import requests
import io
import base64
import json

img = photos.capture_image()

def getPhoto():
	with io.BytesIO() as output:
		#img = photos.capture_image()
		img.save(output, 'JPEG')
		contents = output.getvalue()
		image = base64.b64encode(contents)	
	return image

def enrollPhoto():
	subject_id = raw_input("Hello, What is your name: ? ")
	print("Thank you " + subject_id + "." + " Analyzing...")
	image = getPhoto()
	url = "https://api.kairos.com/enroll"
	values = {
		'image': image,
		'subject_id': subject_id,
		'gallery_name': 'test'
	}
	headers = {
		'Content-Type': 'application/json',
		'app_id': '*****************',
		'app_key': '**********************'
	}	
	r = requests.post(url, data=json.dumps(values), headers = headers)
	parsed_json = json.loads(r.content)
	attr = parsed_json['images'][0]['attributes']
	img.show()
	print(json.dumps(attr, indent=2))

enrollPhoto()
