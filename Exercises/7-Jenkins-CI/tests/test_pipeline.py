def test_pipeline_message():
    message = "Jenkins CI Pipeline Started"
    assert "Jenkins" in message
    assert "CI" in message

def test_exercise_number():
    exercise = 7
    assert exercise == 7
