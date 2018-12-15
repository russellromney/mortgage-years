import numpy as np

header_text = """
## Should I pay off my mortgage early? 🏡

The decision to pay off your mortgage early can be tough -
this paying-your-mortgage-off-early calculator makes it 
easy to decide **whether** to pay off your mortgage early 
and, if so, **how early** to pay it off.

---
"""


def return_message(n_clicks,optimism,blind_faith,sleep_at_night,discipline,job_stability,risk_tolerance,years):
    # compute whether to pay off early
    if n_clicks==0:
        return ""
    quotient = sum([optimism,blind_faith,100-sleep_at_night,discipline,job_stability,np.sqrt(risk_tolerance*100)])/600
    print(quotient,"\n",np.sqrt(risk_tolerance*100))
    print(optimism,blind_faith,sleep_at_night,discipline,job_stability,risk_tolerance)
    if quotient > 0.8:
        return """
###### Good news! You don't need to worry about paying off 
your mortgage early. 

It sounds like you believe in a future of continued returns; 
you're not worried about your income;
and you don't mind risk or carrying a little debt to
leverage your returns. Congrats! Have a cheap glass
of boxed wine and keep doing what you're doing. 

*Technically this tool calculates that you should pay back your mortgage in about **{} years** -- but you're probably fine. Consider that number a fun thought experiement rather than a hard recommendation*

---
""".format(round(quotient*years,1))
    # compute how early to pay off
    elif quotient > 0.45:
        return """
###### You should think about paying off your mortgage a little earlier!

##### You should pay off your mortgage in about: **{} years**

Sounds like you're more cautious about debt, income stability, or continuing market returns. That's okay! Just make your risks smaller and reduce interest costs a bit by putting extra money toward your mortgage each month.

---
""".format(round(quotient*years,1))
    else:
        return """
###### You might want to consider renting instead of a mortgage! 

Mortages are long-term debt obligations that depend on a stable economic outlook, some risk tolerance, and income stability. You might not like the risk or debt obligation that comes with a mortgage. That's okay! 

If you were to get a mortgage despite that, you should pay it off as soon as you can -- in about **{}** years. 

---
""".format(round(quotient*years,1))