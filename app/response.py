class Response:
    def __init__(self):
        self.status = ''
        self.response = ''
        self.data = ''
    
    def toDict(self):
        return self.__dict__