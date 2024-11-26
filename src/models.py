from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import declarative_base  # Updated import

Base = declarative_base()


class Magazine(Base):
    __tablename__ = "magazines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    base_price = Column(Float, nullable=False)


class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    renewal_period = Column(Integer, nullable=True)
    discount = Column(Float, nullable=False)
    tier = Column(Integer, nullable=False)


class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    magazine_id = Column(Integer, ForeignKey("magazines.id"))
    plan_id = Column(Integer, ForeignKey("plans.id"))
    price = Column(Float, nullable=False)
    renewal_date = Column(Date)
    is_active = Column(Boolean, default=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)


class UserCreate(BaseModel):
    username: str
    password: str
    email: str


class UserInDB(UserCreate):
    id: int
    hashed_password: str


class MagazineCreate(BaseModel):
    name: str
    description: str
    base_price: float = Field(gt=0)


class PlanCreate(BaseModel):
    title: str
    description: str
    renewal_period: int = Field(gt=0)
    discount: float = Field(ge=0, le=1)
    tier: int


class SubscriptionCreate(BaseModel):
    user_id: int
    magazine_id: int
    plan_id: int
    renewal_date: date


class SubscriptionInDB(SubscriptionCreate):
    id: int
    price: float
    is_active: bool = True
