from models.funcionario import Funcionario
from models.endereco import Endereco
from enums.tipo_funcionario import TipoFuncionario

def main():
    endereco = Endereco("Rua das Flores", 123, "São Paulo", "SP")
    
    try:
        funcionario = Funcionario("João da Silva", TipoFuncionario.ADMINISTRATIVO, endereco)
        print(f"Funcionário criado: {funcionario.nome}, Tipo: {funcionario.tipo.value}, Endereço: {funcionario.endereco}")
        
        funcionario.desativar()
        print(f"Funcionário {funcionario.nome} desativado, estado: {funcionario.estado.value}")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
