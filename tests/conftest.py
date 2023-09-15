import pytest
from utils import import_csv_data


@pytest.fixture
def item_test():
    x = import_csv_data('csv_data_110_.csv', 15)
    return x


@pytest.fixture
def item_test2():
    x = [['product1', 57957], ['product6', 61774], ['product4', 39249], ['product8', 52434], ['product3', 71536], ['product5', 43801], ['product11', 68456], ['product2', 22600], ['self', 63850], ['product10', 64975], ['product9', 75156], ['product7', 73667]]
    return x



