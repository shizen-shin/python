from bs4 import BeautifulSoup
import requests

from assets.database import db_session
from assets.models import Data

import datetime

def get_info():	
    url ='https://scraping-for-beginner.herokuapp.com/udemy'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    subsc = soup.select('.subscribers')[0].string
    review = soup.select('.reviews')[0].string

    n_subsc = int(subsc.split('：')[1])
    n_review = int(review.split('：')[1])

    results = {
        'n_subscribers': n_subsc,
        'n_reviews': n_review
    }

    return results


def update_data():
    #スクレイピングデータの読込み
    _results = get_info()

    #DBに書き込むデータ
    date = datetime.date.today() #datetime形式
    subscribers = _results['n_subscribers']
    reviews = _results['n_reviews']

    row = Data(date=date, subscribers= subscribers, reviews=reviews)

    db_session.add(row)
    db_session.commit()


if __name__=='__main__':
    update_data()