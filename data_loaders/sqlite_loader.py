# data_loaders/sqlite_loader.py
import sqlite3
import pandas as pd

class SQLiteLoader:
    def __init__(self, db_path, patient_table, data_table):
        self.db_path = db_path
        self.patient_table = patient_table
        self.data_table = data_table

    def load(self):
        with sqlite3.connect(self.db_path) as conn:
            patients_df = pd.read_sql_query(f"SELECT * FROM {self.patient_table}", conn)
            data_df = pd.read_sql_query(f"SELECT * FROM {self.data_table}", conn)

        # Join on foreign key
        merged = data_df.merge(
            patients_df,
            left_on='patient_fk',
            right_on='id',
            suffixes=('_data', '_patient')
        )

        return merged
