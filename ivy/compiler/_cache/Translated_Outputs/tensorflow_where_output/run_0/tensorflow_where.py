import tensorflow

from typing import Union
from typing import Optional

from .tensorflow__helpers import tensorflow_asarray
from .tensorflow__helpers import tensorflow_default_dtype
from .tensorflow__helpers import tensorflow_is_array


def tensorflow_where(
    condition: Union[tensorflow.Tensor, tensorflow.Variable],
    x1: Union[tensorflow.Tensor, tensorflow.Variable],
    x2: Union[tensorflow.Tensor, tensorflow.Variable],
    /,
    *,
    out: Optional[Union[tensorflow.Tensor, tensorflow.Variable]] = None,
):
    oirg_x1 = x1
    oirg_x2 = x2
    try:
        dtype = (
            x1.dtype
            if hasattr(x1, "dtype")
            else x2.dtype if hasattr(x2, "dtype") else tensorflow_default_dtype()
        )
        if not tensorflow_is_array(x1):
            x1 = tensorflow_asarray(x1, dtype=dtype)
        if not tensorflow_is_array(x2):
            x2 = tensorflow_asarray(x2, dtype=dtype)
    except:
        x1 = oirg_x1
        x2 = oirg_x2
    return tensorflow.cast(
        tensorflow.experimental.numpy.where(condition, x1, x2), x1.dtype
    )
