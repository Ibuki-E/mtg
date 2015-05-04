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
print "デッキに入っている特定のカードをn枚以上引く確率を出力"
print "デッキ枚数 =",
deck = input()
print "投入枚数   =",
maxLands = input()
print "引く枚数   =",
draw = input()
#print "何枚以上引きたい   =",
#moreLand = input()

sumLands = 0
x = 0
print
print "枚数, 確率"
while x < draw + 1:
    if x > maxLands: break
#    if draw <= 7: print "   %d  %6.2f" % (x, (1 - sumLands) * 100)
    if x != 0: print "%4d  %6.2f" % (x, (1 - sumLands) * 100)
    sumLands += (comb(maxLands, x) * comb(deck - maxLands, draw - x) / comb(deck,draw))
    x += 1
#    if x == moreLand : first = (1 - sumLands) * 100
#print "%d枚以上引ける確率 = %6.2f" % (moreLand, first)
