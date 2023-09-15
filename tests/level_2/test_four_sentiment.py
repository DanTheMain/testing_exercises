from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__more_bad_words():
    good_word, good_word_num, bad_word, bad_word_num = 'good', 3, 'bad', 2
    text = ' '.join([good_word for _ in range(good_word_num)] + [bad_word for _ in range(bad_word_num)])

    assert check_tweet_sentiment(text, {good_word}, {bad_word}) == "GOOD"


def test__check_tweet_sentiment__more_good_words():
    good_word, good_word_num, bad_word, bad_word_num = 'good', 2, 'bad', 3
    text = ' '.join([good_word for _ in range(good_word_num)] + [bad_word for _ in range(bad_word_num)])

    assert check_tweet_sentiment(text, {good_word}, {bad_word}) == "BAD"


def test__check_tweet_sentiment__equal_number_of_good_bad_words():
    good_word, bad_word, word_num = 'good', 'bad', 3
    text = ' '.join([good_word for _ in range(word_num)] + [bad_word for _ in range(word_num)])

    assert check_tweet_sentiment(text, {good_word}, {bad_word}) is None


def test__check_tweet_sentiment__many_good_and_bad_words_with_more_good_words():
    good_word_count, bad_word_count = 5, 3
    bad_words = {'bad_' + str(i + 1) for i in range(bad_word_count)}
    good_words = {'good_' + str(i + 1) for i in range(good_word_count)}
    text = ' '.join(good_words.union(bad_words))

    assert check_tweet_sentiment(text, good_words, bad_words) == "GOOD"


def test__check_tweet_sentiment__many_good_and_bad_words_with_more_bad_words():
    good_word_count, bad_word_count = 3, 6
    bad_words = {'bad_' + str(i + 1) for i in range(bad_word_count)}
    good_words = {'good_' + str(i + 1) for i in range(good_word_count)}
    text = ' '.join(good_words.union(bad_words))

    assert check_tweet_sentiment(text, good_words, bad_words) == "BAD"


def test__check_tweet_sentiment__many_good_and_bad_words_with_equal_counts():
    good_word_count, bad_word_count = 3, 3
    bad_words = {'bad_' + str(i + 1) for i in range(bad_word_count)}
    good_words = {'good_' + str(i + 1) for i in range(good_word_count)}
    text = ' '.join(good_words.union(bad_words))

    assert check_tweet_sentiment(text, good_words, bad_words) is None


def test__check_tweet_sentiment__many_good_and_bad_and_other_words_more_good_words():
    good_word_count, bad_word_count = 4, 2
    bad_words = {'bad_' + str(i + 1) for i in range(bad_word_count)}
    good_words = {'good_' + str(i + 1) for i in range(good_word_count)}
    other_words = {'some', 'other', 'words'}
    text = ' '.join(good_words.union(bad_words).union(other_words))

    assert check_tweet_sentiment(text, good_words, bad_words) == "GOOD"


def test__check_tweet_sentiment__with_no_good_bad_words_in_text():
    good_word_count, bad_word_count = 3, 2
    bad_words = {'bad_' + str(i + 1) for i in range(bad_word_count)}
    good_words = {'good_' + str(i + 1) for i in range(good_word_count)}
    other_words = {'some', 'other', 'words'}
    text = ' '.join(other_words)

    assert check_tweet_sentiment(text, good_words, bad_words) is None


def test__check_tweet_sentiment__with_no_text():
    assert check_tweet_sentiment('', {'some', 'other', 'words'}, {'more, words'}) is None


def test__check_tweet_sentiment__many_good_and_bad_and_other_words_more_bad_upper_case_words():
    good_word_count, bad_word_count = 4, 7
    bad_words = {'bad_' + str(i + 1) for i in range(bad_word_count)}
    good_words = {'good_' + str(i + 1) for i in range(good_word_count)}
    other_words = {'some', 'other', 'words'}
    text = ' '.join(good_words.union({str(w).upper() for w in bad_words}).union(other_words))

    assert check_tweet_sentiment(text, good_words, bad_words) == "BAD"

