import fastapi
from bd.db import Base, engine
from routers.events import event_route

Base.metadata.create_all(bind=engine)

app = fastapi.FastAPI()

app.include_router(event_route())