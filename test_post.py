
import requests
import json

json_file = r'C:\Users\PC\workspace\appfi-wb-api\templates\info.json'
# url_json = 'https://reqres.in/api/users'
url_post = 'http://127.0.0.1:5000/jsontest'

d = json.loads(open(json_file).read())

# info_json = requests.get(url_json).text


post_info = requests.post(url_post, json=d)

print(post_info.text)
