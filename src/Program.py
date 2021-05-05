"""
Program for encrypting and decrypting text
"""

# -*- coding: utf-8 -*-
__author__ = 'Vladislav Markhivka'

import random
import io
import os


def main():
    """
    The main function is for the start dialogue
    """
    _answer: str = input("Виберіть режим\nШифрування чи Дешифрування <c/d> ")
    if _answer == 'c' or _answer == 'с':
        Cipher()
    elif _answer == 'd':
        AnCipher()
    else:
        print("Не коректна відповідь...")
        main()
    Final()

def Cipher():
    """
    It's a function that manages cipher processes
    """
    _codingText = str(input("Введіть текст для шифрування,не більше 25 символів "))
    _keyNumber = int(random.randint(2, 5))
    _textArray = CreateArray(_codingText)
    _text = Checker(_textArray, _keyNumber)
    FileWrite(_text + str(_keyNumber))

def AnCipher():
    """
    It's a function that manages decipher processes
    """
    _text = FileRead()
    _keyNumber = int(_text[-1])
    _text = _text[:-1]
    print("Текст із файлу\'TempFile.txt\' в розшифрованому вигляді ")
    print(Mover(AnCipherArray(CreateArray(_text), _keyNumber)))

def CreateArray(Text):
    """
    Text - text to convert
    It's а function that converts text to a array
    Returns an array consisting of text characters
    """
    if (type(Text) != str ):
        raise TypeError("Неправильний формат тексту")
    if (len(Text) > 25) :
        raise ValueError("Текст задовгий")
    elif(len(Text) == 0):
        raise ValueError("Введіть текст")
    _textArray = [[], [], [], [], []]
    for j in range(len(_textArray)):
        for i in Text:
            _textArray[j].append(i)
            Text = Text[1:]
            if len(_textArray[j]) == 5:
                break
    return _textArray

def Checker(Array, Key):
    """
    Array - array to fill
    Key - Key number to cipher
    It's а function that fills empty elements with characters
    Returns an array consisting of coded elements
    """
    if (type(Array) != list):
        raise TypeError("Неправильний формат масиву")
    if (type(Key) != int):
        raise TypeError("Неправильний формат коду")
    for i in range(len(Array)):
        if len(Array[i]) < 5:
            for j in range(5 - len(Array[i])):
                Array[i].append(' ')
    return CipherArray(Array, Key)

def AnCipherArray(Array, Key):
    """
    Array - array to decode
    Key - Key number to decode
    It's а function that decode elements
    Returns an array consisting of decode elements
    """
    if (type(Array) != list):
        raise TypeError("Неправильний формат масиву")
    if (type(Key) != int):
        raise TypeError("Неправильний формат коду")
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            Array[i][j] = chr(int(ord(Array[i][j]) / Key))
    return Array

def CipherArray(Array = [[" "]," "], Random = 1):
    """
    Array - array to coding
    Key - Key number to coding
    It's а function that encodes elements
    Returns an array consisting of coded elements
    """
    if (type(Array) != list):
        raise TypeError("Неправильний формат масиву")
    if (type(Random) != int):
        raise TypeError("Неправильний формат коду")
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            Array[i][j] = chr(ord(Array[i][j]) * Random)
    return Mover(Array)

def Mover(Array):
    """
    Array - array to sort
    It's а function that sorts array elements
    Returns a text consisting of sorted coded characters
    """
    Text = ""
    if (type(Array) != list):
        raise TypeError("Неправильний формат масиву")
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            Text += Array[j][i]
    return Text

def FileWrite(Text):
    """
    Text - text to write
    It's а function that write information to a file
    """
    if (type(Text) != str ):
        raise TypeError("Неправильний формат тексту")
    with io.open("TempFile.txt", "w", encoding="utf-8") as _file:
        _file.write(Text)
    print("Ваш текст збережено в файлі \'TempFile.txt\'")

def FileRead():
    """
    It's а function that read information from a file
    Returns a text read from a file
    """
    try:
        with io.open("TempFile.txt", "r", encoding="utf-8") as _file:
            Text = _file.read()
        return Text
    except FileNotFoundError:
        print(
            'Не вдалось знайти файл з текстом для дешифрування,щаб виправити проблему:\n1.Перевірте назву файлу для '
            'зчитування,вона повина бути \'TempFile.txt\'\n2.Перевірте розташування файлу,він повинен бути в одній '
            'деректорії з файлом программи')
        main()

def Final():
    """
    The final function is for the final dialogue
    """
    _answer = str(input("Що робити далі?\nВийти з програми чи Повернутись на початок <q/b> "))
    if 'q' == _answer:
        return 0
    elif _answer == 'b':
        os.system('cls||clear')
        main()
    else:
        print(" Не коректна відповідь...")
        Final()

if __name__ == '__main__':
    main()
