from datetime import datetime
class Trabalho():
    def __init__(self, conteudo, nota, dataEntrega, titulo, dataHoraAtualizacao):
        self._conteudo = conteudo
        self._nota = nota
        self._dataEntrega = dataEntrega
        self._titulo = titulo
        self._dataHoraAtualizacao = dataHoraAtualizacao
        self._cod = None
    
    def _get_conteudo(self):
        return self._conteudo
    def _set_conteudo(self, conteudo):
        self._conteudo = conteudo
    def _get_nota(self):
        return self._nota
    def _set_nota(self, nota):
        self._nota = nota
    def _get_titulo(self):
        return self._titulo
    def _set_titulo(self, titulo):
        self._titulo = titulo
    def _get_dataEntrega(self):
        return self._dataEntrega
    def _set_dataEntrega(self, dataEntrega):
        self._dataEntrega = dataEntrega
    def _get_dataHoraAtualizacao(self):
        return self._dataHoraAtualizacao
    def _set_dataHoraAtualizacao(self, dataHoraAtualizacao):
        self._dataHoraAtualizacao = dataHora
    def _get_cod(self):
        return self._cod
    def _set_cod(self, cod):
        self._cod = cod

    conteudo = property( _get_conteudo, _set_conteudo)
    nota = property( _get_nota, _set_nota)
    titulo = property( _get_titulo, _set_titulo)
    dataEntrega = property( _get_dataEntrega, _set_dataEntrega)
    dataHoraAtualizacao = property( _get_dataHoraAtualizacao, _set_dataHoraAtualizacao)
    cod = property( _get_cod, _set_cod)





