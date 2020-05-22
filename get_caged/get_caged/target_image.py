from pydantic import BaseModel


class TargetImageSpec(BaseModel):
    height: int
    width: int

    @property
    def aspect_ratio(self) -> float:
        return self.width / self.height
