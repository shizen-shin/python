from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')

# Chromeの検索結果「hello」を開く
browser.get('https://www.google.com/search?q=hello&rlz=1C1SQJL_jaJP784JP784&oq=hello&aqs=chrome..69i57.2534j0j1&sourceid=chrome&ie=UTF-8')
elem_search = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input')
elem_search.clear()

# 指定したKWを検索（ここではSEO）
elem_search.send_keys('SEO')
elem_next = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/button').click()


#5ページ目までの自然検索タイトル一覧を取得
titles =[]

def extractTitle():

    elems_title= browser.find_elements_by_class_name('LC20lb')
    for elem_title in elems_title:
        title = elem_title.text
        titles.append(title)

    next = browser.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()

for _ in range(5):
    extractTitle()

#順位を取得
ranks = []

for i in range(1,len(titles)+1):
    rank = int(i)
    ranks.append(rank)


import pandas as pd
df = pd.DataFrame()

df['rank']=ranks
df['title']=titles

  #downloadフォルダに出力
df.to_csv("~/Downloads/search_SEO_titles_5pages.csv",index = False,encoding = "utf_8_sig")