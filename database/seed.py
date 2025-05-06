from faker import Faker
import random
from database.db import SessionLocal, create_bank
from database.models import Vehicle
from faker_vehicle import VehicleProvider

faker = Faker('pt_BR')
faker.add_provider(VehicleProvider)

def generate_vehicle():
    return Vehicle(
        marca=faker.vehicle_make(),
        modelo=faker.vehicle_model(),
        ano=random.randint(1998, 2024),
        motorizacao=random.choice([
            '1.0', '1.2', '1.4', '1.6', '1.8', '2.0', '2.2', '2.5', '3.0',
            'V6', 'V8', 'Eletrico', 'Hibrido'
        ]),
        combustivel=random.choice([
            'Gasolina', 'Etanol', 'Flex', 'Diesel', 'GNV', 'Eletrico', 'Híbrido',
            'Flex/GNV', 'Diesel/Eletrico'
        ]),
        cor=faker.color_name(),
        quilometragem=random.randint(1000, 350000),
        portas=random.choice([2, 3, 4, 5]),
        transmissao=random.choice([
            'Manual', 'Automatica', 'Automatizada', 'CVT', 'DSG', 'Tiptronic'
        ]),
        preco=round(random.uniform(8000, 300000), 2)
    )

def popular_bank():
    create_bank()
    session = SessionLocal()
    session.query(Vehicle).delete()
    for _ in range(500):
        session.add(generate_vehicle())
    session.commit()
    session.close()
    print("Banco populado com sucesso.")
