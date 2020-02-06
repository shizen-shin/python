
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#appを作る宣言。この下にhtml要素、dcc graph要素を書いていく
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)




#appの実行
#debug = Trueで自動更新
if __name__ == '__main__':
    app.run_server(debug=True)
