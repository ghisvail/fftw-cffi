from cffi import FFI
from pkgconfig import parse


config = parse('fftw3')

cdef = """
typedef ... fftw_complex;
typedef ... *fftw_plan;
void fftw_execute(const fftw_plan);
fftw_plan fftw_plan_dft(int, const int *, fftw_complex *, fftw_complex *,
                        int, unsigned);
void fftw_execute_dft(const fftw_plan, fftw_complex *, fftw_complex *);
void fftw_destroy_plan(fftw_plan);
"""

source = """
#include "fftw3.h"
"""

ffibuilder = FFI()
ffibuilder.cdef(cdef)
ffibuilder.set_source('_ffi', source, **config)


if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
