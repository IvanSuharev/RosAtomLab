from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from bd.db import get_db
from models.event import Event

event_route = APIRouter(
    prefix="/event",
    tags=['events']
)


@event_route.get('/<event_id>')
async def get_event_by_id(event_id: int, db: Session = Depends(get_db())):
    event = db.query(Event).get(event_id)
    return event
