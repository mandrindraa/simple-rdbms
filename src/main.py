"""
it is the main file of the project
"""

from core.file_manager import StorageEngine
from query.executor import SQLExecutor


if __name__ == "__main__":
    storage_engine = StorageEngine()
    executor = SQLExecutor(storage_engine)
    while True:
        command = input("SSQL:# ")
        if command.lower() in ["exit", "quit"]:
            break
        executor.execute(command)
