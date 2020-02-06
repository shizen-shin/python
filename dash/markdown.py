
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#markdownで記述する場合、dcc.Markdown()。dcc.Graph()ではない。
#シングルクオテーション３つで、改行も記述できる
app.layout = html.Div([
    dcc.Markdown('''

    # 見出し1
    ## 見出し２
    ### シャープ３つ
    #### シャープ４つ
    ##### h５タグ
    #######　　半角スペース１個だけ。それ以外はただの文字列になる

    - 箇条書き
    - 「-」＝「◯」
    - 箇条書き２
    - 箇条書き３
        - 箇条書き２
        - 箇条書き４
            - 箇条書き５
        - 箇条書き６
            - 箇条書き７
    - 箇条書き８

    1. 番号付き１
    1. 番号付き２
    1. 番号付き３
        1. 番号付き４
        1. 番号付き５
            1. 番号付き６
            1. 番号付き７
            1. 番号付き８
    1. 番号付き９
        1. 番号付き１０


    
    ''')
])



if __name__ == '__main__':
    app.run_server(debug=True)
