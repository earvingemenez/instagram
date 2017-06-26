CLIENT_ID = "7a31a68148894fa6a7b7e684b976d8f2"
CLIENT_SECRET = "9164461f447047e0ac54b6f2a2f4edf3"

from urllib import request, parse
import json

access_token = "28950154.7a31a68.14c2901c6847423a87c7029509f57810"
resp = request.urlopen('https://api.instagram.com/v1/tags/travel/media/recent?access_token=' + access_token)


data = resp.read().decode('utf-8')


import pdb;pdb.set_trace()