
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background':'white',
    'text':'black'
}

app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
        style = {
            'textAlign':'center',
            'color': colors['text'],
            'background-color':colors['background'],
        }
        ),

    html.Div(
        children='''
        Dash: A web application framework for Python.
    ''',
            style = {
            'textAlign':'center',
            'color': colors['text']
            }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [4, 5, 2, 10 ,6], 'type': 'bar', 'name': '今年'},
                {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 8, 9], 'type': 'bar', 'name': '昨年'},
            ],
            'layout': {
                'title': '人数 昨対比',
                'plot_bgcolor':colors['background'],
                'paper_bgcolor':colors['background'],
                'font':{
                    'color':colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
