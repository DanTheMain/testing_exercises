from functions.level_2.five_replace_word import replace_word


def test__replace_word__simple_replace_matching_word():
    assert replace_word("replace some word", "some", "other") == "replace other word"


def test__replace_word__simple_return_words_with_empty_from_to_words():
    assert replace_word("words", "", "") == "words"


def test__replace_word__replace_matching_from_word():
    assert replace_word(f"replace from_word", "from_word", "r_to") == f"replace r_to"


def test__replace_word__replace_multiple_words(make_repeatable_str):
    r_from, r_to, wc, sep = "from_word", "to_word", 33, " and "
    starting_text, resulting_text = make_repeatable_str(
        r_from, wc, sep
    ), make_repeatable_str(r_to, wc, sep)
    assert replace_word(starting_text, r_from, r_to) == resulting_text


def test__replace_word__replace_single_word_with_non_matching_case():
    assert replace_word("word in wOrDs", "wOrd", "w0rd")


def test__replace_word__replace_multiple_words_with_non_matching_case(
    make_repeatable_str,
):
    r_from, r_to, wc, sep = "MatchinG_FrOm_wOrd", "MatchiNg_to_worD", 44, " and "
    starting_text, expected_text = make_repeatable_str(
        r_from, wc, sep
    ), make_repeatable_str(r_to, wc, sep)
    assert replace_word(starting_text, r_from, r_to) == expected_text


def test__replace_word__return_original_words_with_no_matching_from_word_and_matching_to_word():
    original_sentence = "original sentence"
    assert replace_word(original_sentence, "match", "no match") == original_sentence


def test__replace_word__return_empty_with_no_words():
    assert replace_word("", "r_from", "r_to") == ""


def test__replace_word__return_original_words_with_empty_from_to_words():
    words = "placeholder words"
    assert replace_word(words, "", "") == words


def test__replace_word__return_empty_with_only_spaces_in_all_text():
    assert replace_word("         ", " ", " ") == ""
