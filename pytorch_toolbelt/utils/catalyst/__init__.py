from __future__ import absolute_import

from .criterions import *
from .callbacks import *
from .metrics import *
from .opl import *
from .visualization import *
from .utils import *
from .loss_adapter import *

from catalyst.registry import MODULE, Registry, CRITERION


def _register_modules(r: Registry):
    from pytorch_toolbelt.modules import encoders as e

    r.add_from_module(e, prefix="tbt")


def _register_criterions(r: Registry):
    from pytorch_toolbelt import losses as l

    r.add_from_module(e, prefix="tbt")


MODULE.late_add(_register_modules)
CRITERION.late_add(_register_criterions)
