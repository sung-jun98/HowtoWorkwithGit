from utility import add, substract, multiply, divdie

def test_add() -> None:
    alpha, beta = 1, 2
    result = add(alpha + beta)
    assert alpha + beta == result ," Error:function 'add'"