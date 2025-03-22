"""
it is the main file of the project
"""

from core.file_manager import StorageEngine


test1 = StorageEngine("test")
test1.create_table("users", {"name": "str", "age": "int"})
test1.create_table("emails", {"provider": ["str", "primary key"], "email": "str"})
