from flask_wtf import FlaskForm
from wtforms import  DecimalRangeField, IntegerField, FloatField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class PricingParametersForm(FlaskForm):

    strike_price  = DecimalRangeField('Strike price', validators=[NumberRange(min=1.208, max=2.813)], default=1.896)
    c_approx  = DecimalRangeField('Approximation scaling for the payoff', validators=[NumberRange(min=0, max=1)], default=0.25)
    
    submit = SubmitField('Set')
    

    