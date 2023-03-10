from typing import Union
from pydantic import BaseModel, constr
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


UUID_LEN = 36

class NewCamera(BaseModel):
    uuid: constr(max_length=UUID_LEN)


class Camera(BaseModel):
    id: int
    uuid: constr(max_length=UUID_LEN)

    class Config:
        orm_mode = True


Base = declarative_base()

class CameraOrm(Base):
    __tablename__ = "Cameras"
    id = Column(Integer, primary_key=True, nullable=False)
    uuid = Column(String(UUID_LEN))
