from functions.level_2.five_replace_word import replace_word


def test__replace_word__matching_from_word():
    r_from = 'matching_from_word'
    r_to = 'matching_to_word'
    words = f'if {r_from} matches, replace it with "{r_to}"'
    expected_new_words = f'if {r_to} matches, replace it with "{r_to}"'

    assert replace_word(words, r_from, r_to) == expected_new_words


def test__replace_word__matching_from_words():
    r_from = 'matching_from_word'
    r_to = 'matching_to_word'
    words = f'if {r_from} and {r_from} and {r_from} match, replace it with "{r_to}"'
    expected_new_words = f'if {r_to} and {r_to} and {r_to} match, replace it with "{r_to}"'

    assert replace_word(words, r_from, r_to) == expected_new_words


def test__replace_word__no_matching_from_words():
    r_from = 'from_word'
    r_to = f'non_matching_{r_from}'
    words = f'if {r_to} does not match "{r_from}", append words as is'

    assert replace_word(words, r_from, r_to) == words


def test__replace_word__no_words():
    assert replace_word('', 'r_from', 'r_to') == ''


def test__replace_word__empty_from_to_words():
    words = 'placeholder words'

    assert replace_word(words, '', '') == words


def test__replace_word_only_spaces():
    assert replace_word('         ', ' ', ' ') == ''


def test__replace_word__matching_lowered_from_words():
    r_from = 'MatchinG_FrOm_wOrd'
    r_to = 'MatchiNg_to_worD'
    words = f'if {r_from} and {r_from} and {r_from} match, replace it with "{r_to}"'
    expected_new_words = f'if {r_to} and {r_to} and {r_to} match, replace it with "{r_to}"'

    assert replace_word(words, r_from, r_to) == expected_new_words


