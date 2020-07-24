===============
Traverse invoke
===============


.. image:: https://img.shields.io/pypi/v/traverse_invoke.svg
        :target: https://pypi.python.org/pypi/traverse_invoke

.. image:: https://img.shields.io/travis/DaniloZZZ/traverse_invoke.svg
        :target: https://travis-ci.org/DaniloZZZ/traverse_invoke

.. image:: https://readthedocs.org/projects/traverse-invoke/badge/?version=latest
        :target: https://traverse-invoke.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


A nested method [computation model] for nested data

This shit is a blessing. I don't know anything like this except maybe lambda. 

Please do yourself a favor and read the source. 

Docs not yet available, since the whole computation model needs to be formed, 
which requires some experience of using current version.


* Documentation: https://traverse-invoke.readthedocs.io   (uder development. maybe).


Features
--------

* Invoke methods by their path in module tree.
* Pass arguments as nested closures for methods.
* Modify invocation path in runtime (the most exiting thing).


Basic Usage
===========

**Invoke method**

.. code-block:: python

   import sys, traverse_invoke

   method = 'sys.version'
   names = {
   'sys':{'version':sys.version}}
   }
   args = { 'version':'foobar'}

   traverse_invoke.entry_traverse(args, method, names)

This will invoke ``sys.version(**{version:foobar})``

**Traverse**

see test


Discussion
==========

Traverse Invoke allows mapping nested data with matching functions. Given following dictionary:


Let's say we have a complicated namespace of functions

.. code-block:: python

    funcs = {
        'CRM systems':{
            'Hubspot': {
                'create lead':lambda **data: print('Lead data', data)
                ,'create deal':lambda **data: print('Deal data', data)
                }
            ,'Salesforce': {
                'create lead':lambda **data: print('Salesforce lead data', data)
                ,'create deal':lambda **data: print('Salesforce deal data', data)
                }

            }

Config:

.. code-block:: yaml

    Leads:
        - name: Mark
          phone: 111210111
          Salesforce:
            phone: 1000000000
            create deal:
                phone: 10012000
          Hubspot:
            name: Mark Twain

Note that except generic properties there are specific values for each CRM, and CRM methods.
Want to create deals in both CRMs:

.. code-block:: python

    for lead in leads:
        fpath = 'CRM systems.Hubspot.create lead.Salesforce.create lead'.split('.')

        traverse_invoke(lead, fpath, funcs)

This example is in examples folder


.. code-block:: bash
    Salesforce lead data {'name': 'Mark', 'phone': 1000000000, ... }
    Lead data {'name': 'Mark Twain', 'phone': 111210111, ... 
