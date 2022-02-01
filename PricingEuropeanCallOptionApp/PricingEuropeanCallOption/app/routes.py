from flask import render_template, flash, redirect
from app import app
from presentation.LoginForm import LoginForm
from presentation.ProblemDefinitionForm import ProblemDefinitionForm
from presentation.PricingParametersForm import PricingParametersForm
from presentation.EvaluatePayoffForm import EvaluatePayoffForm

from businesslogic.controllers.EuropeanCallController import EuropeanCallController
from classicalquantumlogic.EuropeanCallDriver import EuropeanCallDriver
from classicalquantumlogic.EuropeanCallEstimation import EuropeanCallEstimation

# ...


europeanCallController = EuropeanCallController()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Pricing European Call Options')


@app.route('/problem_definition', methods=['GET', 'POST'])
def problemDefinition():
    form = ProblemDefinitionForm()
    message = None
    if form.validate_on_submit():
        europeanCallController.createProblem(form.spot_price.data, form.volatility.data, form.anual_rate.data, form.maturity_days.data)
        message = 'European Call Options Defined: {}'.format(europeanCallController.getProblem().getParams())
    return render_template('problem_definition.html', title="Problem Definition", form=form, message=message, europeanCallController=europeanCallController)

@app.route('/pricing_parameters', methods=['GET', 'POST'])
def objectiveDefinition():
    form = PricingParametersForm()
    
    if europeanCallController.getProblem() is not None:
        form.strike_price.validators[0].min=europeanCallController.getProblem().low;
        form.strike_price.validators[0].max=europeanCallController.getProblem().high;
    
    problemPlot=europeanCallController.getProblemPlot()
    objectivePlot=None
    expected_value=None
    expected_delta=None
    
    if form.validate_on_submit():
        europeanCallController.createObjectiveFunction(form.strike_price.data, form.c_approx.data)
        objectivePlot=europeanCallController.getObjectivePlot()
        expected_value = "Exact expected value:\t%.4f" % europeanCallController.getExactExpectedValue()
        expected_delta = "\nExact delta value:   \t%.4f" % europeanCallController.getExactDeltaValue()
    return render_template('pricing_parameters.html', title="Pricing Parameters", form=form, problemPlot=problemPlot, objectivePlot=objectivePlot, expected_value=expected_value, expected_delta=expected_delta, europeanCallController=europeanCallController)



@app.route('/evaluate_payoff', methods=['GET', 'POST'])
def evaluatePayoff():
    form = EvaluatePayoffForm()

    expected_value = "Exact expected value:\t%.4f" % europeanCallController.getExactExpectedValue()    
    estimatedValue=None
    confidenceInterval = None

    europeanCallDriver = EuropeanCallDriver(europeanCallController.getProblem(), europeanCallController.getObjective())
    circuit=europeanCallDriver.getQAEAlgorithm().getCircuitImage()

    if form.validate_on_submit():
        estimationResult = europeanCallDriver.estimateEuropeanCall()
        
        estimatedValue = "Estimated value:    \t%.4f" % estimationResult.getEstimatedValue()
        confidenceInterval = "Confidence interval:\t[%.4f, %.4f]" % estimationResult.getConfidenceInterval()
        
    return render_template('evaluate_payoff.html', title="Evaluate Expected Payoff", form=form, expected_value=expected_value, estimated_value=estimatedValue, confidence_interval=confidenceInterval, circuit=circuit, europeanCallController=europeanCallController);





# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect('/index')
#     return render_template('login.html', title='Sign In', form=form)






