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
    html.Label('取得する過去データ数',
        style = {'textAlign':'center'}
        ),

    dcc.Dropdown(
        options =[
            {'label':'20(約20日分)','value':'20'},
            {'label':'60(約2ヶ月分)','value':'60'},
            {'label':'180(約6ヶ月分)','value':'180'},
            {'label':'400(約1年分)','value':'400'},
            {'label':'800(約2年分)','value':'800'},
            {'label':'1200(約3年分)','value':'1200'}
        ],
        value = '400',
        style = {'maxWidth':'50%',
                'margin':'0 auto'        
        }
    ),
    html.Div(children=[
        html.Button('10秒以内に選択してください',
            type = 'button',
            id = 'confirm',
            style = {'backgroundColor':'darkgray',
                    'color':'white',
                    'fontSize':'1.0em',
                    # 'font-weight':'bold',
                    'borderStyle':'none',
                    'margin':'30px auto'
                }            
        )
    ],style = {'textAlign':'center'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)