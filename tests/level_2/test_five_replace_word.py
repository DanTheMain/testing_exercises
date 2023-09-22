from functions.level_2.five_replace_word import replace_word


def _str_multiplier(string: str, count: int, sep: str) -> str:
    return sep.join(count * (string,))


def test__replace_word__simple_replace_matching_word():
    assert replace_word('replace some word', 'some', 'other') == 'replace other word'


def test__replace_word__simple_return_words_with_empty_from_to_words():
    assert replace_word('words', '', '') == 'words'


def test__replace_word__replace_matching_from_word():
    r_from, r_to = 'from_word', 'to_word'
    assert replace_word(f'replace {r_from}', r_from, r_to) == f'replace {r_to}'


def test__replace_word__replace_all_matching_from_words():
    r_from, r_to, wc, sep = 'from_word', 'to_word', 3, ' and '

    assert replace_word(_str_multiplier(r_from, wc, sep), r_from, r_to) == _str_multiplier(r_to, wc, sep)


def test__replace_word__return_replaced_all_words_with_mixed_case():
    r_from, r_to, wc, sep = 'MatchinG_FrOm_wOrd', 'MatchiNg_to_worD', 3, ' and '

    assert replace_word(_str_multiplier(r_from, wc, sep), r_from, r_to) == _str_multiplier(r_to, wc, sep)


def test__replace_word__return_original_words_with_no_matching_from_word_and_matching_to_word():
    r_from = 'from_word'
    r_to = f'non_matching_{r_from}'
    words = f'no match {r_to} - leave as is'

    assert replace_word(words, r_from, r_to) == words


def test__replace_word__return_empty_with_no_words():
    assert replace_word('', 'r_from', 'r_to') == ''


def test__replace_word__return_original_words_with_empty_from_to_words():
    words = 'placeholder words'
    assert replace_word(words, '', '') == words


def test__replace_word__return_empty_with_only_spaces_in_all_text():
    assert replace_word('         ', ' ', ' ') == ''

