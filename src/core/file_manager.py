"""file_manager"""

import os
import json
from typing import Any

class StorageEngine():
    """this is used for data persistency"""
    path = f"{os.getenv("ROOT")}/data/"
    def __init__(self):
        self.metadata: Any
        self.tables = []
        if not os.path.isdir(self.path):
            os.makedirs(self.path)

    def drop(self):
        """remove the database"""
        os.chdir(os.getenv("ROOT"))
        os.rmdir(self.path)

    def use(self, db_name):
        """switch to the database dir"""
        try:
            os.chdir(f"{self.path}/{db_name}_db")
            print(f"Switch to database {db_name} successfully")
        except FileNotFoundError as file_not_found:
            print(f"{file_not_found.filename} This database does not exists.")

    def create_table(self, table_name, schema: dict[str, any]):
        """create table and schema for the named table"""
        self.tables = os.listdir(self.path)
        if table_name in self.tables:
            print(f"Table: {table_name} already exists")
        else:
            os.chdir(self.path)
            self.tables.append(table_name)
            with open(table_name, 'w', encoding='utf-8') as _:
                self.metadata.write_metadata(table_name, schema)
                print(f"Table {table_name} created")
    @staticmethod
    def list_db():
        """list all database"""
        db = f"{os.getenv("ROOT")}/data"
        return "|".join(os.listdir(db))
    @classmethod
    def create_database(cls, db_name):
        """this create a databse from a storage engine class"""
        cls.path = f"{os.getenv("ROOT")}/data/{db_name}_db"
        dbs = StorageEngine.list_db()
        cls.metadata = Metadata(db_name)
        if f"{db_name}_db" in dbs:
            print(f"Cannot create database: {db_name} already exists.")
        else:
            os.mkdir(cls.path)
            with open(f"{cls.path}/metadata", 'w', encoding="utf-8") as file:
                infos = {  "db_name": db_name,"tables": [] }
                json.dump(infos, file, indent=4)
            print("Database created")
    @classmethod
    def list_tables(cls, db_name):
        """List all table in a database"""
        tables = os.listdir(f"{cls.path}/{db_name}_db")
        for i in tables:
            if i == "metadata":
                tables.remove(i)
        return "\t".join(tables)

class Metadata():
    """the metadata of table"""
    def __init__(self, db_name):
        self.path = f"{os.getenv("ROOT")}/data/{db_name}_db/metadata"

    def write_metadata(self, new_table, schema):
        """create a schema for the database"""
        with open(self.path, 'r', encoding="utf-8") as metadata:
            data = json.load(metadata)
        if new_table not in data['tables']:
            data['tables'].append(new_table)
            data[new_table] = schema
            with open(self.path, 'w', encoding="utf-8") as metadata:
                json.dump(data, metadata, indent=4)
    def load_metadata(self):
        """load metadata in json format"""
        with open(self.path, 'r', encoding='utf-8') as metadata:
            return json.load(metadata)
