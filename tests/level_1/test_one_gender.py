from functions.level_1.one_gender import genderalize


def test_male_genderalization():
    verb_male = 'verb_male'
    assert verb_male == genderalize(verb_male, '', 'male')


def test_female_genderalization():
    verb_male, verb_female = 'verb_male', 'verb_female'
    assert verb_female == genderalize(verb_male, verb_female, 'female')


def test_default_genderalization():
    default_gender = 'verb_female'
    assert default_gender == genderalize('', default_gender, 'no_gender')


def test_matching_male_genderalization():
    verb_male, verb_female, male_gender = 'verb_male', 'verb_female', 'male'

    assert (verb_female != genderalize(verb_male, '', male_gender))

