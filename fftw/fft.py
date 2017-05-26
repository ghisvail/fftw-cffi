# Copyright (c) 2016, Imperial College London
# Copyright (c) 2016, Ghislain Antony Vaillant
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD license. See the accompanying LICENSE file
# or read the terms at https://opensource.org/licenses/BSD-3-Clause.

from fftw._ffi import ffi, lib
from numpy import ascontiguousarray, empty_like
from numpy.fft import fftfreq, fftshift, ifftshift
from contextlib import contextmanager

__all__ = ('fftn', 'ifftn', 'fftfreq', 'fftshift', 'ifftshift')


@contextmanager
def make_plan(shape, input, output, sign, flags):
    p = lib.fftw_plan_dft(
        len(shape),
        ffi.new('const int []', shape),
        ffi.cast('fftw_complex *', input),
        ffi.cast('fftw_complex *', output),
        sign,
        flags
    )
    yield p
    lib.fftw_destroy_plan(p)


def fftn(a):
    a = ascontiguousarray(a, dtype='cdouble')
    b = empty_like(a)
    with make_plan(a.shape, a.ctypes.data, b.ctypes.data, -1, 64) as p:
        lib.fftw_execute(p)
    return b


def ifftn(a):
    a = ascontiguousarray(a, dtype='cdouble')
    b = empty_like(a)
    with make_plan(a.shape, a.ctypes.data, b.ctypes.data, +1, 64) as p:
        lib.fftw_execute(p)
    return b
