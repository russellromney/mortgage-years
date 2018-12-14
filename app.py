import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
from dash.dependencies import Input, Output, State

stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(
    __name__,
    external_stylesheets=stylesheet
)
#app.config['suppress_callback_exceptions']=True
server = app.server

styledict_slidertitle=dict(display='inline-block',padding='4px',textAlign='right',width="60%")
styledict_slider=dict(display='inline-block',padding='2px',textAlign='center',width="35%")
styledict_emoji=dict(display='inline-block',padding='2px',textAlign='center',width="0%")
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
       dcc.Markdown(
"""
## Should I pay off my mortgage early? 🏡

The decision to pay off your mortgage early can be tough --
it depends on many factors and there are many risks, 
probabilities, and factors to consider.

This calculator makes it easy to decide
**Whether** to pay off your mortgage early and, if so, **how early** to pay it off.

Inspired by an [article on Chris Reining's blog](https://chrisreining.com/should-i-pay-off-my-mortgage-early-or-invest). 
""",
            containerProps=dict(
                style=dict()
            )
        )
    ],style=dict(display='block',textAlign='left',width='90%',marginLeft='auto',marginRight='auto')),
    # contains the input
    html.Div([
        # market optimism
        html.Div([
            html.H6(
                "I think market growth will continue.",
                style=styledict_slidertitle
            ),
            html.Div([
                dcc.Slider(
                    id='optimism-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=80,
                    marks=marks_
                ),
            ],style=styledict_slider),
            html.Div(
                id='optimism-emoji',
                style=styledict_emoji
            )
        ]),
        # blind faith that the future will be good
        html.Div([
            html.H6(
                "I think the future will be pretty good.",
                style=styledict_slidertitle
            ),
            html.Div([
                dcc.Slider(
                    id='blind-faith-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=80,
                    marks=marks_
                ),
            ],style=styledict_slider),
            html.Div(
                id='blind-faith-emoji',
                style=styledict_emoji
            )
        ]),
        # how well you want to sleep at night
        html.Div([
            html.H6(
                "Does carrying debt make you uncomfortable?",
                style=styledict_slidertitle
            ),
            html.Div([
                dcc.Slider(
                    id='sleep-at-night-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=20,
                    marks=marks_
                ),
            ],style=styledict_slider),
            html.Div(
                id='sleep-at-night-emoji',
                style=styledict_emoji
            )
        ]),
        # "waiting skills" (investing discipline)        
        html.Div([
            html.H6(
                "Do you invest rather than spend extra money?",
                style=styledict_slidertitle
            ),
            html.Div([
                dcc.Slider(
                    id='discipline-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=60,
                    marks=marks_
                ),
            ],style=styledict_slider),
            html.Div(
                id='discipline-emoji',
                style=styledict_emoji
            )
        ]),
        # job loss risk
        html.Div([
            html.H6(
                "How stable will your job/income be?",
                style=styledict_slidertitle
            ),
            html.Div([
                dcc.Slider(
                    id='job-stability-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=80,
                    marks=marks_
                ),
            ],style=styledict_slider),
            html.Div(
                id='job-stability-emoji',
                style=styledict_emoji
            )
        ]),
        # risk tolerance in investing (stocks vs "guaranteed return of housing")        
        html.Div([
            html.H6(
                "How comfortable are you with risk?",
                style=styledict_slidertitle
            ),
            html.Div([
                dcc.Slider(
                    id='risk-tolerance-slider',
                    min=0,
                    max=100,
                    step=4,
                    value=80,
                    marks=marks_
                ),
            ],style=styledict_slider),
            html.Div(
                id='risk-tolerance-emoji',
                style=styledict_emoji
            )
        ]),
        # of mortgage years
        html.Div([
            html.H6(
                "How many years is your mortgage?",
                style=styledict_slidertitle
            ),
            dcc.Input(
                id="years-input",
                style=dict(fontSize=25,display='inline-block'),
                type='number',
                min=1,
                max=100,
            ),
        ]),
    ],style=dict(textAlign='center',marginLeft='auto',marginRight='auto')),

    # contains the output
    html.Div([
        html.Button(
            "Tell me how quickly to pay off my mortgage! 💰",
            id='submit-button',
            style=dict(fontSize=20,backgroundColor="skyBlue",color="black"),
            n_clicks=0
        ),
        dcc.Markdown(
            id='output-markdown',
            containerProps=dict(
                style=dict(fontSize='20',textAlign='center')
            )
        )
    ],style=dict(textAlign='center')),
    html.Div(
        [dcc.Markdown("""Made with ❤️ by [Russell](https://github.com/russellromney)""",
        containerProps=dict(style=dict(textAlign='center')))],
        style=dict(height="500px")
        )
],style=dict(width="90%"))








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
     State("years-input",'value')]
)
def return_decision(n_clicks,optimism,blind_faith,sleep_at_night,discipline,job_stability,risk_tolerance,years):
    # compute whether to pay off early
    if n_clicks==0:
        return ""
    quotient = sum([optimism,blind_faith,100-sleep_at_night,discipline,job_stability,np.sqrt(risk_tolerance*100)])/600
    print(quotient,"\n",np.sqrt(risk_tolerance*100))
    print(optimism,blind_faith,sleep_at_night,discipline,job_stability,risk_tolerance)
    if quotient > 0.8:
        return """
###### Good news! You don't need to worry about paying off your mortgage early. 

It sounds like you believe in a future of continued returns, you're not worried about your income, and you don't mind risk or carrying a little debt to leverage your returns. Congrats! Have a cheap glass of boxed wine and keep doing what you're doing. 

(Technically this tool calculates that you should pay back your mortgage in about **{} years** -- but you're probably fine. Consider that number a fun thought experiement rather than a hard recommendation)
""".format(round(quotient*years,1))
    # compute how early to pay off
    elif quotient > 0.3:
        return """
###### You should think about paying off your mortgage a little earlier!

##### I should pay off my mortgage in about: **{} years**

Sounds like you're a little more cautious about debt, income stability, or continuing market returns. That's okay! Just make your risks a little smaller and reduce interest costs a little bit by putting a little extra money toward your mortgage each month.
""".format(round(quotient*years,1))
    else:
        return """
###### You might want to consider renting instead of a mortgage! 

Mortages are long-term debt obligations that depend on a stable economic outlook, some risk tolerance, and income stability. You might not like the risk or debt obligation that comes with a mortgage. That's okay! 

If you were to get a mortgage despite that, you should pay it off as soon as you can -- in about **{}** years. 
""".format(round(quotient*years,1))





if __name__ == '__main__':
    app.run_server(threaded=True,debug=False)