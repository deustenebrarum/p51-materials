from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, create_engine, delete, select, func
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


engine = create_engine("postgresql://postgres:admin@localhost/p51_users_test")


def main():
    with Session(engine) as session:
        # jim = session.get(User, 2)
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

        # for user in session.scalars(
        #         select(func.count(User.name)).where(User.name == "jim")):
        #     print(user)
        session.delete(delete(User).where(User.name == "jim"))
        session.commit()
        for res in session.scalars(
                select(User).where(User.name == "jim")):
            print(res)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


if __name__ == "__main__":
    main()
