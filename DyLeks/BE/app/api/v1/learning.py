"""
Learning API Router.
Menangani alur pengambilan soal latihan adaptif (Orton-Gillingham)
dan pengolahan skor sesi secara luring.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.exercise_schema import ExerciseResponse, SubmitAnswerRequest
from app.services.adaptive_engine import AdaptiveEngine
from typing import List

router = APIRouter()

@router.get("/get-exercises/{level}", response_model=List[ExerciseResponse])
def get_exercises_by_level(level: int, db: Session = Depends(get_db)):
    """
    Mengambil daftar soal luring adaptif berdasarkan level anak (80% level aktif, 20% level dasar).
    """
    # Menggunakan dummy child_id untuk mode luring anonim
    exercises = AdaptiveEngine.get_next_exercises(db, child_id="anon_child", current_level=level, limit=10)
    return exercises

@router.post("/submit-answer")
def submit_answer(payload: SubmitAnswerRequest, db: Session = Depends(get_db)):
    """
    Menerima respons jawaban anak dan menilai ketepatan secara luring via AdaptiveEngine.
    """
    # Mengevaluasi jawaban anak, session_id dilewatkan None dalam mode anonim
    result = AdaptiveEngine.evaluate_answer(
        db=db,
        exercise_id=payload.exercise_id,
        user_answer=payload.answer,
        response_time_ms=payload.response_time_ms
    )
    
    if result["status"] == "error":
        raise HTTPException(status_code=404, detail=result["message"])
        
    return {
        "is_correct": result["is_correct"],
        "correct_answer": result["correct_answer"] if not result["is_correct"] else None,
        "feedback": result["feedback"]
    }