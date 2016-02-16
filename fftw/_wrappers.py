# Copyright (c) 2016, Imperial College London
# Copyright (c) 2016, Ghislain Antony Vaillant
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD license. See the accompanying LICENSE file
# or read the terms at https://opensource.org/licenses/BSD-3-Clause.

from __future__ import absolute_import

from ._bindings import ffi, lib
from functools import reduce

__all__ = ('FFTW_FORWARD', 'FFTW_BACKWARD', 'FFTW_MEASURE',
           'FFTW_DESTROY_INPUT','FFTW_UNALIGNED', 'FFTW_EXHAUSTIVE',
           'FFTW_PRESERVE_INPUT','FFTW_PATIENT', 'FFTW_ESTIMATE',
           'FFTW_WISDOM_ONLY','fftw_create_plan', 'fftw_destroy_plan',
           'fftw_execute_plan')


FFTW_FORWARD = lib.FFTW_FORWARD
FFTW_BACKWARD = lib.FFTW_BACKWARD

FFTW_ESTIMATE = lib.FFTW_ESTIMATE
FFTW_MEASURE = lib.FFTW_MEASURE
FFTW_PATIENT = lib.FFTW_PATIENT
FFTW_EXHAUSTIVE = lib.FFTW_EXHAUSTIVE
FFTW_WISDOM_ONLY = lib.FFTW_WISDOM_ONLY
FFTW_DESTROY_INPUT = lib.FFTW_DESTROY_INPUT
FFTW_PRESERVE_INPUT = lib.FFTW_PRESERVE_INPUT
FFTW_UNALIGNED = lib.FFTW_UNALIGNED


def fftw_create_plan(input_array, output_array, sign, flags):
    return lib.fftw_plan_dft(
        input_array.ndim,
        ffi.new('const int []', input_array.shape),
        ffi.cast('fftw_complex *', input_array.ctypes.data),
        ffi.cast('fftw_complex *', output_array.ctypes.data),
        sign,
        reduce(lambda x, y: x | y, flags, 0),
    )


def fftw_destroy_plan(handle):
    lib.fftw_destroy_plan(handle)


def fftw_execute_plan(handle, input_array=None, output_array=None):
    if input_array is None and output_array is None:
        lib.fftw_execute(handle)
    elif input_array is not None and output_array is not None:
        lib.fftw_execute_dft(
            handle,
            ffi.cast('fftw_complex *', input_array.ctypes.data),
            ffi.cast('fftw_complex *', output_array.ctypes.data),
        )
    else:
        raise RuntimeError('Partial update of FFTW plan not supported.')