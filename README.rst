===============================================
plonetheme.depannenergiesnouvelles
===============================================

.. contents:: Table of Contents
   :depth: 2

Overview
--------

plonetheme.depannenergiesnouvelles is an installable Plone Theme using `plone.app.theming`_, based on
the default Sunburst Plone theme.

Requirements
------------

    * Tested with Plone 4.3.2 (http://plone.org/products/plone)

    * plone.app.theming (please configure your buildout corresponding to `plone.app.theming installation`_)

Screenshot
------------

.. image:: https://github.com/sylvainb/plonetheme.depannenergiesnouvelles/raw/master/docs/plonetheme-depannenergiesnouvelles-screenshot.png
   :height: 1039px
   :width: 1026px
   :scale: 70 %
   :alt: Screenshot
   :align: center

Installation
------------

Getting the theme
~~~~~~~~~~~~~~~~~~~~

Add ``plonetheme.depannenergiesnouvelles`` to your ``plone.recipe.zope2instance`` buildout section e.g.::

    [instance]
    ...
    eggs =
        Plone
        ...
        plonetheme.depannenergiesnouvelles

Or, you can add it as a dependency on your own product *setup.py*::

    install_requires=[
        ...
        'plonetheme.depannenergiesnouvelles',
    ],

Enabling the theme
~~~~~~~~~~~~~~~~~~~~

    Install the theme from the Add-ons control panel. That's it!

Quickly test ?
~~~~~~~~~~~~~~~~~~~~

Download ``plonetheme.depannenergiesnouvelles`` and use ``virtualenv`` and ``buildout`` to test the theme::

	easy_install virtualenv
	cd plonetheme.depannenergiesnouvelles
	virtualenv .
	source bin/activate
	(plonetheme.depannenergiesnouvelles) easy_install zc.buildout
	!!! check the buildout config file ``test-plone-base.cfg`` before running !!!
	(plonetheme.depannenergiesnouvelles) ln -s test-plone-4.3.x.cfg buildout.cfg
	(plonetheme.depannenergiesnouvelles) python bootstrap.py
	(plonetheme.depannenergiesnouvelles) bin/buildout
	[...] be patient... [...]
	(plonetheme.depannenergiesnouvelles) ./bin/instance fg

Go to http://localhost:8080, add a new Plone Site and install plonetheme.depannenergiesnouvelles.

Launch tests::

	(plonetheme.depannenergiesnouvelles) ./bin/test -s plonetheme.depannenergiesnouvelles

Launch code coverage::

    (plonetheme.depannenergiesnouvelles) bin/coverage
    (plonetheme.depannenergiesnouvelles) bin/report
    And open with a browser htmlcov/index.html

Credits
-------

    * Sylvain Boureliou [sylvainb] - `GitHub <https://github.com/sylvainb>`_ - `Website <http://www.boureliou.com>`_

Source code
-----------

`Source code <https://github.com/sylvainb/plonetheme.depannenergiesnouvelles>`_ is hosted on Github.

How to contribute and submit a patch ?
--------------------------------------

`Source code <https://github.com/sylvainb/plonetheme.depannenergiesnouvelles>`_ and an `issue tracker <https://github.com/sylvainb/plonetheme.depannenergiesnouvelles/issues>`_ is hosted on Github.





.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`plone.app.theming installation`: http://pypi.python.org/pypi/plone.app.theming#installation

