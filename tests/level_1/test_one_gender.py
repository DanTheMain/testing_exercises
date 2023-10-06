from functions.level_1.one_gender import genderalize


def test__genderalization__male():
    assert genderalize("verb_male", "", "male") == "verb_male"


def test__genderalization__female():
    assert genderalize("verb_male", "verb_female", "female") == "verb_female"


def test__genderalization__default():
    assert genderalize("", "default", "no_gender") == "default"


def test__genderalization__non_matching_male():
    assert "verb_female" != genderalize("verb_male", "", "male")
