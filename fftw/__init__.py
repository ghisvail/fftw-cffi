# Copyright (c) 2016, Imperial College London
# Copyright (c) 2016, Ghislain Antony Vaillant
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD license. See the accompanying LICENSE file
# or read the terms at https://opensource.org/licenses/BSD-3-Clause.

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('fftw-cffi').version
except DistributionNotFound:
    __version__ = 'unknown'