#パクタソで指定したKWの画像を取得（１ページ分）
#指定したサイズにリサイズし保存
#resize-imagesフォルダを作成し、検索KW名のフォルダを作成
#変更内容をcsvに一覧で保存
#csvの項目：もとの画像サイズ、変更後の画像サイズ、ファイル名、もとの画像URL


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
keyword = '河村友歌'
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


#取得した画像のサイズをsizesに格納
sizes = []
for url in urls:
    f = io.BytesIO(request.urlopen(url).read())
    img = Image.open(f)
    
    size = img.size
    sizes.append(size)


#保存用フォルダを作成（imagesフォルダ作成し、keyword名のフォルダを作成）
import os

if not os.path.isdir('resized-images'):
    os.mkdir('resized-images')

if not os.path.isdir('reseized-images/{}'.format(keyword)):
    os.mkdir('resized-images/{}'.format(keyword))


#リサイズ
 #サイズを指定
resizes = []
fileNames = []
    
height = 1200
width = 880

for index, url in enumerate(urls):
    f = io.BytesIO(request.urlopen(url).read())
    img = Image.open(f)
    img = img.resize((height,width)) 
    
    #拡張子を取得　(root:前方,ext:拡張子 + ?配下除去) ※.gifなどでエラーでない対応
    import os.path
    root, ext = os.path.splitext(url)
    ext = ext.split("?")
    ext = ext[0]

    img.save('resized-images/{A}/resized-paktaso{B}{C}'.format(A=keyword,B=index,C=ext))
    
    fileName = 'resized-paktaso{B}{C}'.format(B=index,C=ext)
    fileNames.append(fileName)
    
    resize = img.size
    resizes.append(resize)


#csv用のインデックス番号を配列に格納
numbers = []

for number in range(1,len(resizes)+1):
    number = int(number)
    numbers.append(number)


#表作成
import pandas as pd
df = pd.DataFrame()

df['No'] = numbers
df['original size']= sizes
df['resize']=resizes
df['fileName']= fileNames
df['url'] = urls


#downloadフォルダに出力
df.to_csv('resized-images/{}/file-summary.csv'.format(keyword), index = False,encoding = "utf_8_sig")

