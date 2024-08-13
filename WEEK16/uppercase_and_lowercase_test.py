from uppercase_and_lowercase import sum_of_letter_case


def test_sum_of_letter_case():
    word = 'Hola Mundo'
    result = sum_of_letter_case(word)
    assert result == (7,2)