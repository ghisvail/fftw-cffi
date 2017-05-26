# Copyright (c) 2016, Imperial College London
# Copyright (c) 2016, Ghislain Antony Vaillant
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD license. See the accompanying LICENSE file
# or read the terms at https://opensource.org/licenses/BSD-3-Clause.

from fftw._ffi import ffi, lib
from numpy import ascontiguousarray, empty_like


def fftn(a):
    a = ascontiguousarray(a, dtype='cdouble')
    b = empty_like(a)
    p = lib.fftw_plan_dft(
        a.ndim,
        ffi.new('const int []', a.shape),
        ffi.cast('fftw_complex *', a.ctypes.data),
        ffi.cast('fftw_complex *', b.ctypes.data),
        -1,     # FFTW_FORWARD
        64      # FFTW_ESTIMATE
    )
    lib.fftw_execute(p)
    lib.fftw_destroy_plan(p)
    return b


def ifftn(a):
    a = ascontiguousarray(a, dtype='cdouble')
    b = empty_like(a)
    p = lib.fftw_plan_dft(
        a.ndim,
        ffi.new('const int []', a.shape),
        ffi.cast('fftw_complex *', a.ctypes.data),
        ffi.cast('fftw_complex *', b.ctypes.data),
        +1,     # FFTW_BACKWARD
        64      # FFTW_ESTIMATE
    )
    lib.fftw_execute(p)
    lib.fftw_destroy_plan(p)
    return b
