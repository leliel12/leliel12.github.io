---
layout: post
title: "Improving Jupyter Autocompletion for Cleaner Interfaces in Scientific Computing"
categories: software, python, decorators
---

In my day-to-day work, I specialize in creating tools for scientific computing, most of which are executed within Jupyter notebooks. One common challenge for new users is grappling with the intricacies of autocompletion, particularly understanding what is essential for effective use. This issue becomes apparent when utilizing autocompletion in scenarios like the following Python code:

```python
# mymodule.py

import numpy as np

_private = "baz"

def f(arr):
    return np.asarray(arr) + 1
```

Upon using Jupyter's autocompletion, the result includes not only `f(arr)` but also `np`, which is merely a necessary import but not part of my intended "API." These are what I refer to as 'public but private imports,' and they can be bothersome. Concrete examples of this phenomenon can be observed in modules like `sklearn.pipeline` or `inspect`.

One workaround is to assign private aliases to each import, like so:

```python
# mymodule.py

import numpy as _np

_private = "baz"

def f(arr):
    return _np.asarray(arr) + 1
```

However, with each change of this nature, one must manually search for all instances within functions like `f()` where these private aliases are used.

Other alternatives include having a private module `_module` and a public one `module` (similar to what `pandas.testing` does) or organizing everything within a package and having `__init__.py` expose only what is necessary, as demonstrated by `sklearn.ensemble`.

The last alternative involves redefining the `__dir__` function of the module. This function determines the list of attributes visible during autocompletion on most platforms. Here's an example:

```python
import numpy as np

_private = "baz"

def f(arr):
    return np.asarray(arr) + 1

_hidden = ["np"]  # the hidden globals

# dir redefinition that ignores the hidden globals
def __dir__():
    return [attr for attr in globals() if attr not in _hidden]
```

This last option has the advantage of not requiring alterations to the source code where hidden attributes are used. However, developers can still access these attributes if they attempt to do so.

### Exploring an Enhanced Example

The only drawback to this implementation is the need to explicitly mark the hidden attribute and redefine `__dir__` in each module. However, leveraging Python's `inspect` module, which provides utilities for manipulating execution frames, we can create functionality like the following:

```python
# mymodule.py

from hide import hidden

with hidden():
    import numpy as np

_private = "baz"

def f(arr):
    return np.asarray(arr) + 1
```

By employing such a mechanism, we can enhance the readability and usability of our scientific computing tools within Jupyter environments. This approach minimizes the exposure of unnecessary elements during autocompletion, promoting a cleaner and more focused interface for users.
