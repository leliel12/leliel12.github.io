# mymodule.py
import numpy as np

_private = "baz"

def f(arr):
    return np.asarray(arr) + 1

_hidden = ["np"]  # the hidden globals

# dir redefinition that ignores the hidden globals
def __dir__():
    print("hola")
    return [attr for attr in globals() if attr not in _hidden]