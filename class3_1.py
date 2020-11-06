from pprint import pprint
import requests as req, json

url = "http://localhost:9000/receive"

resGet = req.get(url)
print(resGet.text)
print()
dic_A = json.loads(resGet.text)
pprint(dic_A)

print()

resPost = req.post(url)
print(resPost.text)
print()
dic_B = json.loads(resPost.text)
pprint(dic_B)