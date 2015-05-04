#!/usr/bin/env python
# coding: utf-8
# preamble {{{
# Information {{{
#     Author:     Ibuki-E
#     Last Update:
#     Created:    2015-05-03
#     }}}
# Argument {{{
#
#     }}}

# }}}
from scipy.misc import comb
import sys

class deck: # {{{
    def __init__(self, x1, x2, x3):
        self.allDeck = x1
        self.maxLands = x2
        self.draw = x3
        self.list_sumLands = []
        self.list_before = []
    # setは標準入力から値を受け取り代入
    def set_allDeck(self): self.allDeck = input()
    def set_maxLands(self): self.maxLands = input()
    def set_draw(self): self.draw = input()
    # getは値を各値を出力
    def get_allDeck(self, argc):
        print "デッキ枚数 =",
        if argc != 4: self.set_allDeck()
        else: print self.allDeck
    def get_maxLands(self, argc):
        print "投入枚数   =",
        if argc != 4: self.set_maxLands()
        else: print self.maxLands
    def get_draw(self, argc):
        print "引く枚数   =",
        if argc != 4: self.set_draw()
        else: print self.draw
    # n枚以上引く確率を計算し出力
    def calc_prob(self):
        sumLands, x = 0, 0
        print
        print "枚数, 確率（n↑ ）, 確率（n）"
        while x < self.draw + 1:
            if x > self.maxLands: break
            if x != 0: (self.list_sumLands).append(1 - sumLands)
            sumLands += (comb(self.maxLands, x) * comb(self.allDeck - self.maxLands, self.draw - x) / comb(self.allDeck,self.draw))
            if x != 0 and x != self.maxLands: self.list_before.append(self.list_sumLands[-1] - ( 1 - sumLands))
            elif x == self.maxLands: self.list_before.append(self.list_sumLands[-1])
            x += 1
            before_prob = 0
    def display_prob(self):
        for x in xrange(self.draw + 1):
            if x > self.maxLands: break
            if x != 0: print "%4d  %10.3f  %9.3f" % (x, self.list_sumLands[x - 1] * 100, self.list_before[x-1] * 100)
# }}}
# コマンドライン引数取得と引数の個数チェック
argvs = sys.argv
argc = len(argvs)
# デッキ枚数，投入カード枚数，引く枚数をコマンドライン引数から取得
if argc == 4: mydeck = deck(int(argvs[1]), int(argvs[2]), int(argvs[3]))
else: mydeck = deck(60, 25, 7)

print "デッキに入っている特定のカードをn枚以上引く確率を出力"
# デッキ枚数表示，入力
mydeck.get_allDeck(argc)
# 投入カード枚数表示，入力
mydeck.get_maxLands(argc)
# 引く枚数表示，入力
mydeck.get_draw(argc)
# n枚以上引く確率を計算し表示
mydeck.calc_prob()
mydeck.display_prob()
