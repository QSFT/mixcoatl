.. raw:: latex
  
      \newpage

.. _dcm_list_firewall_rules:

dcm-list-firewall-rules
-----------------------

Lists firwall rules.

Description
~~~~~~~~~~~

Returns a list of firewall rules.

Syntax
~~~~~~

.. program-output:: dcm-list-firewall-rules -h

Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -v, --verbose      | Produce verbose output                                     |
+--------------------+------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

The return value from this command is a list of firewall rules.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-firewall-rules 201

Output
%%%%%%

.. code-block:: bash

   +------------------+------------------+---------------+----------+-----------+---------+---------+----------+
   | Firewall Rule ID |      Source      |  Destination  | Protocol | From Port | To Port |   Type  |  Permit  |
   +------------------+------------------+---------------+----------+-----------+---------+---------+----------+
   |       211        |    0.0.0.0/0     | destination ? |   TCP    |    3306   |   3306  | INGRESS | permit ? |
   |       212        |    0.0.0.0/0     | destination ? |   TCP    |     22    |    22   | INGRESS | permit ? |
   |       213        |    0.0.0.0/0     | destination ? |   TCP    |     80    |    80   | INGRESS | permit ? |
   |       214        |       201        | destination ? |   ICMP   |    None   |   None  | INGRESS | permit ? |
   |       215        | 54.241.19.109/32 | destination ? |   TCP    |    2003   |   2003  | INGRESS | permit ? |
   +------------------+------------------+---------------+----------+-----------+---------+---------+----------+
