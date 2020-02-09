import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd 
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

from assets.database import db_session
from assets.models import Data

data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()

dates = []
subscribers = []
reviews = []

for datum in data:
    dates.append(datum.date)
    subscribers.append(datum.subscribers)
    reviews.append(datum.reviews)

 #差分の取得　list形式ー＞Series形式に変更
diff_subscribers = pd.Series(subscribers).diff().values
diff_reviews = pd.Series(reviews).diff().values



#appを作る宣言。この下にhtml要素、dcc graph要素を書いていく
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H1(children = 'グラフ描画アプリ'),
    html.Div(children =[
        dcc.Graph(
            id = 'subscriber_graph',
            figure = {
                'data':[
                    go.Scatter(
                        x=dates,
                        y=subscribers,
                        mode='lines+markers',
                        marker = dict(size=4),
                        opacity =0.7,
                        yaxis='y1',
                        name = 'subscribers'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_subscribers,
                        opacity =0.7,
                        yaxis='y2',
                        name = 'diff_subscribers'
                    ),
                ],
                'layout':go.Layout(
                    title='加入者数の推移',
                    xaxis = dict(title='日付'),
                    yaxis = dict(title='加入者数', side='left',showgrid=False,
                        range = [2100, max(subscribers)+100]),
                    yaxis2 = dict(title='増加数', side='right', overlaying='y', showgrid=False,
                        range = [0, max(diff_subscribers[1:])]),
                    margin=dict(l=200, r=200, b=100, t=100),    #marginの設定
                    legend = dict(
                        font = dict(),   # 凡例のフォント設定
                        x = 0.01, xanchor = 'left',  # 凡例の表示場所の設定
                        y = 0.95, yanchor = 'auto',
                        bordercolor = 'lightgray', borderwidth = 1,  # 凡例を囲む枠線の設定
                    )
                ),
            }
        ),
        dcc.Graph(
            id = 'revirews_graph',
            figure = {
                'data':[
                    go.Scatter(
                        x=dates,
                        y=reviews,
                        mode='lines+markers',
                        opacity =0.7,
                        yaxis='y1',
                        name = 'reviews'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_reviews,
                        opacity =0.7,
                        yaxis='y2',
                        name = 'diff_revirews'
                    ),
                ],
                'layout':go.Layout(
                    title='加入者数の推移',
                    xaxis = go.XAxis(
                        title = '日付',
                        tickfont = dict(size=9, color='darkblue',),
                        tickangle = 45
                        ),
                    yaxis = go.YAxis(
                        title='レビュー数',
                        side='left',
                        showgrid=False,
                        range = [0, max(reviews)+100],
                        tickfont = dict(size=12, color='green')
                    ),
                    yaxis2 = go.YAxis(
                        title='増加数', 
                        side='right', 
                        overlaying='y', 
                        showgrid=False,
                        tickfont = dict(size=12, color='darkgray'),
                        range = [0, max(diff_reviews[1:])]
                        ),
                    legend = dict(
                        font = dict(),   # 凡例のフォント設定
                        x = 0.01, xanchor = 'left',  # 凡例の表示場所の設定
                        y = 0.95, yanchor = 'auto',
                        bordercolor = 'lightgray', borderwidth = 1,  # 凡例を囲む枠線の設定
                    ),
                        margin=dict(l=200, r=200, b=100, t=100),    #marginの設定
                )
            }
        )
    ]),
    html.Div(children = [
        dcc.Markdown('''
        #### ------設定------
        - Heroku上でグラフを描画
        - csvローデータをDBに読込
        - WEB上から最新日のデータを取得しDBに追加（スケジューラーで自動取得登録）
        - DB ローカル：SQLite,Heroku PorstgreSQL 
        - githubでHerokuにデータをpush
        - グラフ描画：dash
        - (機能確認)下部グラフのx軸、y軸はフォント、カラー、傾きを個別に設定
        - (機能確認)凡例の位置を右上に変更。枠で囲み
        - データ取得：beautiful soup
        '''),
    ])
],

style = {
    'textAlign':'center',
    'max-width':'900',
    'margin':'0 auto'
}
)

if __name__ == '__main__':
    app.run_server(debug=True)