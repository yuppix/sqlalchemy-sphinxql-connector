""" CyMySQL connector"""

import cymysql
from cymysql.connections import Connection
from sqlalchemy.dialects.mysql import cymysql as cymysql_dialect
from sqlalchemy_sphinxql_connector.dialect import SphinxDialect

__all__ = ("Dialect",)


class DBAPIShim(object):

    def connect(self, *args, **kwargs):
        return Connection(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(cymysql, name)


class Dialect(SphinxDialect, cymysql_dialect.MySQLDialect_cymysql):

    @classmethod
    def dbapi(cls):
        return DBAPIShim()
