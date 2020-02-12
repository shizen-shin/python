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


def read_data():
    #csvファイルの内容読込み
    from assets import models
    import pandas as pd
    import datetime

    df = pd.read_csv('assets/japanese-stock-price.csv')

    #for文で各配列を抽出（dateはstr->dateに形式を変換)
    for index, _df in df.iterrows():
        date = datetime.datetime.strptime(_df['date'],'%Y/%m/%d').date() 
        row = models.Data(date = date, start = _df['start'], high = _df['high'], low = _df['low'], end = _df['end'], adjusted= _df['adjusted'])
        db_session.add(row)
    db_session.commit()
