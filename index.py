from pyAlice.py_alice import PyAlice
import settings

def handler(event, context):
  return PyAlice(params_alice=event, settings=settings).get_params_for_alice()
