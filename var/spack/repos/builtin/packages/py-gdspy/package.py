# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-gdspy
#
# You can edit this file again by typing:
#
#     spack edit py-gdspy
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyGdspy(PythonPackage):
    """Python package for manipulating GDSII stream files, usually CAD layouts."""

    
    homepage = "https://github.com/heitzmann/gdspy"
    url      = "https://github.com/heitzmann/gdspy/archive/v1.4.tar.gz"

    version('1.4',   sha256='030927a71685262160b87491b0ad9a500c4f3d915db0fdca9a1d6129b91ef810')
    version('1.3.2', sha256='472b71e5b996df9048d60ca383f851abc346050402600414efdcc33257ed29c2')
    version('1.3.1', sha256='3427c0fbd0a4ff437ab0171aa6cd0030763239315631dc187da39b9a34529c92')
    version('1.3',   sha256='bd89b3ec4450f76c726fc2f33768f6fe00df20e4077af33d143749b843e83a78')
    version('1.2.1', sha256='b429c54373ac5833e718c62319f39fa23352a572e5ece673658c7a0d8cd9c689')
    version('1.2',   sha256='ad7926155915f11e124a0f5f71110983079317dbb3d55be6489762eeae593c86')
    version('1.1.2', sha256='a23e3131d609cb9c92008a563d2824c3db63391097893fc035d215a0c74a52e3')
    version('1.1.1', sha256='dc2d3cfcd7b9fb2b2619060e6462b1ccc49e0399ce641d68bb64eab10aa540b4')
    version('1.1',   sha256='d25d6b5915c3762462c3875efe0d9ae79f9c6163f2d0dd5ebe7f56b4dc327e3d')
    version('1.0',   sha256='8be8ace938e0f71276c80b769f21df617448286b60f7258e4d7fd45028207824')

    extends('python')

    depends_on('py-setuptools', type='build')

    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-future',type=('build', 'run'))


#    def install(self, spec, prefix):
#        make()
#        make('install')
