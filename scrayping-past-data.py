#取得日数の指定(先に選択されている想定))
from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')

url = 'https://stock-price-app-miyasaka.herokuapp.com/'
browser.get(url)

#指定された日付を取得（addeventlistnerは組めないっぽい）
#表示に時間かかるため10秒待機(3秒では早い。この間に選択可)
import time
time.sleep(10)

selectDays = browser.find_element_by_class_name('Select-value')
selectDays = selectDays.text

if selectDays == '20(約20日分)':
    selectDay = 20
elif selectDays == '60(約2ヶ月分)':
    selectDay = 60
elif selectDays == '180(約6ヶ月分)':
    selectDay = 180
elif selectDays == '400(約1年分)':
    selectDay = 400
elif selectDays == '800(約2年分)':
    selectDay = 800
elif selectDays == '1200(約3年分)':
    selectDay = 1200
else:
    print('error')   


#ページ送りの数算出（math.celi：繰り上げ *仮に30日など20で割り切れない場合に使用）
import math
i = math.ceil(selectDay/20)-1

url2 = 'https://minkabu.jp/stock/100000018/daily_bar'
browser.get(url2)


#自動更新を止める
btn = browser.find_element_by_xpath('//*[@id="h_top"]/ul/li[1]')
stop = btn.click()


#さらに表示ボタンを押す 繰り返し処理
#クリックを押すのが早すぎて要素が見つかっていない -> time.sleep(秒)：指定時間待機
import time
for _ in range(i):
    more = browser.find_element_by_class_name('moreContent,tac,mt10')
    more.click()
    time.sleep(0.5)

#要素抽出
elems = browser.find_element_by_id('fourvalue_timeline')
elems = elems.find_elements_by_tag_name('tr')

dates = []
starts = []
highs = []
lows = []
ends = []
adjusteds = []

#取得データを各listに入れる *0行目はタイトルのため不要
def extract():
    for elem in elems[1:]:      #list[start:end]
        data = elem.text.split(" ")
        
        date = data[0]
        start = data[1]
        high = data[2]
        low = data[3]
        end = data[4]
        adjusted = data[5]

        dates.append(date)
        starts.append(start)
        highs.append(high)
        lows.append(low)
        ends.append(end)
        adjusteds.append(adjusted)

extract()


#表にする
import pandas as pd
df = pd.DataFrame()

df['date']=dates
df['start']=starts
df['high']=highs
df['low']=lows
df['end']=ends
df['adjusted']=adjusteds


#csv出力
df.to_csv("~/Downloads/japanese-stock-price.csv",index = False,encoding = "utf_8_sig")