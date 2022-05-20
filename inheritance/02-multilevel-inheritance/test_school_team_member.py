import pytest
from school_team_member import Player
from sports import Sports


# A unit Test
def test_player_class_exists():
    try:
        _ = Player(sports=Sports.cricket, roll_no="123", course_name="Python", name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_non_sports_value_sports_in_constructor():
    with pytest.raises(ValueError):
        _ = Player(sports="Cricket",roll_no=1, course_name="Python", name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
        assert False
    assert True


# A unit Test
def test_player_object_creation_with_correct_arguments_in_constructor():
    _ = Player(sports=Sports.basket_ball, roll_no="123", course_name="Python", name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
    assert True


# A unit Test
def test_player_object_creation_with_correct_values():
    player = Player(sports=Sports.hockey, roll_no="123", course_name="Python", name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
    assert player.name == "John" and player.gender == "Male" \
           and player.address == "13 Mall Road, QLD" and player.contact_number == "12345678"\
           and player.email == "john@sample.com" and player.roll_number == "123" \
           and player.course_name == "Python" and player.sports == Sports.hockey
