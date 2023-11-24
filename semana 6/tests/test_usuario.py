import nim_game as nim

def test_user():
    assert nim.usuario_escolhe_jogada (5,  3, 2) == 3