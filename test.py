import pytest
from card import Card
from desk import Desk
from player import Player
from match import Match

# pytest trong cả 2 trường hợp này định nghĩa một fixture này có thể được sử dụng trong các bài kiểm tra khác nhau, tránh việc phải lặp đi lặp lại các đối tượng giống nhau
@pytest.fixture
def card_1():
    return Card("2", "Club")

@pytest.fixture
def card_2():
    return Card("3", "Spade")

def test_str(card_1):
    assert str(card_1) == "2 of Clubs"

def test_is_greater_than(card_1, card_2):
    assert not card_1.is_greater_than(card_2)
    assert card_2.is_greater_than(card_1)


# Desk
# pytest trong trường hợp fixture desk này được sử dụng trong các bài kiểm tra khác nhau để cung cấp 1 instance của class Desk và thực hiện kiểm tra nó.
@pytest.fixture
def desk():
    return Desk()

def test_pick_card(desk):
    result = desk.pick_card()
    assert isinstance(result["house_card"], Card)
    assert isinstance(result["player_card"], Card)
    assert result["house_card"] != result["player_card"]


# #Match
def test_add_reward():
    match = Match()
    match._reward = 10
    match._wining_reward = 20
    match.add_reward()
    assert match._reward == 30
    assert match._wining_reward == 40

def test_get_reward():
    match = Match()
    match._reward = 100
    assert match.get_reward() == 100



# Player
def test_join_match():
    player = Player()
    player._point = 60
    assert player.join_match() == True
    assert player._point == 35

def test_add_reward():
    player = Player()
    player._point = 60
    player.add_reward(10)
    assert player._point == 70

def test_show_point(capsys):
    player = Player()
    player._point = 60
    player.show_point()
    captured = capsys.readouterr()
    assert captured.out == "You have 60 !\n"
