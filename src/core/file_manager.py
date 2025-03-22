"""file_manager"""

import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class StorageEngine():
    """this is used for data persistency"""
    def __init__(self, db_name):
        self.path = f"{os.getenv("ROOT")}/data/{db_name}_db"
        dbs = StorageEngine.list_db()
        self.metadata = Metadata(db_name)
        if f"{db_name}_db" in dbs:
            print(f"Cannot create database: {db_name} already exists.")
        else:
            os.mkdir(self.path)
            with open(f"{self.path}/metadata", 'w', encoding="utf-8") as file:
                infos = {  "db_name": db_name,"tables": [] }
                json.dump(infos, file, indent=4)
            print("Database created")


    def drop(self):
        """remove the database"""
        os.chdir(os.getenv("ROOT"))
        os.rmdir(self.path)

    def use(self):
        """switch to the database dir"""
        try:
            os.chdir(self.path)
        except FileNotFoundError as file_not_found:
            print(f"{file_not_found.filename} This database does not exists.")

    def create_table(self, table_name, schema: dict[str, any]):
        """create table and schema for the named table"""
        tables = os.listdir(self.path)
        if table_name in tables:
            print(f"Table: {table_name} already exists")
        else:
            os.chdir(self.path)
            self.metadata.write_metadata(table_name, schema)
            print(f"Table {table_name} created")
    @staticmethod
    def list_db():
        """list all database"""
        db = f"{os.getenv("ROOT")}/data"
        return os.listdir(db)


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
            return metadata.read()
