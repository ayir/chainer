import chainerx

import numpy


result_dtypes_two_arrays = [
    # Bools.
    (('bool_', 'bool_'), 'bool'),
    # Floats.
    (('float16', 'float16'), 'float16'),
    (('float32', 'float32'), 'float32'),
    (('float64', 'float64'), 'float64'),
    (('float32', 'float16'), 'float32'),
    (('float64', 'float16'), 'float64'),
    (('float64', 'float32'), 'float64'),
    # Signed ints.
    (('int8', 'int8'), 'int8'),
    (('int8', 'int16'), 'int16'),
    (('int8', 'int32'), 'int32'),
    (('int8', 'int64'), 'int64'),
    (('int16', 'int16'), 'int16'),
    (('int32', 'int32'), 'int32'),
    (('int64', 'int64'), 'int64'),
    (('int16', 'int32'), 'int32'),
    (('int16', 'int64'), 'int64'),
    (('int32', 'int64'), 'int64'),
    # Unsigned ints.
    (('uint8', 'uint8'), 'uint8'),
    # Signed int and unsigned int.
    (('uint8', 'int8'), 'int16'),
    (('uint8', 'int16'), 'int16'),
    (('uint8', 'int32'), 'int32'),
    # Int and float.
    (('int8', 'float16'), 'float16'),
    (('uint8', 'float16'), 'float16'),
    (('int16', 'float32'), 'float32'),
    (('int32', 'float32'), 'float32'),
    (('int64', 'float32'), 'float32'),
    # Bool and other.
    (('bool_', 'uint8'), 'uint8'),
    (('bool_', 'int8'), 'int8'),
    (('bool_', 'int16'), 'int16'),
    (('bool_', 'float16'), 'float16'),
    (('bool_', 'float64'), 'float64'),
]


result_dtypes_three_arrays = [
    # Signed ints.
    (('int32', 'int32', 'int32'), 'int32'),
    (('int8', 'int8', 'int32'), 'int32'),
    (('int8', 'int16', 'int32'), 'int32'),
    (('int8', 'int32', 'int32'), 'int32'),
    (('int8', 'int64', 'int32'), 'int64'),
    # Unsigned ints.
    (('uint8', 'uint8', 'uint8'), 'uint8'),
    (('uint8', 'uint8', 'int8'), 'int16'),
    (('uint8', 'int8', 'int8'), 'int16'),
    (('uint8', 'int8', 'int16'), 'int16'),
    (('uint8', 'uint8', 'int16'), 'int16'),
    # Float and signed int.
    (('float16', 'int8', 'int8'), 'float16'),
    (('float16', 'int32', 'int64'), 'float16'),
    (('float16', 'float32', 'int64'), 'float32'),
    # Float and unsigned int.
    (('float16', 'int8', 'uint8'), 'float16'),
    (('float16', 'int32', 'uint8'), 'float16'),
    (('float16', 'float32', 'uint8'), 'float32'),
    # Bool and other.
    (('bool_', 'uint8', 'uint8'), 'uint8'),
    (('bool_', 'bool_', 'uint8'), 'uint8'),
    (('bool_', 'int8', 'uint8'), 'int16'),
    (('bool_', 'bool_', 'int32'), 'int32'),
    (('bool_', 'float16', 'float32'), 'float32'),
    (('bool_', 'bool_', 'float64'), 'float64'),
]


def cast_if_numpy_array(xp, array, chx_expected_dtype):
    """Casts NumPy result array to match the dtype of ChainerX's corresponding
    result.

    This function receives result arrays for both NumPy and ChainerX and only
    converts dtype of the NumPy array.
    """
    assert xp in (chainerx, numpy)
    assert isinstance(array, xp.ndarray)

    # Dtype conversion to allow comparing the correctnesses of the values.
    if xp is numpy:
        return array.astype(chx_expected_dtype, copy=False)

    return array
