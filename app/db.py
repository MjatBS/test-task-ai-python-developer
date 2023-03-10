from .models import CameraOrm


class Engine:
    def create_or_get(self, model):
        return CameraOrm(id=3, uuid=model.uuid)
