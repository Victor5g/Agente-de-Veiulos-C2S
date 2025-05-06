from database.db import SessionLocal
from database.models import Vehicle
from sqlalchemy.inspection import inspect
from sqlalchemy import and_

def search_vehicles(filters):
    session = SessionLocal()
    query = session.query(Vehicle)

    conditions = []
    for key, value in filters.items():
        column = getattr(Vehicle, key, None)
        if column is not None and value is not None:
            if isinstance(value, str):
                conditions.append(column.ilike(f"%{value}%"))
            else:
                conditions.append(column == value)

    if conditions:
        query = query.filter(and_(*conditions))

    results = query.all()

    vehicles = [
        {
            column.key: getattr(v, column.key)
            for column in v.__table__.columns
        } for v in results
    ]

    session.close()
    return vehicles

def get_available_filters():
    filters = {}
    columns = inspect(Vehicle).c

    for column in columns:
        key = column.key
        filters[key] = key.capitalize().replace('_', ' ')

    return filters