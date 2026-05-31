import sys
import os

# Tambahkan path BE ke sys.path agar bisa mengimpor app
sys.path.append(r"d:\4. Thoriq_KULIAH\1.Lomba Thoriq\SEMESTER 4\05. Samsung\DyLeks\BE")

try:
    from app.core.database import SessionLocal
    from app.services.adaptive_engine import AdaptiveEngine
    
    db = SessionLocal()
    
    # 1. Tes Pengambilan Soal Adaptif Level 3
    print("\n=== RUNNING TEST 1: get_next_exercises (Level 3) ===")
    exercises = AdaptiveEngine.get_next_exercises(db, child_id="test_child", current_level=3, limit=10)
    
    print(f"Total exercises retrieved: {len(exercises)}")
    for i, ex in enumerate(exercises, 1):
        print(f"  {i}. ID: {ex.id} | Level: {ex.level} | Answer: {ex.correct_answer}")
        
    # Validasi rasio 80/20 secara manual pada sampel
    level_3_count = sum(1 for ex in exercises if ex.level == 3)
    level_lower_count = sum(1 for ex in exercises if ex.level < 3)
    
    print(f"Level 3 (Active) count: {level_3_count} (Target: ~8)")
    print(f"Level 1-2 (Review) count: {level_lower_count} (Target: ~2)")
    
    assert len(exercises) == 10, "Failed: Limit not met"
    assert level_lower_count >= 1, "Failed: Repetition / Spaced Repetition logic did not retrieve lower level questions"
    print("TEST 1 PASSED! Spaced repetition logic is working.")

    # 2. Tes Evaluasi Jawaban Benar
    print("\n=== RUNNING TEST 2: evaluate_answer (Correct Answer) ===")
    sample_ex = exercises[0]
    res_correct = AdaptiveEngine.evaluate_answer(
        db=db,
        exercise_id=sample_ex.id,
        user_answer=sample_ex.correct_answer,
        response_time_ms=1200
    )
    print("Result Correct:", res_correct)
    assert res_correct["is_correct"] is True, "Failed: Correct answer evaluated as wrong"
    print("TEST 2 PASSED!")

    # 3. Tes Evaluasi Jawaban Salah
    print("\n=== RUNNING TEST 3: evaluate_answer (Wrong Answer) ===")
    res_wrong = AdaptiveEngine.evaluate_answer(
        db=db,
        exercise_id=sample_ex.id,
        user_answer="SALAH_EJAAN",
        response_time_ms=2500
    )
    print("Result Wrong:", res_wrong)
    assert res_wrong["is_correct"] is False, "Failed: Wrong answer evaluated as correct"
    print("TEST 3 PASSED!")

    db.close()
    print("\nALL TESTS PASSED SUCCESSFULLY! Adaptive learning services verified.")
    
except Exception as e:
    import traceback
    print("ERROR:")
    traceback.print_exc()
    sys.exit(1)
