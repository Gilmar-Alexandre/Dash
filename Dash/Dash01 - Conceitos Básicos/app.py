import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Carros":['Gol', 'Onix', 'Pajero', 'Sandero', 'Corolla'],
    "Preço":[20, 30, 45, 18, 45],
    "Cidades": ['Belo Horizonte', 'Betim', 'Betim', 'Contagem','Contagem']
})

fig = px.bar(df, x="Carros",y="Preço", color="Cidades")

# ===================================================================
# Layout

app.layout = html.Div(id="div1",
    children=[
        html.H1("Dash Carros", id="h1"),
        html.Div("Comparativo de Carros"), 

        dcc.Graph(figure=fig, id="graph")
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)

