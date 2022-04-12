import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State


# Global variables
myheading1 = 'Predicting Home Sale Prices in Ames, Iowa'
image1 = 'ames_welcome.jpeg'
tabtitle = 'Ames Housing'
sourceurl = 'http://jse.amstat.org/v19n3/decock.pdf'
githublink = 'https://github.com/cahn1/501-linear-reg-ames-housing/tree/update1'


# app server config
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = tabtitle

# app component layout
app.layout = html.Div(
    children=[
        html.H1(myheading1),
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto'}, className='four columns'),
            html.Div([
                html.H3('Features of Home:'),
                html.Div(
                    children=[
                        html.Div('Year Built:', style={
                            'display':'inline-block'}),
                        dcc.Input(id='YearBuilt', value=2010, type='number',
                                  min=2006, max=2010, step=1, style={
                                'display': 'inline-block', 'height': 25}),
                    ], style={'width': '49%', 'display': 'inline-block'}),
                html.Div('Bathrooms:', style={
                    'display':'inline-block'}),
                dcc.Input(id='Bathrooms', value=2, type='number', min=1, max=5, step=1),
                html.Div('Bedrooms:'),
                dcc.Input(id='BedroomAbvGr', value=4, type='number', min=1, max=5, step=1),
                html.Div('Total Square Feet:'),
                dcc.Input(id='TotalSF', value=2000, type='number', min=100, max=5000, step=1),
                html.Div('Single Family Home:'),
                dcc.Input(id='SingleFam', value=0, type='number', min=0, max=1, step=1),
                html.Div('Large Neighborhood:'),
                dcc.Input(id='LargeNeighborhood', value=0, type='number', min=0, max=1, step=1),
                html.Div('Car Garage:'),
                dcc.Input(id='GarageCars', value=0, type='number', min=0, max=4, step=1),
                html.Div('When Remodeled (Years ago):'),
                dcc.Input(id='RecentYearModAdd', value=0, type='number', min=10, max=70, step=5),
            ], className='four columns'),
            html.Div([
                html.Button(
                    children='Submit', id='submit-val', n_clicks=0,
                    style={
                        'background-color': 'red',
                        'color': 'white',
                        'margin-left': '5px',
                        'verticalAlign': 'center',
                        'horizontalAlign': 'center'}
                ),
                html.H3('Predicted Home Value:'),
                html.Div(id='Results')
            ], className='four columns')
        ], className='twelve columns',),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H4('Regression Equation:'),
        html.Div('Predicted Price = (- $662.7K Baseline) + ($0.35K * Year Built) + ($8.1K * Bathrooms) + (- $4.9K * Bedrooms) + ($0.042K * Total Square Feet) + ($ 22.1K * Single Family Home) + (- $7.9K * Large Neighborhood) + (19.5K * Car Garage) + (- $0.5K * When Remodeled (Years ago)'),
        html.Br(),
        html.A('Google Spreadsheet', href='https://docs.google.com/spreadsheets/d/1q2ustRvY-GcmPO5NYudvsBEGNs5Na5p_8LMeS4oM35U/edit?usp=sharing'),
        html.Br(),
        html.A('Code on Github', href=githublink),
        html.Br(),
        html.A("Data Source", href=sourceurl),
    ]
)

# callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='YearBuilt', component_property='value'),
    State(component_id='Bathrooms', component_property='value'),
    State(component_id='BedroomAbvGr', component_property='value'),
    State(component_id='TotalSF', component_property='value'),
    State(component_id='SingleFam', component_property='value'),
    State(component_id='LargeNeighborhood', component_property='value')

)
def ames_lr_function(
    clicks, YearBuilt, Bathrooms, BedroomAbvGr, TotalSF, SingleFam,
    LargeNeighborhood, GarageCars, RecentYearModAdd):
    if clicks == 0:
        return "Please fill features.."
    else:
        y = [-662787.386 + 354.0397*YearBuilt + 
             8084.212*Bathrooms + 
             -4936.6207*BedroomAbvGr + 
             42.3296*TotalSF+ 
             22095.5417*SingleFam+ 
             -7951.5585*LargeNeighborhood + 
             19530.1413*GarageCars + 
             -506.7658*RecentYearModAdd]
        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y


# Initiate app
if __name__ == '__main__':
    app.run_server(debug=True)
