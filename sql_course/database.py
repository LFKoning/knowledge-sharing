"""Module for the SQLite wrapper class."""
import sqlite3
from typing import Union

import pandas as pd


class Database:
    """Simple SQLite wrapper with some convenience functions.

    Parameters
    ----------
    filepath : str
        Path to the SQLite .db file.
    """

    def __init__(self, filepath: str) -> None:
        self._connection = sqlite3.connect(filepath)

    def list_tables(self):
        """List tables in the database.

        Returns
        -------
        pandas.DataFrame
            DataFrame listing the available tables.
        """

        return self.query(
            "SELECT name, sql FROM sqlite_master WHERE type='table';"
        )

    def query(self, sql: str) -> Union[pd.DataFrame, int]:
        """Execute the SQL statement against the database.

        Parameters
        ----------
        sql : str
            SQL query to perform

        Returns
        -------
        pandas.DataFrame or int
            Pandas DataFrame for SELECT queries, affected rows for all
            other query types.
        """

        with self._connection:
            cursor = self._connection.cursor()
            result = cursor.execute(sql)

            # CREATE / INSERT / UPDATE queries
            if cursor.description is None:
                return result.rowcount

            # SELECT queries
            else:
                columns = [col[0] for col in cursor.description]
                df = pd.DataFrame(result.fetchall(), columns=columns)
                return df
