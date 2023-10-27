from unittest.mock import patch

import pytest

from functions.level_4.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field


def test__fetch_extra_fields_configuration__returns_empty_container_with_non_existent_config():
    assert fetch_extra_fields_configuration('imnothere') == {}


def test__fetch_extra_fields_configuration__returns_empty_container_with_existing_config(test_file):
    assert fetch_extra_fields_configuration(test_file()) == {}


def test__fetch_extra_fields_configuration__return_single_mapping_from_container():
    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as fetch_app_config_field_mock:
        fetch_app_config_field_mock.return_value = 'a: 1'
        assert fetch_extra_fields_configuration('anything') == {'a': 1}


def test__fetch_extra_fields_configuration__return__multiple_mappings_from_container():
    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as fetch_app_config_field_mock:
        fetch_app_config_field_mock.return_value = 'a: 1\nb: 2\nc: 3'
        assert fetch_extra_fields_configuration('anything') == {'a': 1, 'b': 2, 'c': 3}


def test__fetch_extra_fields_configuration__return__multiple_expression_mappings_from_container():
    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as fetch_app_config_field_mock:
        fetch_app_config_field_mock.return_value = 'a: 1 + 1\nb: 2**2\nc: 3 - 3\nd: "some" + "thing"'
        assert fetch_extra_fields_configuration('anything') == {'a': 2, 'b': 4, 'c': 0, 'd': 'something'}


@pytest.mark.xfail(reason='failed on evaluating an empty value', raises=IndexError)
def test__fetch_extra_fields_configuration__throw_error_when_mapping_is_undefined():
    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as fetch_app_config_field_mock:
        fetch_app_config_field_mock.return_value = 'a: \n'
        assert fetch_extra_fields_configuration('anything') == {'a': ''}


def test__fetch_app_config_field__return_None_with_no_matching_key(test_file):
    assert fetch_app_config_field(test_file('[tool:app-config]\nsome_field=value'), 'another_field') is None


def test__fetch_app_config_field__return_value_with_matching_key(test_file):
    assert fetch_app_config_field(test_file('[tool:app-config]\nsome_field=value'), 'some_field') == 'value'


def test__fetch_app_config_field__return_none_with_no_matching_section(test_file):
    assert fetch_app_config_field(test_file(), 'some_field') is None


def test__fetch_app_config_field__return_none_when_no_config_file_exists():
    assert fetch_app_config_field('no_such_file', 'some_field') is None
