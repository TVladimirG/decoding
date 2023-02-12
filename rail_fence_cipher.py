
from dataclasses import dataclass
from itertools import zip_longest


@dataclass()
class IncomData:
    """Входящие данные """
    text = 'Давай пересечем реку и отдохнем в тени деревьев'


def rail_fence_cipher_decript(text: str) -> str:
    """ Получим сообщение зашифрованное с помощью двухрядного 
    зигзагообразного шифра времен гражданской войны США """

    text: str = text.lower()
    text: str = text.replace(' ', '')

    # Если количество букв в фразе нечетное, тогда нам нужно обеспечить
    # чтобы первая половина фразы была на 1 единицу длиннее второй
    k: int = 0
    if len(text) % 2 != 0:
        k = 1

    first = tuple(text[:len(text)//2+k])
    second = tuple(text[len(text)//2+k:])

    open_text = []

    for i, j in zip_longest(first, second):
        if i is not None:
            open_text.append(i)
        if j is not None:
            open_text.append(j)

    return ''.join(open_text)


def rail_fence_cipher_encript(text: str):
    """ Зашифруем сообщение с помощью двухрядного 
    зигзагообразного шифра времен гражданской войны США """

    text: str = text.upper()
    text = text.replace(' ', '')

    first: str = text[::2]
    second: str = text[1::2]
    rail: str = (f'{first}{second}')

    cip_text: str = ' '.join(rail[i:i+5] for i in range(0, len(rail), 5))

    return cip_text


def __main__():
    open_text = IncomData.text
    print(f'Исходный текст: {open_text}')
    
    cip_text: str = rail_fence_cipher_encript(open_text)

    print(f'Зашифрованный текст% {cip_text}')

    open_text = rail_fence_cipher_decript(cip_text)
    print(f'Расшифрованный текст {open_text}')


if __name__ == "__main__":
    __main__()
