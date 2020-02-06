
import dash
import dash_core_components as dcc
import dash_html_components as html

#graph objectsのimport
import plotly.graph_objs as go

#csvファイルを読み込む
import pandas as pd
df = pd.read_csv('stock-price.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#appを作る宣言。この下にhtml要素、dcc graph要素を書いていく
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(
        id='line-graph',
        figure={
            'data':[
                go.Scatter(
                    x=df['date'],
                    y=df['microsoft'],
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size':15,
                    },
                    name = 'microsoft'
                ),
                go.Scatter(
                    x=df['date'],
                    y=df['apple'],
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size':15,
                    },
                    name = 'apple'
                ),
            ],
            'layout':go.Layout(
                xaxis ={'title':'date'},
                yaxis ={'title':'stock price'},
                height = 500,
            )
        }

    )
])



#appの実行
#debug = Trueで自動更新
if __name__ == '__main__':
    app.run_server(debug=True)
