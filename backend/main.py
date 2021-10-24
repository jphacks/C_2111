
import json
import requests

# goo
# Overview: Japanese Word Similarity API

app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
url_textpair = "https://labs.goo.ne.jp/api/textpair"
url_entity = "https://labs.goo.ne.jp/api/entity"
url_keyword = "https://labs.goo.ne.jp/api/keyword"


def textpair(word1, word2, request_id="record003"):
    # textpair API interface: https://labs.goo.ne.jp/api/textpair_doc
    payload = {"app_id": app_id, "request_id": request_id, "text1": word1, "text2":word2}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url_textpair, data=json.dumps(payload).encode(), headers=headers)
    return r

def entity(sentence:str, request_id:str = "record001", class_filter = None):
    payload = {"app_id":app_id, "request_id": request_id, "sentence": sentence, }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url_entity, data=json.dumps(payload).encode(), headers=headers)
    return r 

def keyword(title:str, body:str, request_id:str = "record001", max_num:int = 10, focus = None):
    payload = {
        "app_id":app_id, "request_id": request_id, 
        "title": title, "body": body, "max_num": max_num, "focus": focus
        }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url_keyword, data=json.dumps(payload).encode(), headers=headers)
    return r 

print("textpair")
textpair_result = textpair("人参", "白菜")
print(textpair_result.text)

print("entity")
entity_result = entity(sentence="俺はジャイアン、ガキ大将兼株式会社ドラえもんの社長。", request_id="record001")
print(entity_result.text)

print("keyword")
keyword_result = keyword(title="ドラえもんについて",body ="俺はジャイアン、ガキ大将兼株式会社ドラえもんの社長。", request_id="record001", focus="ORG")
print(keyword_result.text)
