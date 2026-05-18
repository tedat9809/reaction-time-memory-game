import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import calculate_average
from main import check_memory_answer
from main import generate_sequence
from main import check_stroop_answer



def test_generate_sequence_length():
    sequence = generate_sequence(5)
    assert len(sequence) == 5


def test_generate_sequence_type():
    sequence = generate_sequence(4)
    assert isinstance(sequence, list)


def test_generate_sequence_elements_are_strings():
    sequence = generate_sequence(3)
    for item in sequence:
        assert isinstance(item, str)


def test_generate_sequence_elements_are_digits():
    sequence = generate_sequence(10)
    for item in sequence:
        assert item.isdigit()


def test_generate_sequence_zero_length():
    sequence = generate_sequence(0)
    assert sequence == []


def test_calculate_average_regular_values():
    assert calculate_average([1.0, 2.0, 3.0]) == 2.0


def test_calculate_average_empty_list():
    assert calculate_average([]) == 0.0


def test_check_memory_answer_correct():
    assert check_memory_answer("1 2 3", ["1", "2", "3"]) is True


def test_check_memory_answer_incorrect():
    assert check_memory_answer("1 2 4", ["1", "2", "3"]) is False

def test_check_stroop_answer_correct():
    assert check_stroop_answer("red", "red") is True


def test_check_stroop_answer_correct_with_spaces_and_caps():
    assert check_stroop_answer(" RED ", "red") is True


def test_check_stroop_answer_incorrect():
    assert check_stroop_answer("blue", "red") is False