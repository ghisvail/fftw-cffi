# Copyright (c) 2016, Imperial College London
# Copyright (c) 2016, Ghislain Antony Vaillant
# All rights reserved.
#
# Distributed under the terms of the new BSD license.
# See the accompanying LICENSE file or read the terms at
# https://opensource.org/licenses/BSD-3-Clause.

from __future__ import absolute_import, division

from fftw.fftw import Plan, Direction
import numpy
import numpy.fft as fft
import numpy.testing as testing


def ranf_unit_complex(shape, dtype=numpy.complex):
    def fillvalue(*args, **kwargs):
        return numpy.random.ranf() + 1j * numpy.random.ranf()
    return numpy.fromfunction(
        function=numpy.vectorize(fillvalue, otypes=(dtype,)), shape=shape)


tested_shapes = (
    (64,),
    (256,),
    (1024,),
    (32, 32),
    (64, 64),
    (96, 96),
)


def test_plan_call():
    for shape in tested_shapes:
        plan = Plan(
            input_array=ranf_unit_complex(shape),
            output_array=numpy.empty(shape, dtype=numpy.complex),
            direction=Direction.forward,
        )
        testing.assert_allclose(
            plan(),
            fft.fftn(plan.input_array)
        )
        testing.assert_allclose(
            plan(normalize=True),
            fft.fftn(plan.input_array) / plan.input_array.size
        )
        plan = Plan(
            input_array=ranf_unit_complex(shape),
            output_array=numpy.empty(shape, dtype=numpy.complex),
            direction=Direction.backward
        )
        testing.assert_allclose(
            plan(),
            fft.ifftn(plan.input_array) * plan.input_array.size
        )
        testing.assert_allclose(
            plan(normalize=True),
            fft.ifftn(plan.input_array)
        )