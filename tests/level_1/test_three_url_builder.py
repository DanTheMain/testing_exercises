from functions.level_1.three_url_builder import build_url


def test_build_url_with_params():
    host_name, rel_url, params = 'test_host', 'test_url', {'p1': 'pararam', 'p2': 'pam-pam'}
    assert build_url(host_name, rel_url, params) == f'{host_name}/{rel_url}?p1={params["p1"]}&p2={params["p2"]}'


def test_build_url_no_params():
    host_name, rel_url = 'test_host', 'test_url'
    assert build_url(host_name, rel_url) == f'{host_name}/{rel_url}'


def test__build_url__params_order_matters():
    host_name, rel_url, params = 'test_host', 'test_url', {'p1': 'pa-ra-ram', 'p2': 'pam-pam'}
    assert build_url(host_name, rel_url, params) != f'{host_name}/{rel_url}?p1={params["p2"]}&p2={params["p1"]}'


def test__build_url__host_name_use():
    host_name, rel_url = 'test_host', 'test_url'
    assert build_url(host_name, rel_url) != f'not a host/{rel_url}'

