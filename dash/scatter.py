
import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np  #乱数の生成
import plotly.graph_objs as go  #散布図用のオブジェクト(go=graph objects)


#決まった乱数を用意する（学習用）
np.random.seed(1)

#乱数を50個用意する 0~100までで50個作成
x1 = np.random.randint(0, 100, 50) 
y1 = np.random.randint(0, 100, 50)

np.random.seed(2)
x2 = np.random.randint(0, 100, 50) 
y2 = np.random.randint(0, 100, 50)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#appを作る宣言。この下にhtml要素、dcc graph要素を書いていく
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#<本文>　app.layout([])でタグを定義。dcc.Graph()でグラフを定義
 #グラフの大枠作成はdcc.Graph()で行う。グラフへの数字反映はplotly.graph_objs=goを使う
app.layout = html.Div(children=[
    html.H1(
        children='Scatter Graph',
        style ={
            'textAlign':'center',
            'fontSize':'40px'
        }
    ),

    dcc.Graph(
        id ='scatter',
        figure ={
            'data':[
                go.Scatter(
                    x=x1,
                    y=y1,
                    mode='markers',
                    opacity=0.6,
                    marker = {
                        'size':12
                    }, 
                    name = '凡例１'
                ),
                go.Scatter(
                    x=x2,
                    y=y2,
                    mode='markers',
                    opacity=0.6,
                    marker = {
                        'size':12
                    }, 
                    name = '凡例２'
                )

            ],
            'layout':go.Layout(
                xaxis = {'title':'x軸'},
                yaxis = {'title':'y軸'},
            )
        }


    )
])




#appの実行
#debug = Trueで自動更新
if __name__ == '__main__':
    app.run_server(debug=True)
