from fastapi import FastAPI, Form, HTTPException

from .models import NewCamera, Camera, CameraOrm
from .db import Engine


app = FastAPI()

engine = Engine()


@app.post("/api/v1/camera")
def create_camera(uuid: str = Form()) -> Camera:
    camera = CameraOrm(uuid=uuid)

    try:
        camera = engine.create_or_get(camera)
    except:
        raise HTTPException(status_code=500, detail="Error database connection. Camera not created")

    return Camera.from_orm(camera)
