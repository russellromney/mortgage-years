import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
from dash.dependencies import Input, Output, State

from return_message import return_message,header_text

stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

metas = [
    dict(name='viewport',content="width=device-width, initial-scale=1.0")
]

app = dash.Dash(
    __name__,
    external_stylesheets=stylesheet,
    meta_tags=metas
)

app.title="How many years to pay off my mortgage"
server = app.server

styledict_slidertitle=dict(paddingBottom="0px",textAlign='center',width="100vw",maxWidth="400px",margin='auto')
styledict_slider=dict(paddingTop="0px",paddingBottom='30px',textAlign='center',width="100vw",maxWidth="400px",margin='auto')
styledict_emoji=dict(display="none",padding='4px',textAlign='center')
slider_div_style=dict(display='block',padding='4px',textAlign='center',)
markdown_props=dict(
    style=dict(
        display='block',
        textAlign='left',
        width="100vw",
        maxWidth="500px",
        margin='auto'
    )
)
markdown_style=markdown_props['style']

marks_ = {
    1:dict(label="👎",style=dict(fontSize=20)),
    100:dict(label="👍",style=dict(fontSize=20))
}


# function to return the proper emoji based on the slider position
def slider_pic(num):
    return num

app.layout = html.Div([
    # header
    html.Div([
       dcc.Markdown(header_text)
    ],style=dict(
        display='block',
        textAlign='left',
        width="100vw",
        maxWidth="500px",
        margin='auto',
        paddingBottom="0px"
    )),
    
    # contains the input
    html.Div([
        # market optimism
        html.Div([
            dcc.Markdown(
                "I think market growth will continue.",
                containerProps=dict(style=styledict_slidertitle)
            ),
            html.Div([
                dcc.Slider(
                    id='optimism-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=85,
                    marks={
                        1:dict(label="📉",style=dict(fontSize=20)),
                        100:dict(label="📈",style=dict(fontSize=20))
                    },
                ),
            ],style=styledict_slider),
            html.Div(
                id='optimism-emoji',
                style=styledict_emoji
            )
        ]),
        # blind faith that the future will be good
        html.Div([
            dcc.Markdown(
                "I think the future will be pretty good.",
                containerProps=dict(style=styledict_slidertitle)
            ),
            html.Div([
                dcc.Slider(
                    id='blind-faith-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=85,
                    marks={
                        1:dict(label="😥",style=dict(fontSize=20)),
                        100:dict(label="😀",style=dict(fontSize=20))
                    }                                        
                ),
            ],style=styledict_slider),
            html.Div(
                id='blind-faith-emoji',
                style=styledict_emoji
            )
        ],),
        # how well you want to sleep at night
        html.Div([
            dcc.Markdown(
                "I sleep better knowing my mortgage is paid off.",
                containerProps=dict(style=styledict_slidertitle)
            ),
            html.Div([
                dcc.Slider(
                    id='sleep-at-night-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=20,
                    marks={
                        1:dict(label="💤",style=dict(fontSize=20)),
                        100:dict(label="💤💤💤💤💤💤",style=dict(fontSize=20))
                    }                    
                ),
            ],style=styledict_slider),
            html.Div(
                id='sleep-at-night-emoji',
                style=styledict_emoji
            )
        ],),
        # "waiting skills" (investing discipline)        
        html.Div([
            dcc.Markdown(
                "I invest rather than spend extra money.",
                containerProps=dict(style=styledict_slidertitle)
            ),
            html.Div([
                dcc.Slider(
                    id='discipline-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=60,
                    marks={
                        1:dict(label="💸",style=dict(fontSize=20)),
                        100:dict(label="💰",style=dict(fontSize=20))
                    }
                ),
            ],style=styledict_slider),
            html.Div(
                id='discipline-emoji',
                style=styledict_emoji
            )
        ],),
        # job loss risk
        html.Div([
            dcc.Markdown(
                "My job/income is stable.",
                containerProps=dict(style=styledict_slidertitle)
            ),
            html.Div([
                dcc.Slider(
                    id='job-stability-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=85,
                    marks={
                        1:dict(label="⁉️",style=dict(fontSize=20)),
                        100:dict(label="✅",style=dict(fontSize=20))
                    }
                ),
            ],style=styledict_slider),
            html.Div(
                id='job-stability-emoji',
                style=styledict_emoji
            )
        ],),
        # risk tolerance in investing (stocks vs "guaranteed return of housing")        
        html.Div([
            dcc.Markdown(
                "I'm comfortable with some financial risk.",
                containerProps=dict(style=styledict_slidertitle)
            ),
            html.Div([
                dcc.Slider(
                    id='risk-tolerance-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=85,
                    marks={
                        1:dict(label="🙀",style=dict(fontSize=20)),
                        100:dict(label="😼",style=dict(fontSize=20))
                    }
                ),
            ],style=styledict_slider),
            html.Div(
                id='risk-tolerance-emoji',
                style=styledict_emoji
            )
        ],),
        # of mortgage years
        html.Div([
            dcc.Markdown(
                "Mortgage years left: 📅",
                containerProps=dict(style=dict(display='inline-block'))
            ),
            dcc.Input(
                id="years-input",
                type='number',
                min=1,
                max=50,
                list='input-list',
                style=dict(width="100vw",maxWidth="200px",fontSize=25,display='inline-block')
            ),
            html.Datalist(
                id="input-list",
                children=[
                    html.Option(value=5),
                    html.Option(value=10),
                    html.Option(value=15),
                    html.Option(value=20),
                    html.Option(value=25),
                    html.Option(value=30),
                ],
            ),            
        ],style=styledict_slider),
    ],style=dict(margin='auto',paddingTop="0px")),

    # contains the output
    html.Div([
        html.Button(
            "Tell me if I should pay off my mortgage early! 💰",
            id='submit-button',
            style=dict(fontSize=20,backgroundColor="skyBlue",color="black",width="100vw",maxWidth="300px",whiteSpace='normal',lineHeight='normal',height="100%"),
            n_clicks=0
        ),
        dcc.Markdown(
            """Your results go here! 🙌""",
            id='output-markdown',
            containerProps=dict(
                style=dict(textAlign='center',paddingTop='25px',width="100vw",maxWidth="550px",margin='auto')
            )
        )
    ],style=dict(textAlign='center')),
    html.Div([
        dcc.Markdown(
"""
Made with ❤️ by [Russell](https://github.com/russellromney)

#inspired by an [article on Chris Reining's blog](https://chrisreining.com/should-i-pay-off-my-mortgage-early-or-invest) 💡 
""",
            containerProps=dict(style=dict(textAlign='center',paddingTop="10vw"))
        ),
    ],style=styledict_slider)
],style=dict(marginLeft='auto',marginRight='auto'))








# function to return output
@app.callback(
    Output("output-markdown",'children'),
    [Input("submit-button",'n_clicks')],
    [State("optimism-slider",'value'),
     State("blind-faith-slider",'value'),
     State("sleep-at-night-slider",'value'),
     State("discipline-slider",'value'),
     State("job-stability-slider",'value'),
     State("risk-tolerance-slider",'value'),
     State("years-input",'value')])
def return_markdown(n_clicks,optimism,blind_faith,sleep_at_night,discipline,job_stability,risk_tolerance,years):
    return return_message(n_clicks,optimism,blind_faith,sleep_at_night,discipline,job_stability,risk_tolerance,years)





if __name__ == '__main__':
    app.run_server(threaded=True,debug=False)