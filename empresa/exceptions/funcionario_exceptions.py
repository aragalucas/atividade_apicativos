class FuncionarioException(Exception):
    """Base class for exceptions in this module."""
    pass

class FuncionarioInvalidoException(FuncionarioException):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class FuncionarioNaoEncontradoException(FuncionarioException):
    def __init__(self, nome):
        super().__init__(f"Funcionário '{nome}' não encontrado.")
