from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from unidecode import unidecode



from  model import Base, Contrato
class Cliente(Base):

    """
        Adiciona um novo cliente à base.

        Arguments:
            id_cliente: campo de auto incremento gerado pelo banco.
            nome: número do cliente
            cnpj: cnpj do cliente
            localizacao: endereço comṕleto do cliente
            criado_em: data em que o registro foi adicionado à base (geração automática)
            atualizado_em: data em que o registro foi alterado na base (geração automática)
        """

    __tablename__ = 'cli_cliente'
    id_cliente = Column(Integer, primary_key = True, index= True)
    nome = Column(String(254))
    cnpj = Column(String(15), unique=True)
    localizacao = Column(String(254))
    created_on =  Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())

    #Cria o relacionamento entre contrato e cliente com cascade delete nos contratos
    contratos = relationship("Contrato", back_populates="cliente", cascade="all, delete", passive_deletes=True,)


    def __init__(self, nome, cnpj, localizacao):
        self.nome = nome
        self.cnpj = cnpj
        self.localizacao = localizacao
        