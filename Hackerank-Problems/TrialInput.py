# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:39:50 2018

@author: majaa
"""
import sys

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    for i, v in enumerate(argv):
        print("argv[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    main(sys.argv[1:])
