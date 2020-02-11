import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H1(
        children='Stock price scrayping app',
        style = {
            'textAlign':'center',
            'fontSize':'1.8em',
            'margin':'2em 0 1em 0'
            }
        ),

    html.Div(
        children='''
        -------------------------------------------------------------
    ''',
            style = {
            'textAlign':'center'
            }
    ),
    html.Label('取得する過去データの日数',
        style = {'textAlign':'center'}
        ),

    dcc.Dropdown(
        options =[
            {'label':'20日分','value':'20'},
            {'label':'2ヶ月分','value':'60'},
            {'label':'6ヶ月分','value':'180'},
            {'label':'1年分','value':'400'},
            {'label':'2年分','value':'800'},
            {'label':'3年分','value':'1200'}
        ],
        value = '400',
        style = {'maxWidth':'40%',
                'margin':'0 auto'        
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)