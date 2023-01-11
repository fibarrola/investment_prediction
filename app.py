from dash import Dash, dcc, html, Input, Output
from src.fig_functions import money_graph
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div([
        "Dinero inicial: u$d ",
        dcc.Input(id='initial_money', value=19000, type='number')
    ]),

    html.Div([
        "Interés: % ",
        dcc.Input(id='interest_rate', value=20, type='number')
    ]),

    html.Div([
        "Tiempo de retorno (meses) : ",
        dcc.Input(id='return_time', value=36, type='number')
    ]),

    html.Div([
        "Inversión mensual: u$d ",
        dcc.Input(id='monthly_inv', value=200, type='number')
    ]),

    html.Br(),
    html.Div(id='my-output'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='initial_money', component_property='value'),
    Input(component_id='interest_rate', component_property='value'),
    Input(component_id='return_time', component_property='value'),
    Input(component_id='monthly_inv', component_property='value')
)
def update_graph(input_value, interest_rate, return_time, monthly_inv):
    return money_graph(input_value, interest_rate, return_time, monthly_inv)

# @app.callback(
#     Output(component_id='example-graph', component_property='figure'),
#     Input(component_id='interest_rate', component_property='value')
# )
# def update_graph(input_value):
#     return money_graph(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)