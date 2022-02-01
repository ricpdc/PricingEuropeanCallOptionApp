from flask_wtf import FlaskForm
from wtforms import  IntegerField, FloatField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ProblemDefinitionForm(FlaskForm):

    spot_price = FloatField('Spot Price', validators=[DataRequired()], default=2.0)
    volatility = FloatField('Volatility', validators=[DataRequired()], default=0.4)
    anual_rate = FloatField('Anual Rate', validators=[DataRequired()], default=0.05)
    maturity_days = IntegerField('Days to Maturity', validators=[DataRequired()], default=40)
    submit = SubmitField('Define')
    

    