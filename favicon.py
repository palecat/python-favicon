import requests
import sys
import os
from urllib.parse import urlparse


def request_function(domain):
	result = urlparse(domain)
	domain = (result.netloc or result.path)
	url = 'https://www.google.com/s2/favicons?domain=' + domain

	os.makedirs('images' + os.sep, exist_ok=True)

	with open('images' + os.sep + domain + '.png', 'wb') as handler:
		handler.write(requests.get(url).content)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Specify domain!')
        sys.exit()
        
    request_function(sys.argv[1])
