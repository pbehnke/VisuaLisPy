from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session
# from sqlalchemy.orm import sessionmaker, scoped_session
import os

# exp = os.environ.get("DATABASE_URL", "postgres://localhost/programs")
# engine = create_engine(exp, echo=False)
engine = create_engine("sqlite:///code.db", echo=False)
s = scoped_session(sessionmaker(
                                bind=engine,
                                autocommit = False,
                                autoflush = False))
Base = declarative_base()
Base.query = s.query_property()

### Class declarations go here
class Code(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    code = Column(String(64))
    # language = Column(String(64))
    description = Column(String(64), nullable=True)
    
    # FIXME: broken currently b/c language doesn't exist

    # users will access saved code via url/id

    # s.query(Code).filter_by(id=1).one()
    # s.query(Code).filter_by(name='area').one()

### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()

