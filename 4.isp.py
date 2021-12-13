"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC

class IJanela(ABC):

    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoVariavel(IJanela):

    def minimizar(self):
        raise NotImplementedError

    def maximizar(self):
        raise NotImplementedError

    def mostrar_menu(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanela):

    def mostrar_menu(self):
        raise NotImplementedError

class JanelaSemMenu(IJanela):

    def maximizar(self):
        raise NotImplementedError

    def minimizar(self):
        raise NotImplementedError
