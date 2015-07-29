.. raw:: latex
  
      \newpage

.. _install_windows:

Windows
-------

To install mixcoatl on windows:

1. If the system does not have Python, Download Python >= 2.7 `from here <https://www.python.org/downloads/>`_

2. Open PowerShell as administrator by right clicking on the PowerShell icon and selecting ‘Run as Admin’

3. Run the following command to allow running of scripts: 

.. code-block:: powershell

   Set-ExecutionPolicy Unrestricted 

4. Create a directory for the environment variables 

.. code-block:: powershell

   mkdir c:\envs 

   cd c:\envs

5. Download the bootstrap scripts for easy_install and pip: 

.. code-block:: powershell

   (new-object System.Net.WebClient).DownloadFile('http://python-distribute.org/distribute_setup.py', 'c:\envs\distribute_setup.py')  
   (new-object System.Net.WebClient).DownloadFile('https://raw.github.com/pypa/pip/master/contrib/get-pip.py', 'c:\envs\get-pip.py')

6. Run the setup script

.. code-block:: powershell

   .\python.exe c:\envs\distribute_setup.py 

   .\python.exe c:\envs\get-pip.py

7. Add the Python and Scripts directories to the $PATH 

.. code-block:: powershell

   setx PATH "%PATH%;C:\Python27\Scripts;C:\Python27"

8. Restart PowerShell

9. Install Mixcoatl

.. code-block:: powershell

   pip install mixcoatl

The PIP installation process will handle all of the dependency resolution.

Post-Installation
~~~~~~~~~~~~~~~~~

1. Generate API keys from DCM console

2. Set Environment Variables

.. code-block:: powershell

   $env:DCM_ACCESS_KEY=“access-key”
   $env:DCM_SECRET_KEY=“secret-key”
   $env:DCM_API_VERSION=“api-version”
   $env:DCM_ENDPOINT=“https:/your.dcm_url/api/enstratus/<api version>

Alternatively, the variables can be set in a non-persistent way on via the command prompt:

.. code-block:: powershell

   set DCM_ACCESS_KEY=access-key
   set DCM_SECRET_KEY=secret-key
   set DCM_API_VERSION=api-version
   set DCM_ENDPOINT=https:/your.dcm_url/api/enstratus/<api version>
