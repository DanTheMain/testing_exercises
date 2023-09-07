from functions.level_1.one_gender import genderalize


def test_genderalize():
    verb_male, verb_female = 'verb_male', 'verb_female'
    assert (verb_male == genderalize(verb_male, '', 'male'))
    assert (verb_female == genderalize(verb_male, verb_female, 'female'))
    assert (verb_female == genderalize('',verb_female, 'no_gender'))
    assert (verb_female != genderalize(verb_male, '', 'male'))
