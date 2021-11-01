import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

from Boid import Boid


TIME_INTERVAL = 10


def main():
    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.H1("Boids"),
        html.Div([
            html.Div(id="show_time_component"),
            dcc.Interval(
                id="interval_component",
                interval=TIME_INTERVAL,
                n_intervals=0
            )
        ]),
        dcc.Graph(id="graph")
    ])
    
    @app.callback(
        Output("show_time_component", "children"),
        Output("graph", "figure"),
        Input("interval_component", "n_intervals")
    )
    def update_figure(time):
        fig = go.Figure(data=go.Cone(x=[1], y=[1], z=[1], u=[1], v=[1], w=[0]))
        return [html.H4("Time: "+str((time*TIME_INTERVAL)/1000))], fig

    app.run_server(debug=True)
        





if __name__=="__main__":
    main()