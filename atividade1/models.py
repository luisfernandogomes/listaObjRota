from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, Boolean, DateTime, Float, Date, func
# em baixo importamos session(gerenciar)  e sessiomaker(construir)
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship
from datetime import date
from dateutil.relativedelta import relativedelta

engine = create_engine('sqlite:///Pessoas')
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    profissao = Column(String, nullable=False)
    salario = Column(Float, nullable=False)

    def __repr__(self):
        return'<usuario {},{},{}>'.format(self.nome, self.profissao, self.salario)
    def save(self):
        db_session.add(self)
        db_session.commit()
    def get_user(self):
        dados_usuario = {
            'id': self.id,
            'nome': self.nome,
            'profissao': self.profissao,
            'salario': self.salario
        }
        return dados_usuario

def init_db():
    Base.metadata.create_all(bind=engine)
if __name__ == '__main__':
    init_db()