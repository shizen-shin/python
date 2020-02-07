import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

ext_css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=ext_css)

app.layout = html.Div([
    dcc.Input(id='input-div', value='initial value', type='text'),
    html.Div(id='output-div'),
])

@app.callback(
    Output(component_id='output-div', component_property='children'),
    [Input(component_id='input-div', component_property='value')],
)
def AAinput(CCC):
    return 'You entered {}'.format(CCC)

if __name__=='__main__':
    app.run_server(debug=True)
