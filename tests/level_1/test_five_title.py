from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    max_title_len, default_max_title_len = 10, 100
    title_over_max, default_title_over_max = (f"{'a'.join(['a' * max_title_len])}",
                                              f"{'a'.join(['a' * default_max_title_len])}")
    assert (title_over_max == change_copy_item(title_over_max, max_title_len)), \
        'max title length test failed: different title returned or the title limiter argument is not used'
    assert (default_title_over_max == change_copy_item(default_title_over_max)), \
        'default max title length test failed'

    additional_copy_text: str = 'Copy of'
    sample_title: str = "sample"
    assert (f'{additional_copy_text} {sample_title}' == change_copy_item(sample_title))

    sample_copy_number = 0
    sample_title_with_copy_number = f'{additional_copy_text} {sample_title} ({sample_copy_number})'
    assert (f'{additional_copy_text} {sample_title} ({sample_copy_number+1})' == change_copy_item(sample_title_with_copy_number))
    assert (f'{additional_copy_text} (2)' == change_copy_item(additional_copy_text))
