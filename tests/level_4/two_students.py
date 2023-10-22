from functions.level_4.two_students import Student, get_student_by_tg_nickname


def test__get_student_by_tg_nickname__returns_no_matches_with_no_students(generate_test_students,
                                                                          generate_telegram_account_and_username):
    assert get_student_by_tg_nickname(generate_telegram_account_and_username()[1], generate_test_students(0)) is None

