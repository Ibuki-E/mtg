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
    def __init__(self, x1 = 60, x2 = 25, x3 = 7):
        self.allDeck = x1
        self.maxLands = x2
        self.draw = x3
        self.list_sumLands = []
        self.list_before = []
        self.argvs = sys.argv
        self.argc = len(self.argvs)
    # setは標準入力から値を受け取り代入
    def set_allDeck(self):
        if self.argc == 4: self.allDeck = int(argv[1])
        else: self.allDeck = input()
    def set_maxLands(self):
        if self.argc == 4: self.maxLands = int(argv[2])
        else: self.maxLands = input()
    def set_draw(self):
        if self.argc == 4: self.draw = int(argv[3])
        else: self.draw = input()
    # getは値を各値を出力
    def get_allDeck(self):
        print "デッキ枚数 =",
        self.set_allDeck()
        if self.argc == 4: print self.allDeck
    def get_maxLands(self):
        print "投入枚数   =",
        self.set_maxLands()
        if self.argc == 4: print self.maxLands
    def get_draw(self):
        print "引く枚数   =",
        self.set_draw()
        if self.argc == 4: print self.draw
    # n枚以上引く確率を計算
    def calc_prob(self):
        sumLands, x = 0, 0
        print
        print "枚数, 確率（n↑ ）, 確率（n）"
        for x in xrange(self.draw + 1):
            if x > self.maxLands: break
            # n枚以上引く確率をリストへ
            if x != 0: (self.list_sumLands).append(1 - sumLands)
            sumLands += (comb(self.maxLands, x) * comb(self.allDeck - self.maxLands, self.draw - x) / comb(self.allDeck,self.draw))
            # n枚引く確率をリストへ
            if x != 0 and x != self.maxLands: self.list_before.append(self.list_sumLands[-1] - ( 1 - sumLands))
            elif x == self.maxLands: self.list_before.append(self.list_sumLands[-1])
    # 確率を出力
    def display_prob(self):
        for x in xrange(self.draw + 1):
            if x > self.maxLands: break
            if x != 0: print "%4d  %10.3f  %9.3f" % (x, self.list_sumLands[x - 1] * 100, self.list_before[x-1] * 100)
# }}}
# デッキ枚数，投入カード枚数，引く枚数をコマンドライン引数から取得
# コマンドライン引数が存在しないなら標準入力から取得
mydeck = deck()
print "デッキに入っている特定のカードをn枚以上引く確率を出力"
# デッキ枚数表示，入力
mydeck.get_allDeck()
# 投入カード枚数表示，入力
mydeck.get_maxLands()
# 引く枚数表示，入力
mydeck.get_draw()
# n枚以上引く確率を計算し表示
mydeck.calc_prob()
# 確率を出力
mydeck.display_prob()
