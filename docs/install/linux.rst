.. raw:: latex
  
      \newpage

.. _install_linux:

Linux, OS X
-----------

Installing Mixcoatl on a \*nix system like Linux or OS X is done using Python setuptools.

Use a package manager to install python setuptools, for example:

apt-get
^^^^^^^

.. code-block:: bash

   $ apt-get install python-setuptools

yum
^^^

.. code-block:: bash

   $ yum install python-setuptools

PIP/easy_install
~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ pip install mixcoatl

Installing from Source
~~~~~~~~~~~~~~~~~~~~~~

It is also possible to install mixcoatl from source.

First, clone the mixcoatl repository from git:

.. code-block:: bash

   git clone git@github.com:enStratus/mixcoatl.git

Then, use python to install:

.. code-block:: bash

   cd mixcoatl

   python setup.py install
