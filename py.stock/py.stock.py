import requests
from io import StringIO
import pandas as pd
import numpy as np
import json
import datetime

import matplotlib
matplotlib.use('Agg')

datestr = datetime.date.today().strftime('%Y%m%d')

# 下載股價
r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')



# 整理資料，變成表格
df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
                                     for i in r.text.split('\n') 
                                     if len(i.split('",')) == 17 and i[0] != '='])), header=0)


# print(df[['證券代號','證券名稱','成交股數','成交筆數','成交金額','開盤價','最高價','最低價','收盤價']])

df[['證券代號','證券名稱','成交股數','成交筆數','成交金額','開盤價','最高價','最低價','收盤價']].to_json(datestr + '.json', force_ascii=False)

#with open('data.json', 'w') as outfile:
#    json.dump(data, outfile)


json_data=open(datestr + '.json').read()

data = json.loads(json_data)

print(json_data)