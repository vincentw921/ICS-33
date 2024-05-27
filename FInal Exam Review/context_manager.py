class opener:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def __enter__(self):
        try:
            self.file = open(self.file_name)
            return self.file
        except:
            return None
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if not self.file:
            self.file.close()

with opener("functions.py") as f:
    print(f.readlines())
