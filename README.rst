stage
=====

⚙️ `server.conf <server.example.conf>`_
    Configure the server

🔎 `api/loader.py <api/loader.py>`_ 
    Searchs for python files in `api/ <api/>`_ using `utils/tree.py <utils/tree.py>`_ and loads them as flask blueprints.

📁 `db/database.py <db/database.py>`_
    Uses ``sqlalchemy`` to manage the ``sqlite`` database and provides ``Session`` class.


Usage
-----

.. code-block:: console

    docker build -t stage .
    docker run -d -p 8080:8080 --name stage stage
