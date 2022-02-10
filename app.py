import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
 
USERNAME_PASSWORD_PAIRS = [
    ['nethu', '12345'],['guvi', 'guvi']
]
 
app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server
 
app.layout = html.Div([
    dcc.RangeSlider(
        id='range-slider',
        min=-5,
        max=6,
        marks={i:str(i) for i in range(-5, 7)},
        value=[-3, 4]
    ),
    html.H1(id='product')  # this is the output
], style={'width':'50%'})
 
@app.callback(
    Output('product', 'children'),
    [Input('range-slider', 'value')])
def update_value(value_list):
    return value_list[0]*value_list[1]
 from dash import Dash, dcc, html, Input, Output
 
#app = Dash(__name__)
app = JupyterDash(__name__)
app.layout = html.Div([
   html.H6("Change the value in the text box to see callbacks in action!"),
   html.Div([
       "Input: ",
       dcc.Input(id='my-input', value='initial value', type='text')
   ]),
   html.Br(),
   html.Div(id='my-output'),
 
])
 
 
@app.callback(
   Output(component_id='my-output', component_property='children'),
   Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
   return f'Output: {input_value}'
 
 

 
if __name__ == '__main__':
    app.run_server(debug=True)
