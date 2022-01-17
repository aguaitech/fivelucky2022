import requests
import json
import tqdm
import re

# for i in tqdm.tqdm(range(2267, 2306)):
for i in tqdm.tqdm(range(2000, 2500)):
    res = requests.get(
        f'https://render.alipay.com/p/yuyan/18002057000000{i}-prod/index.html')
    regex = re.compile('window\.__component_schema_data_list__ = (.*);')
    match = regex.search(res.text)
    if match:
        j = match.group(1)
        try:
            o = json.loads(j)
            if len(o) == 1 and o[0].get('name') == '@alipay/preheat-2022':
                with open(f'pages/{i}.json', 'w+', encoding='utf-8') as f:
                    f.write(j)
        except Exception:
            pass
    else:
        # print('Not found for', i)
        pass
