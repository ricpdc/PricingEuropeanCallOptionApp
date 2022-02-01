from flask_wtf import FlaskForm
from wtforms import  SubmitField

class EvaluatePayoffForm(FlaskForm):

    submit = SubmitField('Compute Expected Payoff', render_kw={"onclick": "loading();"})
    

    