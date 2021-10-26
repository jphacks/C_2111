import requests

resp = requests.post("http://localhost:5000/predict")

print(resp.text)

# textpair
resp = requests.post("http://localhost:5000/textpair")

print(resp.text)