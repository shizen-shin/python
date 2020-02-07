
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd 
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('output/test-daily-data.csv')

dates = []
for _date in df['date']:
    _date = str(_date)

    try:
        date = datetime.datetime.strptime(_date, '%Y/%m/%d').date()
        dates.append(date)
    except:
        pass

n_subscribers = df['subscribers'].values
n_reviews = df['reviews'].values

diff_subscribers = df['subscribers'].diff().values
diff_reviews = df['reviews'].diff().values


#appを作る宣言。この下にhtml要素、dcc graph要素を書いていく
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H2(children = 'pythonによるWebスクレイピングアプリ'),
    html.Div(children =[
        dcc.Graph(
            id = 'subscriber_graph',
            figure = {
                'data':[
                    go.Scatter(
                        x=dates,
                        y=n_subscribers,
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
                        range = [2100, max(n_subscribers)+100]),
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
                        y=n_reviews,
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
                        range = [0, max(n_reviews)+100],
                        tickfont = dict(size=12, color='green')
                    ),
                    yaxis2 = dict(title='増加数', side='right', overlaying='y', showgrid=False,
                        range = [0, max(diff_reviews[1:])])
                )
            }
        )
    ])
],
style = {
    'textAlign':'center',
    'width':'1200',
    'margin':'0 auto'
}
)

if __name__ == '__main__':
    app.run_server(debug=True)