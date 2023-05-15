class NoDataFound(Exception):

    def __init__(self):
        self.message = "Não foram encontrados dados"
        super().__init__(self.message)
