from goo_lab.goo_apis import Goo

app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
g = Goo(app_id=app_id, request_id="record001").textpair(text1="日本人", text2="アメリカ人")
print(g.text)

sentence = "俺はジャイアン、ガキ大将兼株式会社ドラえもんの社長。"
g = Goo(app_id=app_id, request_id="record001").entity(sentence=sentence)
print(g.text)

sentence = "俺はジャイアン、ガキ大将兼株式会社ドラえもんの社長。"
g = Goo(app_id=app_id, request_id="record001").keyword(
    title="ドラえもんについて", 
    body = "このAPIを用いることにより、人名などの記述内容に差異のあるデータベース間で同一内容を示すレコードを探し出す分析などが容易になります。また顧客からの問い合わせ情報で、自社商品名が多様な書き方で表現されている場合の集計作業などにも適用可能です。",
    focus="ORG"
    )
print(g.text)

print("形態素解析")
sentence = "俺はジャイアン、ガキ大将兼株式会社ドラえもんの社長。"
g = Goo(app_id=app_id, request_id="record001").morph(sentence=sentence)
print(g.text)

print("スロット値")
sentence = "名前は田中太郎で、男性で、30歳です。港区芝浦3-4-1に住んでいます。"
g = Goo(app_id=app_id, request_id="record001").slot(sentence=sentence)
print(g.text)