from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from .settings import DataBase


class FilesModels(DataBase):
    __tablename__ = "files"
    id = Column(Integer, primery_key=True)
    file_unique_id = Column(String, unique=True, nullable=False)
    path_to_file = Column(String, nullable=False)
