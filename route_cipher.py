import sys
from dataclasses import dataclass


@dataclass()
class IncomData:
    """Входящие данные

    Матрица слов:  
    0   1   2   3   
    4   5   6   7   
    8   9   10  11  
    12  13  14  15  
    16  17  18  19

    Ключ шифрования: -4, -1, -2, -3
    Зашифрованный текст: 
    19 15 11 7 3 16 12 8 4 0 17 13 9 5 1 18 14 10 6 2 

    """

    # ciphertext: str = '16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'
    # keys: tuple[int] = (-1, 2, -3, 4)

    ciphertext: str = '19 15 11 7 3 16 12 8 4 0 17 13 9 5 1 18 14 10 6 2'
    keys: tuple[int] = (-4, -1, -2, -3)

    rows: int = 5
    cols: int = 4


def validate_datas(rows: int, cols: int, cipher_keys: tuple[int], words: str):
    """ Если матрица например 4х5 то слов должно быть 4х5=20 
        а так же количество ключей должно совпадать с количеством столбцов
    """

    if rows > 0 and cols > 0:
        if cols == len(cipher_keys) and rows * cols == len(words):
            return

    sys.exit


def decode_text(rows: int, cols: int, cipher_keys: tuple[int], words: list[str]) -> str:
    """ Входящий шифрованный текст - '16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'
        расшифрованный текст       - '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19'
    В итоге мы должны получить матрицу по количеству колонок (список списков)
    Помним, что количество значений в списке ключей совпадает с количеством колонок.
    Будем идти по списку ключей и смотреть их направление, знак минус это обратное направление
    Считываем слова порциями равными количеству строк в матрице
    Если обратное направление то разворачиваем колонку - reverse() 
    Считанные данные записываем в матрицу
    Затем идем по матрице и просто собираем сначала все первые элементы каждой колонки, затем вторые и т.д.
    """
    translation_matrix = [[]] * cols
    translation_list = []

    # Первая колонка
    start: int = 0
    stop: int = rows

    for k in cipher_keys:
        n = abs(k)

        col = words[start:stop]
        # Если ключ отрицательный, тогда нужно перевернуть список
        if k < 0:
            col.reverse()

        translation_matrix[n-1] = col

        # Следующая колонка
        start += rows
        stop += rows

    # Идем по матрице и собираем слова в правильном порядке
    # Сначала все первые элементы каждой колонки, затем вторые и т.д.
    for i in range(rows):
        for j in range(cols):
            translation_list.append(translation_matrix[j][i])

    return " ".join(translation_list)


def route_cipher_decript():

    # Получим начальные данные:
    # - Зашифрованный текст
    # - ключи шифрования
    cipher_text = IncomData.ciphertext
    cipher_keys = IncomData.keys

    # - количество колонок и строк в матрице
    rows: int = IncomData.rows
    cols: int = IncomData.cols

    print(f'Зашифрованный текст: {cipher_text}')
    print(f'Ключ шифрования: {cipher_keys}')

    # Разделим текст на целые слова
    words: list[str] = cipher_text.split()

    # Проверим входящие данные на корректность
    validate_datas(rows, cols, cipher_keys, words)

    # Декодируем текст
    decoded_text: str = decode_text(rows, cols, cipher_keys, words)

    print(f'Расшифрованный результат: {decoded_text}')


def __main__():
    route_cipher_decript()


if __name__ == "__main__":
    __main__()
