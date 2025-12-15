from sqlalchemy import (
    create_engine,
    insert,
    select
)
from sqlalchemy.orm import sessionmaker

from models import Product

engine = create_engine(
    'postgresql://postgres:admin@localhost/p51_products_test')

create_session = sessionmaker(bind=engine)

with create_session() as session:
    session.execute(
        insert(Product).values(name='Laptop', price=1000, quantity=5)
    )
    p = Product(name='Phone', price=500, quantity=10)
    session.add(p)
    print(p.id)
    # session.commit()
    print(*[
        f'{item.id}: {item.name}'
        for item in session.scalars(
            select(Product)
        )
    ], sep='\n')
