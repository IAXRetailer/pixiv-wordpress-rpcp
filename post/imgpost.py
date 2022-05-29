from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

import post as POSTAPI

def postimg(filename):
	client = Client(POSTAPI.SITE,POSTAPI.USER,POSTAPI.PASSWORD)

# prepare metadata
	data = {
	'name': 'picture.jpg',
	'type': 'image/jpeg',
	}

# read the binary file and let the XMLRPC library encode it into base64
	with open(filename, 'rb') as img:
		data['bits'] = xmlrpc_client.Binary(img.read())

	response = client.call(media.UploadFile(data))
# response == {
#       'id': 6,
#       'file': 'picture.jpg'
#       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
#       'type': 'image/jpeg',
# }
	return response