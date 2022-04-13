import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State


# Global variables
myheading1 = 'Predicting Home Sale Prices in Ames, Iowa'
image1 = 'ames_welcome.jpeg'
image2 = 'cancer_heatmap1.jpg'
image3 = 'cancer_predict_true_compare.png'
tabtitle = 'Ames Housing'
sourceurl = 'http://jse.amstat.org/v19n3/decock.pdf'
githublink = 'https://github.com/cahn1/501-linear-reg-ames-housing/tree/update1'

# app server config
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = tabtitle

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.H1('Linear regression analysis', style={
        'textAlign': 'center', 'margin': '48px 0', 'fontFamily': 'system-ui'}),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Predicting Home Sale Prices in Ames, Iowa',
        children=[
            #html.H3(myheading1),
            html.Div([
                html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto'}, className='four columns'),
                html.Div([
                    html.H3('Features of Home:'),
                    html.Div(
                        children=[
                            html.Div('Year Built:', style={
                                'display':'inline-block', 'padding': 5, 'flex': 1}),
                            dcc.Input(id='YearBuilt', value=2010, type='number',
                                    min=2006, max=2010, step=1, style={
                                    'display': 'inline-block', 'height': 26,}),
                        ], style={'width': '49%', 'display': 'inline-block'}),
                    html.Br(),html.Br(),
                    html.Div(
                        children=[
                            html.Div('Bathrooms:', style={
                                'display':'inline-block'}),
                            # dcc.Input(id='Bathrooms', value=2, type='number',
                            #           min=1, max=5, step=1, style={
                            #         'display': 'inline-block', 'height': 26}),
                            dcc.Slider(id='Bathrooms', min=1, max=5, 
                                    marks={i: f' {i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                            
                            html.Div('Bedrooms:', style={'display':'inline-block'}),
                            # dcc.Input(id='BedroomAbvGr1', value=4, type='number', min=1, max=5, step=1, style={
                            #         'display': 'inline-block', 'height': 26}),
                            dcc.Slider(id='BedroomAbvGr', min=1, max=5, 
                                    marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                        ], style={'width': '70%', 'display': 'inline-block'}),
                    #html.Div('Bedrooms:', style={'display':'inline-block'}),
                    html.Br(),html.Br(),
                    html.Div(
                        children=[
                            html.Div('Total Square Feet:', style={
                                'display':'inline-block', 'padding': 5, 'flex': 1}),
                            dcc.Input(id='TotalSF', value=2000, type='number',
                                    min=100, max=5000, step=1, style={
                                    'display': 'inline-block', 'height': 26}),
                        ], style={'width': '70%', 'display': 'inline-block'}),
                    html.Br(),html.Br(),
                    dcc.Checklist(id='SingleFam', options=[{'label': 'Single Family Home', 'value': 1}], value=[],),
                    dcc.Checklist(id='LargeNeighborhood', options=[{'label': 'Large Neighborhood', 'value': 1}], value=[],),
                    html.Br(),html.Br(),
                    html.Div(
                        children=[
                            html.Div('Car Garage:', style={
                                'display':'inline-block'}),
                            # dcc.Input(id='Bathrooms', value=2, type='number',
                            #           min=1, max=5, step=1, style={
                            #         'display': 'inline-block', 'height': 26}),
                            dcc.Slider(id='GarageCars', min=0, max=4, 
                                    marks={i: f' {i}' if i == 1 else str(i) for i in range(0, 5)}, value=0,),
                            
                            html.Div('When Remodeled (Years ago):', style={
                                'display':'inline-block', 'padding': 5, 'flex': 1}),
                            dcc.Input(id='RecentYearModAdd', value=0, type='number',
                                    min=0, max=70, step=1, style={
                                    'display': 'inline-block', 'height': 26}),
                        ], style={'width': '70%', 'display': 'inline-block'}),
                    # html.Div('Car Garage:'),
                    # dcc.Input(id='GarageCars', value=0, type='number', min=0, max=4, step=1),
                    # html.Div('Total Square Feet:'),
                    # dcc.Input(id='TotalSF', value=2000, type='number', min=100, max=5000, step=1),
                    # html.Div('When Remodeled (Years ago):'),
                    # dcc.Input(id='RecentYearModAdd', value=0, type='number', min=0, max=70, step=1),
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
            html.Div('Predicted Price = (- $662.7K Baseline) + ($0.35K * Year Built) + ($8.1K * Bathrooms) + (- $4.9K * Bedrooms) + ($0.042K * Total Square Feet) + ($ 22.1K * Single Family Home) + (- $7.9K * Large Neighborhood) + (19.5K * Car Garage) + (- $0.5K * When Remodeled (Years ago))'),
            html.Br(),
            html.A('Google Spreadsheet', href='https://docs.google.com/spreadsheets/d/1q2ustRvY-GcmPO5NYudvsBEGNs5Na5p_8LMeS4oM35U/edit?usp=sharing'),
            html.Br(),
            html.A('Code on Github', href=githublink),
            html.Br(),
            html.A("Data Source", href=sourceurl),
        ]),
        dcc.Tab(label='Cancer prediction',
            children=[
                html.Div([
                    html.Img(
                        src=app.get_asset_url(image2),
                        style={'width': '30%', 'height': 'auto'},
                        className='four columns'),
                    html.Img(
                        src=app.get_asset_url(image3),
                        style={'width': '30%', 'height': 'auto'},
                        className='four columns'),
                    html.Div([
                        html.H3('Features:'),
                        html.Div(
                            children=[
                                html.Div('PctBachDeg25_Over:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctBachDeg25_Over', min=1, max=5,
                                           marks={i: f' {i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),

                                html.Div('incidenceRate:', style={'display':'inline-block'}),
                                dcc.Slider(id='incidenceRate', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctPublicCoverageAlone:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctPublicCoverageAlone', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('povertyPercent:', style={'display':'inline-block'}),
                                dcc.Slider(id='povertyPercent', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('medIncome:', style={'display':'inline-block'}),
                                dcc.Slider(id='medIncome', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctHS25_Over:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctHS25_Over', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctPublicCoverage:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctPublicCoverage', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctPrivateCoverage:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctPrivateCoverage', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctUnemployed16_Over:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctUnemployed16_Over', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctMarriedHouseholds:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctMarriedHouseholds', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctBachDeg18_24:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctBachDeg18_24', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctEmpPrivCoverage:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctEmpPrivCoverage', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PercentMarried:', style={'display':'inline-block'}),
                                dcc.Slider(id='PercentMarried', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctHS18_24:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctHS18_24', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                                html.Div('PctBlack:', style={'display':'inline-block'}),
                                dcc.Slider(id='PctBlack', min=1, max=5,
                                           marks={i: f'{i}' if i == 1 else str(i) for i in range(1, 6)}, value=2,),
                            ], style={'width': '70%', 'display': 'inline-block'}),
                        # html.Br(),html.Br(),
                        # html.Div(
                        #     children=[
                        #         html.Div('Car Garage:', style={
                        #             'display':'inline-block'}),
                        #         # dcc.Input(id='Bathrooms', value=2, type='number',
                        #         #           min=1, max=5, step=1, style={
                        #         #         'display': 'inline-block', 'height': 26}),
                        #         dcc.Slider(id='GarageCars', min=0, max=4,
                        #                    marks={i: f' {i}' if i == 1 else str(i) for i in range(0, 5)}, value=0,),
                        #     ], style={'width': '70%', 'display': 'inline-block'}),
                    ], className='four columns'),
                    html.Div([
                        html.Button(
                            children='Submit', id='submit-val1', n_clicks=0,
                            style={
                                'background-color': 'red',
                                'color': 'white',
                                'margin-left': '5px',
                                'verticalAlign': 'center',
                                'horizontalAlign': 'center'}
                        ),
                        html.H3('Predicted Cancer Death Rate:'),
                        html.Div(id='cancer_output')
                    ], className='four columns')
                ], className='twelve columns',),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H4('Regression Equation:'),
                html.Div('Predicted Death Rate = 102.7807 + (-1.0272*PctBachDeg25_Over) + (0.207*incidenceRate) + (-0.0655*PctPublicCoverageAlone) + (0.6177*povertyPercent) + (0.0001*medIncome) + (0.6255*PctHS25_Over) + (-0.0824*PctPublicCoverage) + (-0.6517*PctPrivateCoverage) + (0.3433*PctUnemployed16_Over) + (-0.9779*PctMarriedHouseholds) + (-0.1667*PctBachDeg18_24) + (0.4668*PctEmpPrivCoverage) + (0.5182*PercentMarried) + (0.277*PctHS18_24) + (-0.0209*PctBlack)'),
                html.Br(),
                html.A('Code on Github', href=githublink),
                html.Br(),
                html.A("Data Source", href=sourceurl),
            ]),
    ],
    style={
        'fontFamily': 'system-ui'
    },
    content_style={
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'padding': '44px'
    },
    parent_style={
        'maxWidth': '1400px',
        'margin': '0 auto'
    })
])


# callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='YearBuilt', component_property='value'),
    State(component_id='Bathrooms', component_property='value'),
    State(component_id='BedroomAbvGr', component_property='value'),
    State(component_id='TotalSF', component_property='value'),
    State(component_id='SingleFam', component_property='value'),
    State(component_id='LargeNeighborhood', component_property='value'),
    State(component_id='GarageCars', component_property='value'),
    State(component_id='RecentYearModAdd', component_property='value'))
def ames_lr_function(
    clicks, YearBuilt, Bathrooms, BedroomAbvGr, TotalSF, SingleFam,
    LargeNeighborhood, GarageCars, RecentYearModAdd):
    if clicks == 0:
        return "Please fill features.."
    else:
        print(f'SingleFam: {SingleFam}')
        y = [-662787.386 + 354.0397*YearBuilt + 
             8084.212*Bathrooms + 
             -4936.6207*BedroomAbvGr + 
             42.3296*TotalSF+ 
             22095.5417*(0 if SingleFam == [] else 1) +
             -7951.5585*(0 if LargeNeighborhood == [] else 1) +
             19530.1413*GarageCars + 
             -506.7658*RecentYearModAdd]
        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y

# callback
@app.callback(
    Output(component_id='cancer_output', component_property='children'),
    Input(component_id='submit-val1', component_property='n_clicks'),
    State(component_id='PctBachDeg25_Over', component_property='value'),
    State(component_id='incidenceRate', component_property='value'),
    State(component_id='PctPublicCoverageAlone', component_property='value'),
    State(component_id='povertyPercent', component_property='value'),
    State(component_id='medIncome', component_property='value'),
    State(component_id='PctHS25_Over', component_property='value'),
    State(component_id='PctPublicCoverage', component_property='value'),
    State(component_id='PctPrivateCoverage', component_property='value'),
    State(component_id='PctUnemployed16_Over', component_property='value'),
    State(component_id='PctMarriedHouseholds', component_property='value'),
    State(component_id='PctBachDeg18_24', component_property='value'),
    State(component_id='PctEmpPrivCoverage', component_property='value'),
    State(component_id='PercentMarried', component_property='value'),
    State(component_id='PctHS18_24', component_property='value'),
    State(component_id='PctBlack', component_property='value'))
def cancer_lr_function(
        clicks, PctBachDeg25_Over, incidenceRate, PctPublicCoverageAlone,
        povertyPercent, medIncome, PctHS25_Over, PctPublicCoverage,
        PctPrivateCoverage, PctUnemployed16_Over, PctMarriedHouseholds,
        PctBachDeg18_24, PctEmpPrivCoverage, PercentMarried, PctHS18_24,
        PctBlack):
    if clicks == 0:
        return "Please fill features.."
    else:
        y = [102.7807 +
             -1.0272*PctBachDeg25_Over +
             0.207*incidenceRate +
             -0.0655*PctPublicCoverageAlone +
             0.6177*povertyPercent +
             0.0001*medIncome +
             0.6255*PctHS25_Over +
             -0.0824*PctPublicCoverage +
             -0.6517*PctPrivateCoverage +
             0.3433*PctUnemployed16_Over +
             -0.9779*PctMarriedHouseholds +
             -0.1667*PctBachDeg18_24 +
             0.4668*PctEmpPrivCoverage +
             0.5182*PercentMarried +
             0.277*PctHS18_24 +
             -0.0209*PctBlack]
        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y

if __name__ == '__main__':
    app.run_server(debug=True)
