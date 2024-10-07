import unittest
from models.funcionario import Funcionario
from models.endereco import Endereco
from enums.tipo_funcionario import TipoFuncionario
from exceptions.funcionario_exceptions import FuncionarioInvalidoException

class TestFuncionario(unittest.TestCase):
    def setUp(self):
        self.endereco = Endereco("Rua das Flores", 123, "São Paulo", "SP")

    def test_criar_funcionario_valido(self):
        funcionario = Funcionario("João da Silva", TipoFuncionario.ADMINISTRATIVO, self.endereco)
        self.assertEqual(funcionario.nome, "João da Silva")
        self.assertEqual(funcionario.tipo, TipoFuncionario.ADMINISTRATIVO)

    def test_criar_funcionario_sem_nome(self):
        with self.assertRaises(FuncionarioInvalidoException):
            Funcionario("", TipoFuncionario.ADMINISTRATIVO, self.endereco)

    def test_criar_funcionario_sem_tipo(self):
        with self.assertRaises(FuncionarioInvalidoException):
            Funcionario("João da Silva", None, self.endereco)

    def test_desativar_funcionario(self):
        funcionario = Funcionario("João da Silva", TipoFuncionario.ADMINISTRATIVO, self.endereco)
        funcionario.desativar()
        self.assertEqual(funcionario.estado.value, "Inativo")

if __name__ == "__main__":
    unittest.main()
