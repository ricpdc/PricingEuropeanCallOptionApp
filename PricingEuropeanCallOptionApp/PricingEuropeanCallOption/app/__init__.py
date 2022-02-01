import os
from flask import Flask
from config import Config

template_dir = os.path.abspath('./presentation/templates')

app = Flask(__name__, template_folder=template_dir, static_folder='D:\\OneDrive - Universidad de Castilla-La Mancha\\Universidad\\Quantum\\UML Profile\\ejemplo\\ws\\PricingEuropeanCallOptionApp\\PricingEuropeanCallOption\\static')


app.config.from_object(Config)

from app import routes