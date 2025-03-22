# catalog/schema.py
class Column:
    def __init__(self, name, data_type, primary_key=False):
        self.name = name
        self.data_type = data_type
        self.primary_key = primary_key

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.primary_key = next((col for col in columns if col.primary_key), None)
    
    def create_record(self, values):
        if len(values) != len(self.columns):
            raise ValueError("Number of values doesn't match columns")
        
        record = {}
        for col, val in zip(self.columns, values):
            if not col.data_type.validate(val):
                raise TypeError(f"Invalid type for column {col.name}")
            record[col.name] = val
        
        return record