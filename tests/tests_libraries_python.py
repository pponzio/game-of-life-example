

def test_join_python():
    l = ['o', 'o', 'o']
    assert '|'.join(l) == 'o|o|o'


def test_split_python():
    str = 'o|o|o'
    assert str.split('|') == ['o', 'o', 'o']