import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

# Load data
df = pd.read_csv("dataset_sales.csv")

# Start the app
app = dash.Dash(__name__)
server = app.server  # If you want to deploy it later (optional)

# App layout
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '20px'}, children=[
    
    html.H1("Adidas Campaign Dashboard", style={'textAlign': 'center', 'color': '#333333', 'margin-bottom': '30px'}),

    html.Div([
        html.Div([
            html.Label("Select Channel:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='channel-dropdown',
                options=[{'label': channel, 'value': channel} for channel in sorted(df['Channel'].unique())],
                value=None,
                placeholder="Select a Channel",
                multi=False
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div([
            html.Label("Select Promo Type:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='promo-dropdown',
                options=[{'label': promo, 'value': promo} for promo in sorted(df['Promo_Type'].unique())],
                value=None,
                placeholder="Select a Promo Type",
                multi=False
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'}),
    ], style={'display': 'flex', 'justify-content': 'center', 'marginBottom': '30px'}),

    html.Div(id='stats-output', style={
        'backgroundColor': 'white',
        'padding': '20px',
        'marginBottom': '30px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)',
        'textAlign': 'center',
        'fontSize': '20px',
        'color': '#333333'
    }),

    dcc.Graph(id='revenue-bar-chart', style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '30px'}),
    dcc.Graph(id='promo-pie-chart', style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '30px'}),
    dcc.Graph(id='cost-vs-revenue-line', style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px'}),
])

# Callback to update graphs and stats
@app.callback(
    [Output('stats-output', 'children'),
     Output('revenue-bar-chart', 'figure'),
     Output('promo-pie-chart', 'figure'),
     Output('cost-vs-revenue-line', 'figure')],
    [Input('channel-dropdown', 'value'),
     Input('promo-dropdown', 'value')]
)
def update_dashboard(selected_channel, selected_promo):
    # Filter
    filtered_df = df.copy()
    if selected_channel:
        filtered_df = filtered_df[filtered_df['Channel'] == selected_channel]
    if selected_promo:
        filtered_df = filtered_df[filtered_df['Promo_Type'] == selected_promo]

    # Stats
    stats_text = f"""
    📢 Impressions: {filtered_df['Impressions'].sum():,} | 
    🖱️ Clicks: {filtered_df['Clicks'].sum():,} | 
    🛒 Conversions: {filtered_df['Conversions'].sum():,} | 
    💰 Revenue: ${filtered_df['Revenue'].sum():,.2f}
    """

    # Graphs
    bar_fig = px.bar(filtered_df, x='Campaign_ID', y='Revenue', color='Channel', 
                     title="Revenue per Campaign", template="plotly_white")
    pie_fig = px.pie(filtered_df, names='Promo_Type', title="Promo Type Distribution", template="plotly_white")
    line_fig = px.line(filtered_df, x='Campaign_ID', y=['Cost', 'Revenue'], title="Cost vs Revenue", template="plotly_white")

    return stats_text, bar_fig, pie_fig, line_fig

# Run app
if __name__ == '__main__':
    app.run(debug=True)
