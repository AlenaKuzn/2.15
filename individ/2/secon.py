#!/usr/bin/env python3
# -*- coding: utf-8 -*

#Сумма после минимального
def summa_posl_min(*args):
    summ = 0
    if args:
        i_min = 0
        min = 99999
        for i in args:
            if abs(i) < min:
                min = abs(i)
                i_min = args.index(i)

        for i in args[i_min+1:]:
            summ += abs(i)
        return summ
    else:
        return None


if __name__ == "__main__":
    print(summa_posl_min())
    print("Сумма: ", summa_posl_min(5, -17, 5, -1, 15, 52, 32, -8))
    print("Сумма: ", summa_posl_min(17, -6, 11, 44, -2, 3, -5, 22))
