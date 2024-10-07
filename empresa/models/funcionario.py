from enums.tipo_funcionario import TipoFuncionario
from enums.estado import EstadoFuncionario
from exceptions.funcionario_exceptions import FuncionarioInvalidoException, FuncionarioNaoEncontradoException
from models.endereco import Endereco

class Funcionario:
    def __init__(self, nome, tipo, endereco: Endereco):
        if not nome or not isinstance(tipo, TipoFuncionario):
            raise FuncionarioInvalidoException("Nome e tipo de funcionário são obrigatórios.")
        
        self.nome = nome
        self.tipo = tipo
        self.endereco = endereco
        self.estado = EstadoFuncionario.ATIVO

    def desativar(self):
        self.estado = EstadoFuncionario.INATIVO
