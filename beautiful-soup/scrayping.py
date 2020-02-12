from bs4 import BeautifulSoup
import requests

import pandas as pd
import datetime
	
n_subsc =''
n_review=''

def get_info():	
	url ='https://scraping-for-beginner.herokuapp.com/udemy'
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	
	subsc = soup.select('.subscribers')[0].string
	review = soup.select('.reviews')[0].string
	
	n_subsc = int(subsc.split('：')[1])
	n_review = int(review.split('：')[1])

get_info()

def update_csv():	
    
    df = pd.read_csv('output/test-daily-data.csv')	

    date = datetime.datetime.today().strftime('%Y/%m/%d').replace('/0','/')
	
    results = pd.DataFrame([[date,n_subsc,n_review]],columns=['date','subscribers','reviews'])
    df = pd.concat([df,results])
	
    year = datetime.datetime.today().strftime('%y')
    month = datetime.datetime.today().strftime('%m')
    day = datetime.datetime.today().strftime('%d')
    hour = datetime.datetime.today().strftime('%H')
    minute = datetime.datetime.today().strftime('%M')
    second = datetime.datetime.today().strftime('%S')
    datesec = year + month + day + hour + minute + second
	
    df.to_csv('output/test-daily-data-{}.csv'.format(datesec), index = False, encoding = "utf_8_sig")


if __name__=='__main__':
    update_csv()