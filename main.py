from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import SportType, Athlete, Result
from pydantic import BaseModel, condecimal
from datetime import date
from decimal import Decimal

app = FastAPI()
Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic model for SportType
class SportTypeCreate(BaseModel):
    unit_of_measurement: str
    name: str
    world_record: condecimal(max_digits=10, decimal_places=2)
    olympic_record: condecimal(max_digits=10, decimal_places=2)


class SportTypeResponse(BaseModel):
    id: int
    unit_of_measurement: str
    name: str
    world_record: condecimal(max_digits=10, decimal_places=2)
    olympic_record: condecimal(max_digits=10, decimal_places=2)


class SportTypeDelete(BaseModel):
    message: str


# Pydantic model for Result
class ResultCreate(BaseModel):
    competition_name: str
    performance: int
    place: int
    date: date
    venue: str


class ResultResponse(BaseModel):
    id: int
    competition_name: str
    performance: int
    place: int
    date: date
    venue: str


class ResultDelete(BaseModel):
    message: str


# Pydantic model for Athlete
class AthleteCreate(BaseModel):
    win: int
    full_name: str
    birth_year: int
    country: str


class AthleteResponse(BaseModel):
    id: int
    win: int
    full_name: str
    birth_year: int
    country: str


class AthleteDelete(BaseModel):
    message: str


# Basic CRUD using FastAPI

# Create
@app.post("/sport_types/", response_model=SportTypeResponse)
def create_sport_type(sport_type: SportTypeCreate, db: Session = Depends(get_db)):
    db_sport_type = SportType(**sport_type.dict())
    db.add(db_sport_type)
    db.commit()
    db.refresh(db_sport_type)
    return db_sport_type


@app.post("/results/", response_model=ResultResponse)
def create_result(result: ResultCreate, db: Session = Depends(get_db)):
    db_result = Result(**result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result


@app.post("/athletes/", response_model=AthleteResponse)
def create_athlete(athlete: AthleteCreate, db: Session = Depends(get_db)):
    db_athlete = Athlete(**athlete.dict())
    db.add(db_athlete)
    db.commit()
    db.refresh(db_athlete)
    return db_athlete


# Read
@app.get("/sport_types/{sport_type_id}", response_model=SportTypeResponse)
def get_sport_type(sport_type_id: int, db: Session = Depends(get_db)):
    sport_type = db.query(SportType).filter(SportType.id == sport_type_id).first()
    if sport_type is None:
        raise HTTPException(status_code=404, detail='Sport Type not found')
    return sport_type


@app.get("/athletes/{athlete_id}", response_model=AthleteResponse)
def get_athlete(athlete_id: int, db: Session = Depends(get_db)):
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if athlete is None:
        raise HTTPException(status_code=404, detail='Athlete not found')
    return athlete


@app.get("/results/{result_id}", response_model=ResultResponse)
def get_result(result_id: int, db: Session = Depends(get_db)):
    results = db.query(Result).filter(Result.id == result_id).first()
    if results is None:
        raise HTTPException(status_code=404, detail='Result not found')
    return results


# Update
@app.put("/sport_types/{sport_type_id}", response_model=SportTypeResponse)
def update_sport_type(sport_type_id: int, updated: SportTypeCreate, db: Session = Depends(get_db)):
    sport_type = db.query(SportType).filter(SportType.id == sport_type_id).first()
    if sport_type is None:
        raise HTTPException(status_code=404, detail='Sport type not found')

    for key, value in updated.dict().items():
        setattr(sport_type, key, value)

    db.commit()
    db.refresh(sport_type)
    return sport_type


@app.put("/results/{result_id}", response_model=ResultResponse)
def update_result(result_id: int, updated: ResultCreate, db: Session = Depends(get_db)):
    result = db.query(Result).filter(Result.id == result_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail='Result not found')

    for key, value in updated.dict().items():
        setattr(result, key, value)

    db.commit()
    db.refresh(result)
    return result


@app.put("/athletes/{athlete_id}", response_model=AthleteResponse)
def update_athlete(athlete_id: int, updated: AthleteCreate, db: Session = Depends(get_db)):
    athlete = db.query(Athlete).filter(athlete_id == Athlete.id).first()
    if athlete is None:
        raise HTTPException(status_code=404, detail="Athlete not found")

    for key, value in updated.dict().items():
        setattr(athlete, key, value)

    db.commit()
    db.refresh(athlete)
    return athlete


# Delete
@app.delete("/sport_types/{sport_id}", response_model=SportTypeDelete)
def delete_sport(sport_type_id: int, db: Session = Depends(get_db)):
    sport_type = db.query(SportType).filter(SportType.id == sport_type_id).first()
    if sport_type is None:
        raise HTTPException(status_code=404, detail="SportType not found")

    db.delete(sport_type)
    db.commit()
    return {"message": "SportType deleted"}


@app.delete("/results/{result_id}", response_model=ResultDelete)
def delete_result(result_id: int, db: Session = Depends(get_db)):
    result = db.query(Result).filter(Result.id == result_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Result not found")

    db.delete(result)
    db.commit()
    return {"message": "Result deleted"}


@app.delete("/athletes/{athlete_id}", response_model=AthleteDelete)
def delete_athlete(athlete_id: int, db: Session = Depends(get_db)):
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if athlete is None:
        raise HTTPException(status_code=404, detail="Athlete not found")

    db.delete(athlete)
    db.commit()
    return {"message": "Athlete deleted"}
