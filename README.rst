=========
fftw-cffi
=========

Compute fast Fourier transforms in Python.

Example
=======

The following code snippet shows how to compute the forward Fourier transform 
of an arbitrary array of 64 samples::

    >>> from fftw.fftw import Plan
    >>> import numpy
    >>> input_array = numpy.arange(64, dtype=numpy.complex)
    >>> plan = Plan(input_array, output_array=numpy.empty_like(input_array))
    >>> result_array = plan()

    >>> print(input_array)
    [  0.+0.j   1.+0.j   2.+0.j   3.+0.j   4.+0.j   5.+0.j   6.+0.j   7.+0.j
       8.+0.j   9.+0.j  10.+0.j  11.+0.j  12.+0.j  13.+0.j  14.+0.j  15.+0.j
      16.+0.j  17.+0.j  18.+0.j  19.+0.j  20.+0.j  21.+0.j  22.+0.j  23.+0.j
      24.+0.j  25.+0.j  26.+0.j  27.+0.j  28.+0.j  29.+0.j  30.+0.j  31.+0.j
      32.+0.j  33.+0.j  34.+0.j  35.+0.j  36.+0.j  37.+0.j  38.+0.j  39.+0.j
      40.+0.j  41.+0.j  42.+0.j  43.+0.j  44.+0.j  45.+0.j  46.+0.j  47.+0.j
      48.+0.j  49.+0.j  50.+0.j  51.+0.j  52.+0.j  53.+0.j  54.+0.j  55.+0.j
      56.+0.j  57.+0.j  58.+0.j  59.+0.j  60.+0.j  61.+0.j  62.+0.j  63.+0.j]

    >>> print(result_array)
    [ 2016.  +0.j           -32.+651.374964j     -32.+324.9014524j
       -32.+215.72647697j   -32.+160.87486375j   -32.+127.75116108j
       -32.+105.48986269j   -32. +89.43400872j   -32. +77.254834j
       -32. +67.65831544j   -32. +59.86778918j   -32. +53.38877458j
       -32. +47.89138441j   -32. +43.14700523j   -32. +38.99211282j
       -32. +35.30655922j   -32. +32.j           -32. +29.00310941j
       -32. +26.26172131j   -32. +23.73281748j   -32. +21.38171641j
       -32. +19.18006188j   -32. +17.10435635j   -32. +15.13487283j
       -32. +13.254834j     -32. +11.44978308j   -32.  +9.70709388j
       -32.  +8.01558273j   -32.  +6.36519576j   -32.  +4.7467516j
       -32.  +3.15172491j   -32.  +1.57205919j   -32.  +0.j
       -32.  -1.57205919j   -32.  -3.15172491j   -32.  -4.7467516j
       -32.  -6.36519576j   -32.  -8.01558273j   -32.  -9.70709388j
       -32. -11.44978308j   -32. -13.254834j     -32. -15.13487283j
       -32. -17.10435635j   -32. -19.18006188j   -32. -21.38171641j
       -32. -23.73281748j   -32. -26.26172131j   -32. -29.00310941j
       -32. -32.j           -32. -35.30655922j   -32. -38.99211282j
       -32. -43.14700523j   -32. -47.89138441j   -32. -53.38877458j
       -32. -59.86778918j   -32. -67.65831544j   -32. -77.254834j
       -32. -89.43400872j   -32.-105.48986269j   -32.-127.75116108j
       -32.-160.87486375j   -32.-215.72647697j   -32.-324.9014524j
       -32.-651.374964j  ]

Installation
============

Requirements
------------

The following dependencies are required to build, run and test the package:

  - setuptools
  - pkgconfig
  - numpy
  - cffi
  - nose

An installation of the FFTW library is required. It should be discoverable 
with a call to pkg-config::

  $ pkg-config --libs fftw3

Local or non-system installation locations are supported using 
PKG_CONFIG_PATH::

  $ export PKG_CONFIG_PATH=$HOME/local/lib/pkgconfig
  $ pkg-config --libs fftw3

Using pip
---------

The recommended way to install the package is via pip::

  $ pip install fftw-cffi

Using setup.py 
--------------

This method is suitable for environments where pip is not available, or for 
testing modifications to the package::

  $ python setup.py install

Contributing
============

Guidelines
----------

The development team welcomes feedback, code and enhancement proposals to the 
package from the community. Please consider opening an issue or submitting 
patches for inclusion to the code base via pull-request. For code 
contributions, please provide appropriate test cases for each new features and 
verify that the complete test suite runs successfully.

Running the tests
-----------------

If the bindings were modified, then one should first rebuild the CFFI module 
with::

  $ python setup.py build_ext --inplace

Before running the test suite with a call to::

  $ python setup.py nosetests

License
=======

The **fftw-cffi** source code is released under the terms of the `new BSD 
license <https://opensource.org/licenses/BSD-3-Clause>`_. The copyright 
information can be checked out in the accompanying `LICENSE <LICENSE>`_ file.

A separate installation of the FFTW library is required. The source code can 
be downloaded from the official `homepage <http://www.fftw.org>`_ and 
installed following the instructions available in the corresponding README 
file. The FFTW library is licensed under the `GPL version 2 or later 
<http://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html>`_.