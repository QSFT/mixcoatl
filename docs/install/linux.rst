.. raw:: latex
  
      \newpage

.. _install_linux:

Linux, OS X
-----------

Installing Mixcoatl on a Unix system like Linux or OS X is done using Python setuptools and pip. First we need to obtain
those tools from your system package manager. Examples are shown below for apt based and yum based systems.

Mixcoatl is tested on Ubuntu 12.04, 14.04, RHEL 6, 7 (and derivatives like CentOS), and OSX 10.10 (Yosemite). However it
will generally work on any distribution where `pip` is available.


Prerequisites
^^^^^^^^^^^^^

Before we can install mixcoatl we need the python setuptools and `pip`. Get them using which ever package manger you have
available.

**apt-get:**


.. code-block:: bash

    $ sudo apt-get install python-pip

**yum:**

.. code-block:: bash

    $ sudo yum install epel-release
    $ sudo yum install python-pip

**OSX:**

.. code-block:: bash

    $ sudo easy_install pip

Install mixcoatl with pip
^^^^^^^^^^^^^^^^^^^^^^^^^

Now that we have the python setuptools we are able able to use the `pip` command to install mixcoatl.

.. code-block:: bash

    $ pip install mixcoatl

Post Install
^^^^^^^^^^^^

In order for mixcoatl to be useful you must set a number of environment variables. This will tell the mixcoatl
command line tools where to find you DCM endpoint. For example (replace access key and secret keys with your own):

.. code-block:: bash

    export DCM_ENDPOINT="https://dcm.enstratius.com/api/enstratus/2015-06-29"
    export DCM_API_VERSION="2015-06-29"
    export DCM_ACCESS_KEY="SVDBDCDWNTPIDBXNEBVE"
    export DCM_SECRET_KEY="G0o7RawE2tC3O5vVOGXDWJIhyFYNH6bISlb9Zk7l"


API keys can be generated from the DCM console


Installing from Source (for experts)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is also possible to install mixcoatl from source. However, the recommended method is to use pip install as above.

First, clone the mixcoatl repository from git:

.. code-block:: bash

   $ git clone git@github.com:enStratus/mixcoatl.git

Then, use python to install:

.. code-block:: bash

   $ cd mixcoatl
   $ python setup.py install








