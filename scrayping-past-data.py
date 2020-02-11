from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')

url = 'https://minkabu.jp/stock/100000018/daily_bar'
browser.get(url)


#抽出件数の指定



#要素抽出
elems = browser.find_element_by_id('fourvalue_timeline')
elems = browser.find_elements_by_tag_name('tr')

titles = []
descriptions = []
dates = []

def extract():
    for elem_title in elem_titles:
        title = elem_title.text
        titles.append(title)

    #zip()でまとめて実行することもできる
    for elem_description, elem_date in zip(elem_descriptions, elem_dates):
        description = elem_description.text
        descriptions.append(description)

        date = elem_date.text
        dates.append(date)

extract()


#２ページ目から５ページ目まで
for i in range(2,6):

    url = 'https://suumo.jp/journal/new/page/{}'.format(i)
    browser.get(url)

    elem_titles = browser.find_elements_by_class_name('mediahzdtldata-title')
    elem_descriptions = browser.find_elements_by_class_name('mediahzdtldata-desc')
    elem_dates = browser.find_elements_by_class_name('mediahzdtldata-date')
    
    extract()


#番号を振る（更新日最新順）
ranks =[]

for rank in range(1,len(titles)+1):
    rank = int(rank)
    ranks.append(rank)


#表にする
import pandas as pd
df = pd.DataFrame()

df['rank']=ranks
df['title']=titles
df['description']=descriptions
df['date']=dates

#csvファイルで出力
df.to_csv("~/Downloads/suumoJernal_titles1-5pages.csv",index = False,encoding = "utf_8_sig")