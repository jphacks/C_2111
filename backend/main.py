
import json
import requests

# goo
# Overview: Japanese Word Similarity API

app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
url_textpair = "https://labs.goo.ne.jp/api/textpair"

def textpair(word1, word2, request_id="record003"):
    # textpair API interface: https://labs.goo.ne.jp/api/textpair_doc
    payload = {"app_id": app_id, "request_id": request_id, "text1": word1, "text2":word2}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url_textpair, data=json.dumps(payload).encode(), headers=headers)
    return r

result = textpair("人参", "白菜")
print(result.text)
print(result.json()["score"])

