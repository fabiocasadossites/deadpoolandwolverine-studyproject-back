from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class Shorts:
    __tablename__ = 'shorts'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    link: Mapped[str]
    status: Mapped[str]
    dateCad: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    dateUp: Mapped[str]
    token: Mapped[str]


@table_registry.mapped_as_dataclass
class Characters:
    __tablename__ = 'characters'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    status: Mapped[str]
    dateCad: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    dateUp: Mapped[str]
    token: Mapped[str]


@table_registry.mapped_as_dataclass
class Gallery:
    __tablename__ = 'gallery'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    img: Mapped[str]
    status: Mapped[str]
    characters: Mapped[list['Characters']] = relationship(
        init=False, back_populates='gallery', cascade='all, delete-orphan'
    )


@table_registry.mapped_as_dataclass
class Client:
    __tablename__ = 'client'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    cep: Mapped[str]
    number: Mapped[str]
    address: Mapped[str]
    complement: Mapped[str]
    uf: Mapped[str]
    state: Mapped[str]
    dateCad: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    dateUp: Mapped[str]
    token: Mapped[str]


@table_registry.mapped_as_dataclass
class Product:
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    img: Mapped[str]
    amount: Mapped[str]
    price: Mapped[str]
    status: Mapped[str]
    dateCad: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    dateUp: Mapped[str]
    token: Mapped[str]


@table_registry.mapped_as_dataclass
class Profile:
    __tablename__ = 'profile'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    status: Mapped[str]
    dateCad: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    dateUp: Mapped[str]
    token: Mapped[str]


@table_registry.mapped_as_dataclass
class Email:
    __tablename__ = 'email'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    id_sale: Mapped[str]
    tipe: Mapped[str]
    status: Mapped[str]
    dateCad: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    dateShooting: Mapped[str]
    token: Mapped[str]


@table_registry.mapped_as_dataclass
class Sale:
    __tablename__ = 'sale'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    id_client: Mapped[str]
    id_product: Mapped[str]
    amount: Mapped[str]
    priceUnit: Mapped[str]
    priceFull: Mapped[str]
    address: Mapped[str]
    amountTipe: Mapped[str]
    pix_qrcode: Mapped[str]
    pix_copia: Mapped[str]
    status: Mapped[str]
    returnPag: Mapped[str]
    dateCad: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    dateUp: Mapped[str]
    token: Mapped[str]
