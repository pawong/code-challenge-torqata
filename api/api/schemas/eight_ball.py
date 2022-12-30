from pydantic import BaseModel


class EightBallRequest(BaseModel):
    question: str


class EightBall(EightBallRequest):
    answer: str
