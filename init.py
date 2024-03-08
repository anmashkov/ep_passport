from sqlalchemy.orm import Session

from models import Engineers, ProductPassport, Series, MaintenanceTask

import uuid

engineers = [
    "Иванов Иван Иванович",
    "Петров Петр Петрович",
    "Сидоров Сергей Александрович",
    "Козлова Екатерина Дмитриевна"
]

series = [
    "A123",
    "B456",
    "C789",
    "F1415",
    "H1819",
    "I2021",
]

products = [
    {"number": 1, "series": "A123", "produced_at": "2022-01-05", "sold_at": "2022-01-10"},
    {"number": 2, "series": "B456", "produced_at": "2022-01-07", "sold_at": "2022-01-12"},
    {"number": 3, "series": "C789", "produced_at": "2022-01-09", "sold_at": "2022-01-14"},
    {"number": 4, "series": "A123", "produced_at": "2022-01-11", "sold_at": "2022-01-16"},
    {"number": 5, "series": "C789", "produced_at": "2022-01-13", "sold_at": "2022-01-18"},
    {"number": 6, "series": "F1415", "produced_at": "2022-01-15", "sold_at": "2022-01-20"},
    {"number": 7, "series": "A123", "produced_at": "2022-01-17", "sold_at": "2022-01-22"},
    {"number": 8, "series": "H1819", "produced_at": "2022-01-19", "sold_at": "2022-01-24"},
    {"number": 9, "series": "I2021", "produced_at": "2022-01-21", "sold_at": "2022-01-26"},
    {"number": 10, "series": "C789", "produced_at": "2022-01-23", "sold_at": "2022-01-28"}
]

maintenance_tasks = [
    {
        "title": "Проверка смазки",
        "content": "Проверить уровень и качество смазки, дозаполнить при необходимости.",
        "product_number": 1,
        "engineer": "Иванов Иван Иванович"
    },
    {
        "title": "Очистка фильтров",
        "content": "Очистить и промыть фильтры от загрязнений.",
        "product_number": 2,
        "engineer": "Сидоров Сергей Александрович"
    },
    {
        "title": "Проверка зазоров",
        "content": "Проверить и отрегулировать зазоры в механизмах.",
        "product_number": 3,
        "engineer": "Иванов Иван Иванович"
    },
    {
        "title": "Проверка электрических соединений",
        "content": "Проверить состояние и качество электрических соединений.",
        "product_number": 3,
        "engineer": "Сидоров Сергей Александрович"
    },
    {
        "title": "Тестирование функционала",
        "content": "Провести тестирование работоспособности и функционала изделия.",
        "product_number": 4,
        "engineer": "Козлова Екатерина Дмитриевна"
    }
]


class DatabaseInitiator:

    def __init__(self, base, engine):
        self.engine = engine
        self.base = base

    def create_tables(self):
        self.base.metadata.drop_all(self.engine)
        self.base.metadata.create_all(self.engine)
        self.init_engineers()
        self.init_series()
        self.init_products()
        self.init_maintenance_tasks()

    def init_engineers(self):
        with Session(self.engine) as session:
            for engineer in engineers:
                en = Engineers(fio=engineer, UUID=str(uuid.uuid4()))
                session.add(en)

            session.commit()

    def init_series(self):
        with Session(self.engine) as session:
            for ser in series:
                s = Series(number=ser)
                session.add(s)

            session.commit()

    def init_products(self):
        with Session(self.engine) as session:
            for product in products:
                pp = ProductPassport(
                    number=product['number'],
                    produced_at=product['produced_at'],
                    sold_at=product['sold_at'],
                    series=session.query(Series).filter(Series.number == product['series']).first()
                )
                session.add(pp)

            session.commit()

    def init_maintenance_tasks(self):
        with Session(self.engine) as session:
            for task in maintenance_tasks:
                mt = MaintenanceTask(
                    title=task['title'],
                    content=task['content'],
                    engineers=session.query(Engineers).filter(Engineers.fio == task['engineer']).first(),
                    product=session.query(ProductPassport).filter(ProductPassport.id == task['product_number']).first()
                )

                session.add(mt)

            session.commit()

