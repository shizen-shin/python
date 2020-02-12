# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime
import os

databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')  #ファイル名「data.db」、絶対パス(abspath)でファイルの保存先を指定
engine = create_engine(os.environ.get('DATABASE_URL') or 'sqlite:///' + databese_file, convert_unicode=True , echo=True)  #どのDBを使うか: 本番環境はDATABASE_URL(herokuのPostgreSQL),ローカルは「sqlite:///」、echo=True:作業時にSQLを出力するか
db_session = scoped_session(  #オプションを記載（いじらなくてOK）
                sessionmaker(
                    autocommit = False,  #自動でコミット：しない
                    autoflush = False,  #自動反映: しない
                    bind = engine
                )
             )
Base = declarative_base() 
Base.query = db_session.query_property()

def init_db():    #DBの初期化
    import assets.models
    Base.metadata.create_all(bind=engine)


def read_data():  #初期データの読込(csv)
    from assets import models
    #from assets.database import db_session
    import pandas as pd
    import datetime

    df = pd.read_csv('japanese-stock-price.csv')

    for index, _df in df.iterrows():
        date = datetime.datetime.strptime(_df['date'],'%Y/%m/%d').date()
        row = models.Data(date = date, subscribers = _df['subscribers'], reviews = _df['reviews'])
        db_session.add(row)
    db_session.commit()
