from functions.level_4.two_students import get_student_by_tg_nickname


def test__get_student_by_tg_nickname__returns_no_matches_with_no_students(
    generate_test_students, generate_telegram_account
):
    assert (
        get_student_by_tg_nickname(
            generate_telegram_account(), generate_test_students(0)
        )
        is None
    )


def test__get_student_by_tg_nickname__returns_no_matches_with_no_matching_students(
    generate_test_students, generate_telegram_account
):
    assert (
        get_student_by_tg_nickname(
            generate_telegram_account(), generate_test_students()
        )
        is None
    )


def test__get_student_by_tg_nickname__returns_no_matches_with_students_without_tg_account(
    generate_test_student, generate_telegram_account
):
    assert (
        get_student_by_tg_nickname(
            generate_telegram_account(), [generate_test_student(telegram_account=None)]
        )
        is None
    )


def test__get_student_by_tg_nickname__returns_matching_student_by_tg_account(
    generate_test_student, generate_test_students, generate_telegram_account
):
    tg_account = generate_telegram_account()
    matching_student = generate_test_student(telegram_account=tg_account)
    students = generate_test_students() + [matching_student]
    assert (
        get_student_by_tg_nickname(
            telegram_username=tg_account.strip("@"), students=students
        )
        == matching_student
    )


def test__get_student_by_tg_nickname__returns_first_matching_student_by_tg_account(
    generate_test_student, generate_test_students, generate_telegram_account
):
    tg_account = generate_telegram_account()
    first_matching_student = generate_test_student(telegram_account=tg_account)
    second_matching_student = generate_test_student(telegram_account=tg_account)
    third_matching_student = generate_test_student(telegram_account=tg_account)
    students = generate_test_students() + [
        first_matching_student,
        second_matching_student,
        third_matching_student,
    ]

    assert (
        get_student_by_tg_nickname(
            telegram_username=tg_account.strip("@"), students=students
        )
        == first_matching_student
    )
