from PIL import Image

import io
from urllib import request

from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')

#パクタソトップを開く
url = 'https://www.pakutaso.com/'
browser.get(url)


elem_search = browser.find_element_by_id('headerSearch')
elem_search.clear()

#クエリを入力
keyword = '犬'
elem_search.send_keys(keyword)

elem_button = browser.find_element_by_class_name('search__form')
button_click = elem_button.find_element_by_class_name('search__submit').click()



urls = []

#1ページ目の画像srcを取得
def PictureSrcs():

    elem_pictures = browser.find_elements_by_class_name('photoEntries__thumb')

    for index, elem_picture in enumerate(elem_pictures):
        picture = elem_picture.find_element_by_tag_name('img')
        url = picture.get_attribute('src')
        urls.append(url)

PictureSrcs()


#何ページ目まで取得するか指定
n = 3

　　#ページ数足りない場合にスキップ
try:
    for _ in range(1,n+1):

        next = browser.find_element_by_id('fs-pagenation')
        next = next.find_element_by_class_name('fs-next-link.fs-turn-page-link').click()

        PictureSrcs()
        
except:
    pass


#保存用フォルダを作成（imagesフォルダ作成し、keyword名のフォルダを作成）
import os

if not os.path.isdir('images'):
    os.mkdir('images')

if not os.path.isdir('images/{}'.format(keyword)):
    os.mkdir('images/{}'.format(keyword))



#画像に名前をつけて保存（index番号＋拡張子）
for index, url in enumerate(urls):    

    #拡張子を取得　(root:前方,ext:拡張子 + ?配下除去) ※.gifなどでエラーでない対応
    import os.path
    root, ext = os.path.splitext(url)
    ext = ext.split("?")
    ext = ext[0]

    f=io.BytesIO(request.urlopen(url).read())
    img = Image.open(f)
    img.save('images/{A}/paktaso{B}{C}'.format(A=keyword,B=index,C=ext))