try:
    from ._version import __version__
except ImportError:
    __version__ = '__Хз__'

from .events import *
from . import dispatcher as dp
from .database import db
