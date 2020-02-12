#DBへの最新日付追加処理
#１ページ目のデータ取得し、現在DBになければ追加する ※休日は更新がないため
#取得データ最新日とDB内の最新日付と比較し、新しいデータがあればDBに追加


#1ページ目のデータ取得
from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')

url = 'https://minkabu.jp/stock/100000018/daily_bar'
browser.get(url)

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


#取得した日付をstr->dateにする(先頭＝最新日のみ)
import datetime
scraypedDate = datetime.datetime.strptime(dates[0],'%Y/%m/%d').date()
scraypedDate



#日付の比較
#scraypedDate:スクレイプした日付、latestDate:表の最上or最下で大きい方の日付

#DBの最新日(latestDate)
from assets.database import db_session
from assets.models import Data
import datetime


###日付を比較して、新しい日を見つける作戦。※一番下に新しい日付がくるとは限らない。ブロックで入れた場合など。→ 結局１つづつ比較するしかない
dbDates = db_session.query(Data.date).all()
dbDateTop = dbDates[0].date

#date列を１列ずつdatetime型に変換
for index, dbDate in enumerate(dbDates):
    dbDate = dbDates[index].date

    if dbDate > dbDateTop:
        latestDate = dbDate
    else:
        latestDate = dbDateTop

if scraypedDate > latestDate:

    #scraypしたデータを一列ずつrowに入れる（dateはdatetime型に変換）
    for date, start, high, low, end, adjusted in zip(dates, starts, highs, lows, ends, adjusteds):
        date = datetime.strptime(date,'%Y/%m/%d').date()

        row = Data(date = date, start = start, high = high, low = low, end = end, adjusted= adjusted)
        db_session.add(row)
    
    db_session.commit()

else:
    pass