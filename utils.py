# -*- coding: utf-8 -*-

import os
import re

import fasttext
import langdetect
import langid


CURRENT_PATH = os.path.abspath(os.getcwd())

FASTTEXT_MODEL_PATH = os.path.join(CURRENT_PATH,
                                   'tmp',
                                   'lid.176.ftz')

# Mapping from ISO 639-1 language codes to ISO 639-3
LANGUAGE_MAPPING = {
    'cs': 'ces',
    'da': 'dan',
    'nl': 'nld',
    'en': 'eng',
    'fi': 'fin',
    'fr': 'fra',
    'de': 'deu',
    'hu': 'hun',
    'it': 'ita',
    'pl': 'pol',
    'pt': 'por',
    'ro': 'ron',
    'es': 'spa',
    'sv': 'swe'
}

UNKNOWN_LANGUAGE = '(unk)'


class LanguageIdentificationHelper(object):

    def __init__(self, library):
        self.library = library

        if self.library == 'fasttext':
            self.load_model()

    def load_model(self):
        self.ft_model = fasttext.load_model(FASTTEXT_MODEL_PATH)

    def predict(self, text):
        lang = None

        if self.library == 'langid':
            lang, _ = langid.classify(text)
        elif self.library == 'langdetect':
            lang = langdetect.detect(text)
        elif self.library == 'fasttext':
            text = [text] if isinstance(text, str) else text

            pred = self.ft_model.predict(text, k=1)
            pred = pred[0]

            lang = [
                re.sub(r'^[a-z_]+([a-z]{2})$', r'\1', y[0])
                for y in pred
            ]

        lang = [lang] if isinstance(lang, str) else lang
        lang = [
            (LANGUAGE_MAPPING[y] if y in LANGUAGE_MAPPING else UNKNOWN_LANGUAGE)
            for y in lang
        ]

        lang = lang[0] if len(lang) == 1 else lang

        return lang
