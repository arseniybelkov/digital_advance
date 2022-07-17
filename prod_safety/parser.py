import re
from functools import partial
from typing import List, Union

import pymorphy2


class Parser:
    def __init__(self, morph: pymorphy2.MorphAnalyzer, bar: bool=True):
        self.bar = bar
        self.morph = morph
        self.func_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
        self.ru_en = partial(re.sub, pattern=r'[^а-яА-Яa-zA-Z ]', repl='')
        self.ru = partial(re.sub, pattern=r'[^а-яА-Я ]', repl='')
        
    def check_pos(self, word: str) -> bool:
        return morph.parse(word)[0].tag.POS not in self.func_pos
    
    def preproc_text(self, text: str, parser: str='ru') -> str:
        assert parser in ('ru', 'en'), parser
        text = self.ru(string=text) if parser=='ru' else self.run_en(string=text)
        return [w for w in text.split(' ') if self.check_pos(w) and len(w) > 2]
    
    def parse_text(self, text: str, parser: str='ru') -> str:
        return ' '.join([morph.parse(w)[0].normal_form for w in self.preproc_text(text, parser)])
    
    def parse(self, texts: Union[str, List[str]], parser: str='ru') -> Union[str, List[str]]:
        is_str = False
        if isinstance(texts, str):
            is_str = True
            texts = [texts]
        parsed_texts = []
        for t in (tqdm(texts) if self.bar else texts):
            parsed_texts.append(' '.join(list(filter(lambda w: bool(w), self.parse_text(t, parser).strip().split(' ')))))
        return parsed_texts[0] if is_str else parsed_texts
