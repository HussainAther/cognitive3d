import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Classroom Engagement Metrics"),
    dcc.Graph(id='engagement-chart')
])

if __name__ == '__main__':
    app.run_server(debug=True)

