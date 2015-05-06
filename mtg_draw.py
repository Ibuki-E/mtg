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

# デッキ枚数，投入カード枚数，引く枚数をコマンドライン引数から取得
# コマンドライン引数が存在しないなら標準入力から取得
class deck: # {{{
    def __init__(self, x1 = 0, x2 = 0, x3 = 0):
        self.allDeck = x1
        self.maxLands = x2
        self.draw = x3
        self.list_sumLands = []
        self.list_before = []
        self.argvs = sys.argv
        self.argc = len(self.argvs)
        self.flag_input= 0
    # setは標準入力から値を受け取り代入
    def set_allDeck(self):
        if self.allDeck != 0: pass
        elif self.argc == 4: self.allDeck = int(self.argvs[1])
        else:
            self.allDeck = input()
            self.flag_input = 1
    def set_maxLands(self):
        if self.maxLands != 0: pass
        elif self.argc == 4: self.maxLands = int(self.argvs[2])
        else:
            self.maxLands = input()
            self.flag_input = 1
    def set_draw(self):
        if self.draw != 0: pass
        elif self.argc == 4: self.draw = int(self.argvs[3])
        else:
            self.draw = input()
            self.flag_input = 1
    # getは値を各値を出力
    def get_allDeck(self):
        print "デッキ枚数 =",
        self.set_allDeck()
        if self.argc == 4 or self.flag_input == 0: print self.allDeck
        self.flag_input = 0
    def get_maxLands(self):
        print "投入枚数   =",
        self.set_maxLands()
        if self.argc == 4 or self.flag_input == 0: print self.maxLands
        self.flag_input = 0
    def get_draw(self):
        print "引く枚数   =",
        self.set_draw()
        if self.argc == 4 or self.flag_input == 0: print self.draw
        self.flag_input = 0
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
    def do_draw(self):
        print "デッキに入っている特定のカードをn枚以上引く確率を出力"
        self.get_allDeck()
        self.get_maxLands()
        self.get_draw()
        self.calc_prob()
        self.display_prob()
# }}}
"""
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
"""
