#! -*- coding: utf-8 -*-

from bert4keras.snippets import longest_common_subsequence


def red_color(text):
    return u'\033[1;31;40m%s\033[0m' % text


def green_color(text):
    return u'\033[1;32;40m%s\033[0m' % text


def compare(source, target):
    _, mapping = longest_common_subsequence(source, target)
    source_idxs = set([i for i, j in mapping])
    target_idxs = set([j for i, j in mapping])    
    colored_source, colored_target = u'', u''
    for i, j in enumerate(source):
        if i in source_idxs:
            colored_source += green_color(j)
        else:
            colored_source += red_color(j)
    for i, j in enumerate(target):
        if i in target_idxs:
            colored_target += green_color(j)
        else:
            colored_target += red_color(j)
    print(colored_source)
    print(colored_target)
