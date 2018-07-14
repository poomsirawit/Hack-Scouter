# Adding certificate verification
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
from io import BytesIO
from PIL import Image, ImageDraw

import cognitive_face as CF

# Endpoint: https://westcentralus.api.cognitive.microsoft.com/face/v1.0
# Key 1: 384d9d63abaf41cb8b9bcb5be8d41645
# Key 2: e42128e1c50948d4b85275a39ffba132

KEY = '384d9d63abaf41cb8b9bcb5be8d41645'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

# SEA: southeastasia.api.cognitive.microsoft.com
#BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0/'
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
faces = CF.face.detect(img_url)

print(faces)

#Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))

#Download the image from the url
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

#For each face returned use the face rectangle and draw a red box.
draw = ImageDraw.Draw(img)
for face in faces:
    draw.rectangle(getRectangle(face), outline='red')

#Display the image in the users default image browser.
img.show()
