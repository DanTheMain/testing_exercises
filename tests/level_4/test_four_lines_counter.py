import pytest

from functions.level_4.four_lines_counter import count_lines_in


def test__count_lines_in__returns_none_with_non_existing_file():
    assert count_lines_in("non_existing_file.fake") is None


@pytest.mark.parametrize(
    "file_content, expected_count",
    [
        ("a\nb\nc\n", 3),
        ("a", 1),
        ("\n", 1),
        ("\n\n", 2),
    ],
)
def test__count_lines_in__returns_correct_line_count(
    file_content, expected_count, create_temp_file
):
    assert count_lines_in(create_temp_file(file_content)) == expected_count


@pytest.mark.parametrize(
    "file_content, expected_count", [("#a\nb\n#c\n", 1), ("#a", 0), ("\n#\n", 1)]
)
def test__count_lines_in__returns_correct_line_count_omitting_commented_lines(
    file_content, expected_count, create_temp_file
):
    assert count_lines_in(create_temp_file(file_content)) == expected_count


@pytest.mark.parametrize(
    "file_content, expected_count",
    [
        ("  #a  \n  b  \n #c\n", 1),
        (" #a  ", 0),
    ],
)
def test__count_lines_in__returns_correct_line_count_omitting_commented_lines_starting_with_spaces(
    file_content, expected_count, create_temp_file
):
    assert count_lines_in(create_temp_file(file_content)) == expected_count
