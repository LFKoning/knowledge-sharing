"""Module for the SQLite wrapper class."""
import sqlite3
import pandas as pd


class Database:
    """
    SQLite Database wrapper with convenience functions.
    
    Parameters
    ----------
    filepath : str
        Path to the SQLite .db file.
    """
    
    def __init__(self, filepath):
        self._connection = sqlite3.connect(filepath)
        
    def list_tables(self):
        """List tables in the database."""

        return self.query(
            "SELECT name, sql FROM sqlite_master WHERE type='table';"
        )
        
    def query(self, sql):
        """
        Execute the SQL statement against the database.
        
        Parameters
        ----------
        sql : str
            SQL query to perform
        
        Returns
        Union[pandas.DataFrame, int]
            Pandas DataFrame for SELECT queries,
            affected rows for all other queries.
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
