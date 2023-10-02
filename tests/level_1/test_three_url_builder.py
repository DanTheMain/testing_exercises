import pytest
from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    'host_name, rel_url, params',
    [
        ('test_host', 'test_url', {'p1': 'pa-ra-ram', 'p2': 'pam-pam'}),
        ('test_host', 'test_url', None),
    ]
)
def test__build_url__with_without_params(host_name: str, rel_url: str, params: dict | None):
    expected = f'{host_name}/{rel_url}'
    if params is None:
        args = (host_name, rel_url)
    else:
        expected += f'?p1={params["p1"]}&p2={params["p2"]}'
        args = (host_name, rel_url, params)

    assert build_url(*args) == expected


def test__build_url__params_order_matters():
    host_name, rel_url, params = 'test_host', 'test_url', {'p1': 'pa-ra-ram', 'p2': 'pam-pam'}
    assert f'{host_name}/{rel_url}?p1={params["p2"]}&p2={params["p1"]}' != build_url(host_name, rel_url, params)


def test__build_url__host_name_use():
    host_name, rel_url = 'test_host', 'test_url'
    assert f'not a host/{rel_url}' != build_url(host_name, rel_url)

