class Autor :
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._cod = None
    
    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get_email(self):
        return self._email
    def _set_email(self, nome):
        self._email = email
    def _get_cod(self):
        return self._cod
    def _set_cod(self, cod):
        self._cod = cod

    nome = property( _get_nome, _set_nome)
    email = property( _get_email, _set_email)
    cod = property( _get_cod, _set_cod)

p = Autor('Julio','consulta')



