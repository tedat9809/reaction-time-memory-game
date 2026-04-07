from main import generate_sequence


def test_generate_sequence_length():
    sequence = generate_sequence(5)
    assert len(sequence) == 5


def test_generate_sequence_type():
    sequence = generate_sequence(4)
    assert isinstance(sequence, list)


def test_generate_sequence_elements():
    sequence = generate_sequence(3)
    for item in sequence:
        assert isinstance(item, str)
        