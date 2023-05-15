class JSONMalformed(Exception):

    def __init__(self, file):
        self.message = f"O Json {file} está mal formatado"
        super().__init__(self.message)
