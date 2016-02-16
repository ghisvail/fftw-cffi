# Copyright (c) 2016, Imperial College London
# Copyright (c) 2016, Ghislain Antony Vaillant
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD license. See the accompanying LICENSE file
# or read the terms at https://opensource.org/licenses/BSD-3-Clause.


from cffi import FFI
import pkgconfig


if not pkgconfig.exists("fftw3"):
    raise RuntimeError("NFFT library not found via pkgconfig.")
# Transform pkgconfig output to a dictionary of lists, which is the only format
# accepted by distutils.
pc_fftw3 = {key: list(val) for (key, val) in pkgconfig.parse("fftw3").items()}


ffi = FFI()

ffi.cdef(
    """
    #define FFTW_FORWARD ...
    #define FFTW_BACKWARD ...
    #define FFTW_MEASURE ...
    #define FFTW_DESTROY_INPUT ...
    #define FFTW_UNALIGNED ...
    #define FFTW_CONSERVE_MEMORY ...
    #define FFTW_EXHAUSTIVE ...
    #define FFTW_PRESERVE_INPUT ...
    #define FFTW_PATIENT ...
    #define FFTW_ESTIMATE ...
    #define FFTW_WISDOM_ONLY ...

    typedef ... fftw_complex;
    typedef ... *fftw_plan;

    void fftw_execute(const fftw_plan);
    fftw_plan fftw_plan_dft(int, const int *, fftw_complex *, fftw_complex *,
                            int, unsigned);
    void fftw_execute_dft(const fftw_plan, fftw_complex *, fftw_complex *);
    void fftw_destroy_plan(fftw_plan);
    """
)

ffi.set_source(
    '_bindings',
    """
    #include <fftw3.h>
    """,
    **pc_fftw3
)


if __name__ == "__main__":
    ffi.compile()
