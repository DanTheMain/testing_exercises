from functions.level_1.three_url_builder import build_url


def test_build_url():
    host_name, rel_url, params = 'test_host', 'test_url', {'p1': 'pararam', 'p2': 'pam-pam'}
    assert(f'{host_name}/{rel_url}?p1={params["p1"]}&p2={params["p2"]}' == build_url(host_name, rel_url, params))
    assert (f'{host_name}/{rel_url}' == build_url(host_name, rel_url))
    assert (f'{host_name}/{rel_url}?p1={params["p2"]}&p2={params["p1"]}' != build_url(host_name, rel_url, params))
    assert (f'not_a_host/{rel_url}?p1={params["p1"]}&p2={params["p2"]}' != build_url(host_name, rel_url, params))