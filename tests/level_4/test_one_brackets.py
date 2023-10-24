from functions.level_4.one_brackets import delete_remove_brackets_quotes


def test__delete_remove_brackets_quotes__return_original_without_starting_brace():
    assert delete_remove_brackets_quotes("no_starting_{") == "no_starting_{"


def test__delete_remove_brackets_quotes__strip_first_last_chars_with_starting_brace():
    assert delete_remove_brackets_quotes("{name}") == "am"


def test_delete_remove_brackets_quotes__strip_from_short_name():
    assert delete_remove_brackets_quotes("{") == ""
