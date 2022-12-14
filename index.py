import dash
import dash.dcc as dcc
import dash.html as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from app import app, server
import callbacks

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("About", href="/about", id="page-1-link"),
                dbc.NavLink("Portfolio", href="/portfolio", id="page-2-link"),
                dbc.NavLink("Random", href="/random", id="page-3-link")
            ],
            brand="Christopher Han",
            brand_href = '/about',
            color="dark",
            dark=True
        ),
        dbc.Container(id="page-content", className="pt-4",
        style= {'padding-bottom':'70px'}),
        dbc.NavbarSimple(
            brand= 'GitHub Repo',
            brand_style = {'font-size': '15px'},
            brand_href= 'https://github.com/Christopher-Changhee-Han/personalportfolio',
            fixed = 'bottom',
            color="dark",
            dark=True,
            style={'width':'100vw'}
        )
    ], style={'width':'100vw'}
)

if __name__ == '__main__':
    app.run_server(debug = True)