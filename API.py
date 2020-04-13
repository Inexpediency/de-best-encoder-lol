import itertools
from collections import namedtuple


class Encoder:
    _couple = namedtuple('couple', ['code', 'encode'])
    __ALPHABET = (
        _couple(code='A', encode='.@.'),
        _couple(code='B', encode='.8.'),
        _couple(code='C', encode='.⊂.'),
        _couple(code='D', encode='.⊃.'),
        _couple(code='E', encode='.☰.'),
        _couple(code='F', encode='.≔.'),
        _couple(code='G', encode='⅁..'),
        _couple(code='H', encode='|-|'),
        _couple(code='I', encode='.|.'),
        _couple(code='J', encode='⌡..'),
        _couple(code='K', encode='|<.'),
        _couple(code='L', encode='|_.'),
        _couple(code='M', encode='|⋎|'),
        _couple(code='N', encode='.ℵ.'),
        _couple(code='O', encode='.☢.'),
        _couple(code='P', encode='.|^'),
        _couple(code='Q', encode='.☢ᵕ'),
        _couple(code='R', encode='.≳.'),
        _couple(code='S', encode='.⌇.'),
        _couple(code='T', encode='.✝.'),
        _couple(code='U', encode='.⊍.'),
        _couple(code='V', encode='\./'),
        _couple(code='W', encode='|v|'),
        _couple(code='X', encode='.✕.'),
        _couple(code='Y', encode='.⋎.'),
        _couple(code='Z', encode='‾/_'),
        _couple(code=',', encode='///'),
        _couple(code='.', encode='|||'),
        _couple(code='...', encode='...'),
        _couple(code=':', encode='\\\\'),
        _couple(code='?', encode = '¿¿¿'),
        _couple(code='!', encode = '¡¡¡'),
        _couple(code=' ', encode='._.')
    )

    @staticmethod
    def coding(text: str) -> str:
        text = list(itertools.chain(text.upper()))
        coded_text = []
        for letter in text:
            completed = False
            for coding in Encoder.__ALPHABET:
                if coding.code == letter:
                    completed = True
                    coded_text.append(coding.encode)
                if completed:
                    break
            if not completed:
                coded_text.append(letter)
        coded_string = "".join(coded_text)
        return coded_string

    @staticmethod
    def encoding(text: str) -> str:
        text = [text[i:i + 3] for i in range(0, len(text), 3)]
        encoded_text = []
        for letter in text:
            completed = False
            for coding in Encoder.__ALPHABET:
                if coding.encode == letter:
                    completed = True
                    encoded_text.append(coding.code)
                if completed:
                    break
            if not completed:
                encoded_text.append(letter)
        encoded_string = "".join(encoded_text)
        return encoded_string.lower()
