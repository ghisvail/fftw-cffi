# Copyright (c) 2016, Imperial College London
# Copyright (c) 2016, Ghislain Antony Vaillant
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD license. See the accompanying LICENSE file
# or read the terms at https://opensource.org/licenses/BSD-3-Clause.

from __future__ import absolute_import

from ._wrappers import *
from enum import IntEnum, unique

__all__ = ('Direction', 'Flag', 'Plan')


@unique
class Direction(IntEnum):
    forward = FFTW_FORWARD
    backward = FFTW_BACKWARD


@unique
class Flag(IntEnum):
    estimate = FFTW_ESTIMATE
    measure = FFTW_MEASURE
    patient = FFTW_PATIENT
    exhaustive = FFTW_EXHAUSTIVE    
    wisdom_only = FFTW_WISDOM_ONLY
    destroy_input = FFTW_DESTROY_INPUT
    preserve_input = FFTW_PRESERVE_INPUT
    unaligned = FFTW_UNALIGNED


class Plan(object):
    
    def __init__(self, input_array, output_array, direction=Direction.forward,
                 flags=(Flag.estimate,), *args, **kwargs):
        if input_array.shape != output_array.shape:
            raise ValueError('Incompatible shapes between input and output '
            'arrays.')
        if input_array.dtype != output_array.dtype:
            raise ValueError('Incompatible dtypes between input and output '
            'arrays.')
        self.input_array = input_array
        self.output_array = output_array
        self.__handle = fftw_create_plan(self.input_array, self.output_array,
                                         direction, flags) 

    def __del__(self):
        fftw_destroy_plan(self.__handle)

    def __call__(self, input_array=None, normalize=False, *args, **kwargs):
        self.execute(input_array=input_array)
        if normalize:
            return self.output_array / self.output_array.size
        else:
            return self.output_array

    def execute(self, input_array=None, output_array=None):
        if input_array is not None:
            # TODO: use descriptor.
            self.input_array = input_array
        if output_array is not None:
            # TODO: use descriptor.
            self.output_array = output_array
        fftw_execute_plan(self.__handle, self.input_array, self.output_array)
