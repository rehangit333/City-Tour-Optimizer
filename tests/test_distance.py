from distance import haversine_distance

def test_distance():
    d = haversine_distance((48.8584, 2.2945), (48.8606, 2.3376))
    assert round(d, 1) == 3.2  # Eiffel Tower to Louvre Museum
