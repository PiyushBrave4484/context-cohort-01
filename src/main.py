from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.models import (
    UserCreate,
    SubscriptionCreate,
    MagazineCreate,
    PlanCreate,
    User,
    Magazine,
    Plan,
    Subscription,
)
from src.database import engine, Base
from src.dependencies import get_db
from src.auth import create_user, authenticate_user

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/register", response_model=UserCreate)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user


@app.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    return {"message": "Login successful"}


@app.post("/magazines", response_model=MagazineCreate)
def create_magazine(magazine: MagazineCreate, db: Session = Depends(get_db)):
    db_magazine = Magazine(**magazine.dict())
    db.add(db_magazine)
    db.commit()
    db.refresh(db_magazine)
    return db_magazine


@app.get("/magazines", response_model=List[MagazineCreate])
def get_magazines(db: Session = Depends(get_db)):
    return db.query(Magazine).all()


@app.post("/subscriptions", response_model=SubscriptionCreate)
def create_subscription(
    subscription: SubscriptionCreate, db: Session = Depends(get_db)
):
    db_subscription = Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


@app.get("/subscriptions/{user_id}", response_model=List[SubscriptionCreate])
def get_user_subscriptions(user_id: int, db: Session = Depends(get_db)):
    return (
        db.query(Subscription)
        .filter(Subscription.user_id == user_id, Subscription.is_active == True)
        .all()
    )


@app.put("/subscriptions/{subscription_id}", response_model=SubscriptionCreate)
def update_subscription(
    subscription_id: int,
    new_subscription: SubscriptionCreate,
    db: Session = Depends(get_db),
):
    db_subscription = (
        db.query(Subscription)
        .filter(Subscription.id == subscription_id, Subscription.is_active == True)
        .first()
    )
    if db_subscription:
        db_subscription.is_active = False
        db.commit()
        db.refresh(db_subscription)
        new_subscription_data = new_subscription.dict()
        new_subscription_data["price"] = db_subscription.price
        new_subscription_data["is_active"] = True
        new_subscription_instance = Subscription(**new_subscription_data)
        db.add(new_subscription_instance)
        db.commit()
        db.refresh(new_subscription_instance)
        return new_subscription_instance
    else:
        raise HTTPException(status_code=404, detail="Subscription not found")


@app.delete("/subscriptions/{subscription_id}")
def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = (
        db.query(Subscription)
        .filter(Subscription.id == subscription_id, Subscription.is_active == True)
        .first()
    )
    if db_subscription:
        db_subscription.is_active = False
        db.commit()
        return {"message": "Subscription canceled"}
    else:
        raise HTTPException(status_code=404, detail="Subscription not found")
