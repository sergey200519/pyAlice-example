from pyAlice.simulation import Simulation
from pyAlice.py_alice import PyAlice

import settings

def handler(event, context=None):
    py = PyAlice(params_alice=event, settings=settings)
    return py.get_params_for_alice("dict")

Simulation(handler=handler)