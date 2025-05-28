from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
app = Dash(__name__)
df = px.data.gapminder()
app.layout = html.Div([
    html.H1("Gapminder Data Dashboard"),
    dcc.Dropdown(
        id='continent-dropdown',
        options=[{'label': c, 'value': c} for c in df['continent'].unique()],
        value='Asia'
    ),
    dcc.Graph(id='scatter-plot')
])
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('continent-dropdown', 'value')
)
def update_chart(selected_continent):
    filtered_df = df[df['continent'] == selected_continent]
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp',
                     size='pop', color='country', hover_name='country',
                     log_x=True, size_max=60)
    return fig
if __name__ == '__main__':
    app.run(debug=True)
