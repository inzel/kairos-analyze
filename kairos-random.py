# Credit to https://github.com/kpphillips for this. I came across this and used it to learn more about this API.

import requests
import json
from PIL import Image
import Constants

def getRandomPhotoUrl():
	#url='http://tinyfac.es/api/users'
	r=requests.get("http://tinyfac.es/api/users")
	parsed_json=json.loads(r.content)
	avatarUrl=parsed_json[-1]['avatars'][3]['url']
	return avatarUrl

def analyzeRandomPhoto():
	headers = {
		"app_id": Constants.api_id,
		"app_key": Constants.api_key
	}
	
	imageUrl = getRandomPhotoUrl()
	payload = '{"image":' + '"' + imageUrl + '"' + '}'
	
	imageResponse = requests.get(imageUrl, stream=True)
	im = Image.open(imageResponse.raw)
	im.show()
	
	url = "https://api.kairos.com/detect"
	
	r = requests.post(url, data=payload, headers=headers)
	
	parsed_json = json.loads(r.content)
	attr = parsed_json['images'][0]['faces'][0]['attributes']
	print(json.dumps(attr, indent=2))
	
	return attr
	
analyzeRandomPhoto()
