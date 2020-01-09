# encoding: utf-8

from rest_framework import parsers


class RawParser(parsers.BaseParser):
    """
    Parses Raw data.
    """
    media_type = '*/*'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream
