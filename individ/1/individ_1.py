#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("indiv_1.txt", "r") as fileptr:
        sentences = fileptr.readlines()

    # Вывод вопросительных предложений.
    for sentence in sentences:
        if "?" in sentence:
            print(sentence)

    # Вывод восклицательных предложений.
    for sentence in sentences:
        if "!" in sentence:
            print(sentence)
