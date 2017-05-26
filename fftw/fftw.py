from enum import IntEnum
from fftw._fftw3 import ffi, lib
from operator import or_
from functools import reduce


class Direction(IntEnum):
    FORWARD = -1
    BACKWARD = 1


class Flag(IntEnum):
    ESTIMATE = 64
    MEASURE = 0
    PATIENT = 32
    EXHAUSTIVE = 8


class Plan(object):

    def __init__(self, input, output, direction=Direction.FORWARD,
                 flags=(Flag.ESTIMATE,), *args, **kwargs):
        from numpy import dtype
        if input.shape != output.shape:
            raise ValueError('Incompatible shapes')
        if input.dtype != output.dtype:
            raise ValueError('Incompatible dtypes')
        if input.dtype != dtype('cdouble'):
            raise ValueError('Unsupported dtypes')
        shape = input.shape
        self.__handle = lib.fftw_plan_dft(
            len(shape),
            ffi.new('const int []', shape),
            ffi.cast('fftw_complex *', input.ctypes.data),
            ffi.cast('fftw_complex *', output.ctypes.data),
            direction,
            reduce(or_, flags, 0)
        )

    @classmethod
    def fromdims(cls, dims, *args, **kwargs):
        from numpy import empty
        return cls(input=empty(dims, dtype='cdouble'),
                   output=empty(dims, dtype='cdouble'),
                   flags=(Flag.MEASURE,), *args, **kwargs)

    def __del__(self):
        lib.fftw_destroy_plan(self.__handle)

    def __call__(self, input=None, output=None):
        lib.fftw_execute_dft(
            self.__handle,
            ffi.cast('fftw_complex *', self.__input.ctypes.data),
            ffi.cast('fftw_complex *', self.__output.ctypes.data)
        )
