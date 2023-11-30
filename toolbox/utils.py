import re
import html
import unidecode

SPECIAL_CLEANR = re.compile("[\s\.,:;]")


def unescape(v):
    return html.unescape(v)


def strip_tags(v):
    return re.sub(r"<[^>]*?>", "", v)


def special_clean(v):
    return SPECIAL_CLEANR.sub("", v)


def htmlize(v):
    return unidecode.unidecode(v.replace(" ", "-"))
