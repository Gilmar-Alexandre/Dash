from dash import html, dcc
import dash_bootstrap_components as dbc
import dash

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app import *
# pip install dash-auth
import dash_auth


from dash_bootstrap_templates import load_figure_template
load_figure_template(["quartz"])

# ================= Layout =================== #
app.layout = dbc.Container(children=[
                dbc.Row([
                    dbc.col([

                    ]),
                ])

                ],fluid=True)


if __name__ == "__main__":
    app.run_server(port=8051, debug=True)