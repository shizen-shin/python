# coding: utf-8
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date  #型を宣言。一通り宣言しておく
from assets.database import Base
from datetime import datetime as dt

#Table情報
class Data(Base):  #「Data」というDBを作成 (エクセルのファイル名)
    #TableNameの設定
    __tablename__ = "data" #「Data」というテーブルを作成 (エクセルのシート名)

    #Column情報を設定する
    id = Column(Integer, primary_key=True)  #主キーに設定 primary_key=True:設定しなくても勝手に割り当てられるようになる、型:Integer
    date = Column(Date, unique=False)  #型:Date、unique=False:同じ数でもOK（Trueは重複を認めない）
    subscribers = Column(Integer, unique=False)  #型:Integer
    reviews = Column(Integer, unique=False)
    timestamp = Column(DateTime, default=dt.now())  #DBをいつ保存したかのログ用。型:DateTime、現在時刻をデフォルトで出力  ＊なくても機能

    def __init__(self, date=None, subscribers=None, reviews=None, timestamp=None):  #初期化
        self.date = date
        self.subscribers = subscribers
        self.reviews = reviews
        self.timestamp = timestamp
