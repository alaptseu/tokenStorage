import click
import os
from ts.cli import pass_context
from tinydb import TinyDB, Query, where
from urllib import parse
import platform
import tempfile

from ts.core.DataError import DataError


class DBHandler(object):
    """
    The main class of DBHandler
    Gives an access to TinyDb
    """
    tempdir = '/tmp' if platform.system() == 'Darwin' else tempfile.gettempdir()
    DEFAULT_DB = tempdir + '/urldb.json'
    DEFAULT_TABLE = 'oauth'

    def __init__(self, **kwargs):
        """
        Create a new instance of TinyDB.
        """
        self._db_path = kwargs.pop('db_path', self.DEFAULT_DB)
        self._db_table_name = kwargs.pop('db_table', self.DEFAULT_TABLE)
        self._db = TinyDB(self.db_path)
        self._token_table =  self.db.table(self._db_table_name)

    def add_token_data(self, data, key1, key2):
        key1_value = data[key1]
        key2_value = data[key2]
        result = self.token_table.search((where(key1) == key1_value) & (where(key2) == key2_value))
        if len(result) == 0:
            self.token_table.insert(data)
        else:
            raise DataError('Already exists')

    def get_all_auth_endpooints(self):
        return self.token_table.all()


    def search_token_endpoint(self, search_key, search_value):
        return self.token_table.search(where(search_key) == search_value)

    @property
    def db_path(self):
        return self._db_path

    @property
    def db_table_name(self):
        return self._db_table_name

    @property
    def db(self):
        return self._db

    @property
    def token_table(self):
        return self._token_table

    @token_table.setter
    def token_table(self, table):
        self._token_table = table




