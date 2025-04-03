from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    assert abs(text_to_duration("10:20") - 10.33333333333333) < 1e-5

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

test_text_to_duration_float()
test_text_to_duration_integer()