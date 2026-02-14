# app/models.py

from sqlalchemy import Column, Integer, String, Text
from .database import Base, engine  # import engine from database.py

class User(Base):
    __tablename__ = "register"  # match your PostgreSQL table

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    sign_level = Column(String(50), nullable=False)  # Basic, Intermediate, Advance
    name = Column(String(100), nullable=False)
    image = Column(String(500), nullable=False)  # URL or path to image
    heading = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)  # Can be longer text with multiple steps


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    level = Column(String(50), nullable=False)  # Beginner, Intermediate, Advance
    # Question text/image are optional so that a quiz can be image-only or text-only
    question_text = Column(Text, nullable=True)
    question_image = Column(String(500), nullable=True)

    option1_text = Column(String(255), nullable=True)
    option2_text = Column(String(255), nullable=True)
    option3_text = Column(String(255), nullable=True)
    option4_text = Column(String(255), nullable=True)

    option1_image = Column(String(500), nullable=True)
    option2_image = Column(String(500), nullable=True)
    option3_image = Column(String(500), nullable=True)
    option4_image = Column(String(500), nullable=True)

    correct_option = Column(Integer, nullable=False)  # 1–4


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)


# Correct way to create tables
Base.metadata.create_all(bind=engine)
