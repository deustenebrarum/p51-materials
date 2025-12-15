from typing import List
from typing import Optional
from sqlalchemy import create_engine, ForeignKey, delete, select, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session, sessionmaker


engine = create_engine(
    "postgresql://postgres:admin@localhost/p51_users_test")

create_session = sessionmaker(bind=engine)


def main():
    with create_session() as session:
        Base.metadata.create_all(engine)
        print(delete(User))
        # session.execute()

        session.commit()

        # sandy = session.get(User, 4)
        # session.add_all([
        #     Address(email_address=f"jim-{i}@example.com", user=jim)
        #     for i in range(6)
        # ])
        # session.add_all([
        #     Address(email_address=f"sandy-{i}@example.com", user=sandy)
        #     for i in range(3)
        # ])
        # session.commit()
        Address().user
        # for user in session.scalars(
        #         select(func.count(User.name)).where(User.name == "jim")):
        #     print(user)
        # session.commit()
        # for res in session.scalars(
        #         select(User).where(User.name == "jim")):
        #     print(res)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    '''
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL,
        fullname VARCHAR(255),
    )
    '''
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(255), unique=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(255))
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "addresses"
    email_address: Mapped[str]
    # user_id INTEGER REFERENCES users(id)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


if __name__ == "__main__":
    main()
