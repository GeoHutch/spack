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
#     spack install py-emopt
#
# You can edit this file again by typing:
#
#     spack edit py-emopt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyEmopt(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/anstmichaels/emopt" #Andy hasn't made a project website yet so I'm just using the github page
    url      = "https://github.com/anstmichaels/emopt"
    git      = "git://github.com/anstmichaels/emopt.git"

    # FIXME: Add proper versions and checksums here.
    # NOTE: emopt does not yet have specified releases, just the git master path
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version("master", branch="master")
    version("2019.5.6", branch="master", commit="06b648b")

    # FIXME: Add dependencies if required.
    extends("python")

    depends_on("petsc +complex+mumps+hdf5", type="build")
    depends_on("slepc", type="build")

    depends_on("py-petsc4py", type=("build","run"))
    depends_on("py-slepc4py", type=("build","run"))
    depends_on("py-scipy", type=("build","run"))
    depends_on("py-future", type="run")
    depends_on("py-mpi4py", type=("build","run"))
    depends_on("py-matplotlib", type="run")
    depends_on("py-h5py", type="run")

    depends_on("py-setuptools", type="build")
    depends_on("boost")
    depends_on("eigen")


