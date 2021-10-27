import json
from typing import Any
import requests

class Goo:
    """
    gooAPIをpythonで使えるようにする
    """
    def __init__(self, app_id:str, request_id:str) -> None:
        self.app_id = app_id
        self.request_id = request_id

    def textpair(self, text1:str, text2:str) -> Any:
        # textpair API interface: https://labs.goo.ne.jp/api/textpair_doc
        url = "https://labs.goo.ne.jp/api/textpair"
        payload = {"app_id": self.app_id, "request_id": self.request_id, "text1": text1, "text2": text2}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload).encode(), headers=headers)
        return r

    def entity(self, sentence:str, class_filter = None) -> Any:
        url = "https://labs.goo.ne.jp/api/entity"
        payload = {"app_id": self.app_id, "request_id": self.request_id, "sentence": sentence}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload).encode(), headers=headers)
        return r 

    def keyword(self, title:str, body:str, max_num:int = 10, focus = None) -> Any:
        url = "https://labs.goo.ne.jp/api/keyword"
        payload = {
            "app_id":self.app_id, "request_id": self.request_id, 
            "title": title, "body": body, "max_num": max_num, "focus": focus
            }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload).encode(), headers=headers)
        return r 

    def morph(self, sentence:str, info_filter:str = "form|pos|read", pos_filter:str = None) -> Any:
        url = "https://labs.goo.ne.jp/api/morph"
        if pos_filter is None:
            payload = {
                "app_id":self.app_id, "request_id": self.request_id, "sentence":sentence, "info_filter":info_filter,
                }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload).encode(), headers=headers)
        return r 

    def slot(self, sentence:str, slot_filter:str = None) -> Any:
        url = "https://labs.goo.ne.jp/api/slot"
        if slot_filter is None:
            payload = {"app_id":self.app_id, "request_id": self.request_id, "sentence":sentence,}
        else:
            payload = {
                "app_id":self.app_id, "request_id": self.request_id, "sentence":sentence, "slot_filter":slot_filter
                }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload).encode(), headers=headers)
        return r 

    def hiragana(self, sentence:str, output_type:str = "hiragana") -> Any:
        url = "https://labs.goo.ne.jp/api/hiragana"
        payload = {"app_id":self.app_id, "request_id": self.request_id, "sentence":sentence, "output_type":output_type}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload).encode(), headers=headers)
        return r 
