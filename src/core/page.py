
class Page:
    def __init__(self, page_id, size=4096):
        self.page_id = page_id
        self.size = size
        self.data = bytearray(size)
        self.free_space_pointer = 0
    
    def add_record(self, serialized_data):
        if len(serialized_data) + self.free_space_pointer > self.size:
            return False  # Page full
        
        start_pos = self.free_space_pointer
        self.data[start_pos:start_pos + len(serialized_data)] = serialized_data
        self.free_space_pointer += len(serialized_data)
        return start_pos  # Return position where record was inserted
    
    def get_record(self, position, length):
        return bytes(self.data[position:position + length])