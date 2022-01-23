from .EC2 import *

try:
    from .local import *
except:
    pass