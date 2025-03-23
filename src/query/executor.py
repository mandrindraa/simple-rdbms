"""
SQLExecutor class to parse and execute SQL commands.
"""
import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword
from core.file_manager import StorageEngine
class SQLExecutor:
    """Parse and execute SQL commands."""
    def __init__(self, storage_engine):
        self.storage_engine = storage_engine

    def execute(self, command):
        """Parse and execute an SQL command."""
        parsed = sqlparse.parse(command)
        statement = parsed[0]  # Assume a single statement for simplicity
        # Identify the type of SQL command
        command_type = statement.get_type()

        if command_type == "CREATE":
            self._handle_create(statement)
        elif command_type == "INSERT":
            self._handle_insert(statement)
        elif command_type == "SELECT":
            self._handle_select(statement)
        else:
            self._handle_use(statement)
            self._handle_list(statement)

    def _handle_use(self, statement):
        """Handle database switch"""
        tokens = [token for token in statement.tokens if not token.is_whitespace]
        print(f"From use, {tokens}")
        for i, token in enumerate(tokens):
            if token.ttype == Keyword and token.value.upper() == "USE":
                db_name = tokens[i+1].get_real_name()
                self.storage_engine.use(db_name)
    def _handle_list(self, statement):
        """Handle LIST <TABLE | DATABASE> commands."""
        tokens = [token for token in statement.tokens if not token.is_whitespace]
        for i, token in enumerate(tokens):
            if token.ttype == Identifier and token.value.upper() == "LIST":
                print("From list")
                action = tokens[i+1].get_real_name()
                if action.upper() == "TABLE":
                    db_name = tokens[i+2].get_real_name()
                    print(StorageEngine.list_tables(db_name))
                else:
                    print(StorageEngine.list_db())

    def _handle_create(self, statement):
        """Handle CREATE <TABLE | DATABASE> commands."""
        tokens = [token for token in statement.tokens if not token.is_whitespace]
        table_name = None
        schema = {}

        for i, token in enumerate(tokens):
            if token.ttype == Keyword and token.value.upper() == "DATABASE":
                database_name = tokens[i + 1].get_real_name()
                self.storage_engine.create_database(database_name)
                print(f"Database '{database_name}' created.")
                return
            if token.ttype == Keyword and token.value.upper() == "TABLE":
                table_name = tokens[i + 1].get_real_name()
                self.storage_engine.create_table(table_name, {})
            if isinstance(token, IdentifierList):
                for column in token.get_identifiers():
                    column_name, column_type = column.value.split()
                    schema[column_name] = column_type

        if table_name:
            self.storage_engine.create_table(table_name, schema)
            print(f"Table '{table_name}' created with schema: {schema}")
        else:
            print("Invalid CREATE TABLE syntax.")

    def _handle_insert(self, statement):
        """Handle INSERT INTO commands."""
        # Parse and implement INSERT logic here
        print(f"INSERT command not implemented yet: {statement}")

    def _handle_select(self, statement):
        """Handle SELECT commands."""
        # Parse and implement SELECT logic here
        print(f"SELECT command not implemented yet: {statement}")
    def exit(self):
        """Rt"""
        return 0
