from pydantic import BaseModel, Field


class ResponseSuccessfully(BaseModel):
    successfully: bool = Field(default=True)

    class Config:
        schema_extra = {
            "example": {
                "successfully": True
            }
        }


__all__ = [
    "ResponseSuccessfully"
]
