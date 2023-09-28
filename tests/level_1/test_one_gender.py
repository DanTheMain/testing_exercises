from pytest import mark
from functions.level_1.one_gender import genderalize


@mark.parametrize(
    'verb_male, verb_female, gender, expected',
    [
        ('verb_male', '', 'male', 'verb_male'),
        ('verb_male', 'verb_female', 'female', 'verb_female'),
        ('', 'verb_female', 'no_gender', 'verb_female'),
    ]
)
def test_male_female_default_genderalization(verb_male, verb_female, gender, expected):
    assert genderalize(verb_male, verb_female, gender) == expected


def test_matching_male_genderalization():
    verb_male, verb_female, male_gender = 'verb_male', 'verb_female', 'male'

    assert verb_female != genderalize(verb_male, '', male_gender)

