from sqlalchemy import Column,String,BigInteger,Text,Boolean,ForeignKey,DateTime
from Database.database import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

# Table to keep users information
class UserModels(Base):
    __tablename__ = 'users'
    id =Column(BigInteger,primary_key=True,autoincrement=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    email = Column(String,nullable=False)


# Table to keep question asked in quiz
class QuestionModels(Base):
    __tablename__ = 'questions'
    id =Column(BigInteger,primary_key=True,autoincrement=True)
    question = Column(Text,nullable=False)
    options = relationship("QuestionOptionsModels",primaryjoin="QuestionModels.id ==QuestionOptionsModels.question_id",lazy='joined',order_by="QuestionOptionsModels.id")

# Table to store question options
class QuestionOptionsModels(Base):
    __tablename__ = 'question_options'
    id =Column(BigInteger,primary_key=True,autoincrement=True)
    question_id =Column(BigInteger,ForeignKey(QuestionModels.id),nullable=False)
    option_text = Column(String,nullable=False)
    is_correct = Column(Boolean,nullable=False,default=False)



class  UserResponseModels(Base):
    __tablename__ = 'user_response'
    id =Column(BigInteger,primary_key=True,autoincrement=True)
    question_id =Column(BigInteger,ForeignKey(QuestionModels.id),nullable=False)
    option_id = Column(BigInteger,ForeignKey(QuestionOptionsModels.id),nullable=False)
    user_id = Column(BigInteger,ForeignKey(UserModels.id),nullable=False)
    created_date =Column(DateTime,default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)

