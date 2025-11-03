development
============

1. Create a Python Virtual Environment

.. code:: console

    python3 -m venv venv
    source venv/bin/activate

2. Switch NVM to use 14.21.3

.. code:: console
    nvm install lts/fermium
    nvm use lts/fermium

If on Apple Silicon node versions less than 14 won't run.
Instructions here can be used to run Terminal in Rosetta on x86 emulation.
https://stackoverflow.com/questions/67254339/nvm-install-node-fails-to-install-on-macos-big-sur-m1-chip


    How to open terminal in Rosetta2 mode: Go to Application -> Right click on terminal app -> Get Info -> Select "Open using Rosetta" -> Restart Terminal
    In Terminal, write -> arch -x86_64 zsh


3. ``npm install``

4. ``pip install -r requirements.txt``

5. ``npm run dev``



Installation
============

This theme is distributed on PyPI_ and can be installed with ``pip``:

.. code:: console

   $ pip install sphinx-rtd-theme

To use the theme in your Sphinx project, you will need to edit
your ``conf.py`` file's ``html_theme`` setting:

.. code:: python

    html_theme = "nccoe_rtd_theme"

.. admonition:: See also:

    `Supported browsers`_
        Officially supported and tested browser/operating system combinations

    `Supported dependencies`_
        Supported versions of Python, Sphinx, and other dependencies.

    `Example documentation`_
        A full example of this theme output, with localized strings enabled.

.. _PyPI: https://pypi.python.org/pypi/nccoe_rtd_theme
.. _Supported browsers: https://sphinx-rtd-theme.readthedocs.io/en/stable/development.html#supported-browsers
.. _Supported dependencies: https://sphinx-rtd-theme.readthedocs.io/en/stable/development.html#supported-dependencies
.. _Example documentation:  https://sphinx-rtd-theme.readthedocs.io/en/stable/

Configuration
=============

This theme is highly customizable on both the page level and on a global level.
To see all the possible configuration options, read the documentation on
`configuring the theme`_.

.. _configuring the theme: https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

Contributing
============

If you would like to help modify or translate the theme, you'll find more
information on contributing in our `contributing guide`_.

.. _contributing guide: https://sphinx-rtd-theme.readthedocs.io/en/stable/contributing.html
