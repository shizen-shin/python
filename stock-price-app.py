import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd 
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

from assets.database import db_session
from assets.models import Data

#DBの各列のデータを読み込む ＊データを個別に使うわけではないので、result型でOK
data = db_session.query(Data.date, Data.start, Data.high, Data.low, Data.end, Data.adjusted).all()

dates = []
starts = []
highs = []
lows = []
ends = []
adjusteds = []

#株価がstr型になっているため、浮動小数点floatになおす
for datum in data:
    dates.append(datum.date)
    starts.append(float(datum.start.replace(",","")))
    highs.append(float(datum.high.replace(",","")))
    lows.append(float(datum.low.replace(",","")))
    ends.append(float(datum.end.replace(",","")))
    adjusteds.append(float(datum.adjusted.replace(",","")))


#差分の取得　list形式ー＞Series形式に変更
diff_starts = pd.Series(starts).diff().values
diff_highs = pd.Series(highs).diff().values
diff_lows = pd.Series(lows).diff().values
diff_ends = pd.Series(ends).diff().values
diff_adjusteds = pd.Series(adjusteds).diff().values



#appを作る宣言。この下にhtml要素、dcc graph要素を書いていく
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H1(children = 'Japanese Stock price 推移'),
    html.H2(children = '[1]start price(始値)推移'),
    html.Div(children =[
        dcc.Graph(
            id = 'start-price with diff',
            figure = {
                'data':[
                    go.Scatter(
                        x=dates,
                        y=starts,
                        mode='lines',
                        marker = dict(size=4),
                        opacity =0.7,
                        yaxis='y1',
                        name = '始値'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_starts,
                        opacity =0.7,
                        yaxis='y2',
                        name = 'diff_starts'
                    ),
                ],
                'layout':go.Layout(
                    title='stock price（始値＋前日差分）',
                    xaxis = dict(title='date'),
                    yaxis = dict(title='始値', side='left',showgrid=False,
                        range = [10000, max(starts)+500]),
                    yaxis2 = dict(title='増減', side='right', overlaying='y', showgrid=False,
                        range = [min(diff_starts[:]), max(diff_starts[:])]),
                    margin=dict(l=200, r=200, b=100, t=100),    #marginの設定
                    legend = dict(
                        font = dict(),   # 凡例のフォント設定
                        x = 0.01, xanchor = 'left',  # 凡例の表示場所の設定
                        y = 0.95, yanchor = 'auto',
                        bordercolor = 'lightgray', borderwidth = 1,  # 凡例を囲む枠線の設定
                    )
                )
            }
        )
    ,dcc.Graph(
            id = 'start-price',
            figure = {
                'data':[
                    go.Scatter(
                        x=dates,
                        y=starts,
                        mode='lines+markers',
                        marker = dict(size=4),
                        opacity =0.7,
                        yaxis='y1',
                        name = '始値'
                    )
                ],
                'layout':go.Layout(
                    title='stock price（始値）',
                    xaxis = dict(title='date'),
                    yaxis = dict(title='始値', side='left',showgrid=False,
                        range = [10000, max(starts)+500]),
                    margin=dict(l=200, r=200, b=100, t=100),    #marginの設定
                    legend = dict(
                        font = dict(),   # 凡例のフォント設定
                        x = 0.01, xanchor = 'left',  # 凡例の表示場所の設定
                        y = 0.95, yanchor = 'auto',
                        bordercolor = 'lightgray', borderwidth = 1,  # 凡例を囲む枠線の設定
                    )
                )
            }
        )
    ,dcc.Graph(
            id = 'start-price-diff',
            figure = {
                'data':[
                    go.Bar(
                        x=dates,
                        y=diff_starts,
                        opacity =0.7,
                        yaxis='y1',
                        name = '始値前日差分'
                    )
                ],
                'layout':go.Layout(
                    title='stock price（始値前日差分）',
                    xaxis = dict(title='date'),
                    yaxis = dict(title='始値', side='right', overlaying='y', showgrid=False,
                        range = [min(diff_starts[:]), max(diff_starts[:])]),
                    margin=dict(l=200, r=200, b=100, t=100),    #marginの設定
                    legend = dict(
                        font = dict(),   # 凡例のフォント設定
                        x = 0.01, xanchor = 'left',  # 凡例の表示場所の設定
                        y = 0.95, yanchor = 'auto',
                        bordercolor = 'lightgray', borderwidth = 1,  # 凡例を囲む枠線の設定
                    )
                )
            }
        )
    ]),

        #高値(high)の推移
        html.H2(children = '[2]high price(高値)推移'),
        html.Div(children =[
        dcc.Graph(
            id = 'high-price with diff',
            figure = {
                'data':[
                    go.Scatter(
                        x=dates,
                        y=highs,
                        mode='lines',
                        marker = dict(size=4),
                        opacity =0.7,
                        yaxis='y1',
                        name = '始値'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_highs,
                        opacity =0.7,
                        yaxis='y2',
                        name = 'diff_highs'
                    ),
                ],
                'layout':go.Layout(
                    title='stock price（高値＋前日差分）',
                    xaxis = dict(title='date'),
                    yaxis = dict(title='高値', side='left',showgrid=False,
                        range = [10000, max(highs)+500]),
                    yaxis2 = dict(title='増減', side='right', overlaying='y', showgrid=False,
                        range = [min(diff_highs[:]), max(diff_highs[:])]),
                    margin=dict(l=200, r=200, b=100, t=100),    #marginの設定
                    legend = dict(
                        font = dict(),   # 凡例のフォント設定
                        x = 0.01, xanchor = 'left',  # 凡例の表示場所の設定
                        y = 0.95, yanchor = 'auto',
                        bordercolor = 'lightgray', borderwidth = 1,  # 凡例を囲む枠線の設定
                    )
                )
            }
        )
    ,dcc.Graph(
            id = 'high-price',
            figure = {
                'data':[
                    go.Scatter(
                        x=dates,
                        y=highs,
                        mode='lines+markers',
                        marker = dict(size=4),
                        opacity =0.7,
                        yaxis='y1',
                        name = '高値'
                    )
                ],
                'layout':go.Layout(
                    title='stock price（高値）',
                    xaxis = dict(title='date'),
                    yaxis = dict(title='高値', side='left',showgrid=False,
                        range = [10000, max(highs)+500]),
                    margin=dict(l=200, r=200, b=100, t=100),    #marginの設定
                    legend = dict(
                        font = dict(),   # 凡例のフォント設定
                        x = 0.01, xanchor = 'left',  # 凡例の表示場所の設定
                        y = 0.95, yanchor = 'auto',
                        bordercolor = 'lightgray', borderwidth = 1,  # 凡例を囲む枠線の設定
                    )
                )
            }
        )
    ,dcc.Graph(
            id = 'high-price-diff',
            figure = {
                'data':[
                    go.Bar(
                        x=dates,
                        y=diff_highs,
                        opacity =0.7,
                        yaxis='y1',
                        name = '高値前日差分'
                    )
                ],
                'layout':go.Layout(
                    title='stock price（高値前日差分）',
                    xaxis = dict(title='date'),
                    yaxis = dict(title='高値', side='right', overlaying='y', showgrid=False,
                        range = [min(diff_highs[:]), max(diff_highs[:])]),
                    margin=dict(l=200, r=200, b=100, t=100),    #marginの設定
                    legend = dict(
                        font = dict(),   # 凡例のフォント設定
                        x = 0.01, xanchor = 'left',  # 凡例の表示場所の設定
                        y = 0.95, yanchor = 'auto',
                        bordercolor = 'lightgray', borderwidth = 1,  # 凡例を囲む枠線の設定
                    )
                )
            }
        )
    ]),
    html.Div(children = [
        dcc.Markdown('''
        #### ------設定------
        - 対象：みん株から国内の株価推移データを取得
        - https://minkabu.jp/stock/100000018/daily_bar
        - 過去データscrayping:　WEB上で過去データ取得しcsv化。csvをDBに取り込み
        - 過去データのscraypingは、取得日数の選択が可能
        - Python実行でhttps://extract-past-stock-price-data.herokuapp.com/　が起動
        - WEB上から最新データ取得し、DBに入っていなければ追加
        - DB処理：ローカルはSQLite, heroku上ではPostgreSQL使用（by SQLAlchemy)
        - グラフ化：DBを読込みグラフを表示
        - 株価推移と前日差分を表示
        - (機能確認)下部グラフのx軸、y軸はフォント、カラー、傾きを個別に設定
        - (機能確認)凡例の位置を右上に変更。枠で囲み
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