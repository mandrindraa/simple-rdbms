# catalog/data_types.py
class DataType:
    """Base class for all data types"""
    pass

class IntegerType(DataType):
    def validate(self, value):
        return isinstance(value, int)
    
    def serialize(self, value):
        return value.to_bytes(4, byteorder='big')
    
    def deserialize(self, bytes_value):
        return int.from_bytes(bytes_value, byteorder='big')

class VarcharType(DataType):
    def __init__(self, max_length):
        self.max_length = max_length
    
    def validate(self, value):
        return isinstance(value, str) and len(value) <= self.max_length
    
    def serialize(self, value):
        encoded = value.encode('utf-8')
        length = len(encoded).to_bytes(2, byteorder='big')
        return length + encoded
    
    def deserialize(self, bytes_value):
        length = int.from_bytes(bytes_value[:2], byteorder='big')
        return bytes_value[2:2+length].decode('utf-8')