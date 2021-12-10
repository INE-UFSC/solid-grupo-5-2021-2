"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

class Database:
    def __init__(self):
        pass
    
    # salva no DB
    def save(self, animal: Animal):
        pass
