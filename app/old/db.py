import psycopg2
from flask import current_app, g

params_dic = {
  "port":"5432",
  "database":"statscan",
  "user":"postgres",
  "password":"PoBuCe60"
}

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(**params_dic)

        """g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row"""

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
