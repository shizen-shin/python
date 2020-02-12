# coding: utf-8
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float  #型を宣言。一通り宣言しておく
from assets.database import Base
from datetime import datetime as dt

#Table情報
class Data(Base):  #「Data」というDBを作成 (エクセルのファイル名)
    #TableNameの設定
    __tablename__ = "data" #「Data」というテーブルを作成 (エクセルのシート名)

    #Column情報を設定する
    id = Column(Integer, primary_key=True)  #主キーに設定 primary_key=True:設定しなくても勝手に割り当てられるようになる、型:Integer
    date = Column(Date, unique=False)  #型:Date、unique=False:同じ数でもOK（Trueは重複を認めない）
    start = Column(Integer, unique=False)  #型:Integer
    high = Column(Integer, unique=False)
    low = Column(Integer, unique=False)
    end = Column(Integer, unique=False)
    adjusted = Column(Integer, unique=False)
    timestamp = Column(Integer, default=dt.now())  #DBをいつ保存したかのログ用。型:DateTime、現在時刻をデフォルトで出力  ＊なくても機能

    def __init__(self, date=None, start=None, high=None, low=None, end=None, adjusted=None, timestamp=None):  #初期化
        self.date = date
        self.start = start
        self.high = high
        self.low = low
        self.end = end
        self.adjusted = adjusted
        self.timestamp = timestamp
