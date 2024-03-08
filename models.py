from datetime import datetime

from sqlalchemy import Integer, String, \
    Column, ForeignKey, Table, Text, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# Список инженеров
class Engineers(Base):
    __tablename__ = 'engineers'

    id = Column(Integer, primary_key=True)
    fio = Column(String(255))
    UUID = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)

    tasks = relationship("MaintenanceTask", back_populates="engineers")

    def __repr__(self):
        return f"<Engineers(fio={self.fio}, UUID={self.UUID})>"


# Регламентные работы
class MaintenanceTask(Base):
    __tablename__ = 'maintenance_task'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(Text)
    engineer_id = Column(Integer, ForeignKey('engineers.id'))
    product_id = Column(Integer, ForeignKey('product_passport.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    engineers = relationship("Engineers", back_populates="tasks")
    product = relationship("ProductPassport", back_populates="maintenances")

    def __repr__(self):
        return f"<MaintenanceTask(title={self.title}, engineer_id={self.engineer_id})>"


# Паспорт изделия
class ProductPassport(Base):
    __tablename__ = 'product_passport'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    series_id = Column(Integer, ForeignKey('series.id'))
    produced_at = Column(DateTime)
    sold_at = Column(DateTime)

    maintenances = relationship("MaintenanceTask", back_populates="product")
    series = relationship("Series", back_populates="product")

    def __repr__(self):
        return f"<ProductPassport(number={self.number}, engineer_id={self.engineer_id})>"


# Регламентные работы
class Series(Base):
    __tablename__ = 'series'

    id = Column(Integer, primary_key=True)
    number = Column(String(255))

    product = relationship("ProductPassport", back_populates="series")

    def __repr__(self):
        return f"<RoutineMaintenance(number={self.number})>"
