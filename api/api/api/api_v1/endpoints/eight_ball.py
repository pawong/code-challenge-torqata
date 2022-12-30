import random

from typing import Any

from api import schemas

from fastapi import APIRouter, Body, HTTPException, Request
from fastapi.encoders import jsonable_encoder


router = APIRouter()

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

@router.get('')
def get_answer_only():
    """8ball get answer only endpoint"""
    return answers[random.randint(0, len(answers)-1)]

@router.post('', response_model=schemas.EightBall)
def get_answer(question_in: schemas.EightBallRequest):
    """8ball post answer endpoint"""
    question = question_in.question
    if question is None or not len(question):
        raise HTTPException(
            status_code=400,
            detail="Invalid formed question",
        )
    return {
        "answer": answers[random.randint(0, len(answers)-1)],
        "question": question
    }
