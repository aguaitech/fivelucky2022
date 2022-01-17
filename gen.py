from random import random
import json
import os

preAct = []
aliAct = []
normAct = []

for fn in os.listdir("pages"):
    with open('pages/'+fn, encoding="utf-8") as f:
        j = json.load(f)
        channelNo = j[0]['data']['channelNo']
        if channelNo == 'AP-PRE':
            preAct.append((fn, j))
        elif channelNo in ["GOV-GJZWFWPT-C", "AP-PRE", "AP"]:
            aliAct.append((fn, j))
        else:
            normAct.append((fn, j))

optStr = ""

for fn, act in preAct+aliAct+normAct:
    if random() > 0.9:
        optStr = optStr + "B站 @阿拐AGUAI 发布"
    obj = act[0]['data']
    optStr += f"({obj['channelName']})"
    if random() > 0.9:
        optStr = optStr + "B站 @阿拐AGUAI 发布"
    optStr += f"{obj['brandBlessText']} https://render.alipay.com/p/yuyan/18002057000000{fn[:4]}-prod/index.html\n"

print(optStr)
