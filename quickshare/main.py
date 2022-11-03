from fastapi import FastAPI

from quickshare.routes.routes import route

from .settings import create_db

app = FastAPI(on_startup=create_db())
app.include_router(route)


def run():
    return app
