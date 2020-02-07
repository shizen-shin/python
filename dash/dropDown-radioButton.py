
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# html.Label('見出し')
# ドロップダウン：dcc.Dropdown(options=[],value=)　valueは初期値
# マルチセレクト: Dropdownと同じ。valueがlist形式になる　value=['A','b'] + multi=True
# ラジオボタン： dcc.Radioitems(options=[], value=) ※複数選択不可

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options =[
            {'label':'佐藤','value':'sato'},
            {'label':'鈴木','value':'suzuki'},
            {'label':'田中','value':'tanaka'},
        ],
        value = 'suzuki',
    ),

    html.Label('Multi-select Dropdown'),
    dcc.Dropdown(
        options =[
            {'label':'東京','value':'tokyo'},
            {'label':'長野','value':'nagano'},
            {'label':'山形','value':'yamagata'},
            {'label':'埼玉','value':'saitama'},
            {'label':'北海道','value':'hokkaido'},
            {'label':'沖縄','value':'okinawa'},
        ],
        value = ['hokkaido','tokyo','okinawa'],
        multi=True
    ),

    html.Label('Radio-items'),
    dcc.RadioItems(
        options =[
            {'label':'東京','value':'tokyo'},
            {'label':'長野','value':'nagano'},
            {'label':'山形','value':'yamagata'},
            {'label':'埼玉','value':'saitama'},
            {'label':'北海道','value':'hokkaido'},
            {'label':'沖縄','value':'okinawa'},
        ],
        value = 'yamagata',
    ),
])



if __name__ == '__main__':
    app.run_server(debug=True)
