
Googol = 10**100
fib_num_481 = 14913169640232740127827512057302148063648650711209401966150219926546779697987984279570098768737999681
prev = 0
curr = 1
print('\033[95mFibonacci Sequence')
print('\033[36mUnits\u001b[37m')
print(prev)
for i in range(0, 1760): # 1470

   if curr >= 0 and curr < 10:
      print('\033[36mUnits\u001b[37m')
   elif curr >= 10 and curr < 100:
      print('\033[95mTens\u001b[37m')
   elif curr >= 100 and curr < 1000:
      print('\u001b[34;1mHundreds\u001b[37m')
   elif curr >= 1000 and curr < 100000: # 10^2
      print('\u001b[31;1mThousands\u001b[37m')
   elif curr >= 100000 and curr < 1000000: # 10^3
      print('\u001b[32mHundred Thousands\u001b[37m')
   elif curr >= 10**6 and curr < 10**9:
      print('\u001b[33;1mMillion\u001b[37m') # 1st illion
   elif curr >= 10**9 and curr < 10**12:
      print('\u001b[34;1mBillion\u001b[37m') # 2
   elif curr >= 10**12 and curr < 10**15:
      print('\u001b[31;1mTrillion\u001b[37m') # 3
   elif curr >= 10**15 and curr < 10**18:
      print('\u001b[36mQuadrillion\u001b[37m') # 4
   elif curr >= 10**18 and curr < 10**21:
      print('\u001b[35mQuintillion\u001b[37m') # 5
   elif curr >= 10**21 and curr < 10**24:
      print('\u001b[32mSextillion\u001b[37m') # 6
   elif curr >= 10**24 and curr < 10**27:
      print('\u001b[33;1mSeptillion\u001b[37m') # 7
   elif curr >= 10**27 and curr < 10**30:
      print('\u001b[34;1mOctillion\u001b[37m') # 8
   elif curr >= 10**30 and curr < 10**33:
      print('\u001b[31;1mNonillion\u001b[37m') # 9
   elif curr >= 10**33 and curr < 10**36:
      print('\u001b[36mDecillion\u001b[37m') # 10
   elif curr >= 10**36 and curr < 10**39:
      print('\u001b[35mUndecillions\u001b[37m') # 11
   elif curr >= 10**39 and curr < 10**42:
      print('\u001b[32mDuodecillion\u001b[37m') # 12
   elif curr >= 10**42 and curr < 10**45:
      print('\u001b[33;1mTredecillion\u001b[37m') # 13
   elif curr >= 10**45 and curr < 10**48:
      print('\u001b[34;1mQuattuordecillion\u001b[37m') # 14
   elif curr >= 10**48 and curr < 10**51:
      print('\u001b[31;1mQuindecillion\u001b[37m') # 15
   elif curr >= 10**51 and curr < 10**54:
      print('\u001b[36mSexdecillion\u001b[37m') # 16
   elif curr >= 10**54 and curr < 10**57:
      print('\u001b[35mSeptendecillion\u001b[37m') # 17
   elif curr >= 10**57 and curr < 10**60:
      print('\u001b[32mOctodecillion\u001b[37m') # 18
   elif curr >= 10**60 and curr < 10**63:
      print('\u001b[34;1mNovemdecillion\u001b[37m') # 19
   elif curr >= 10**63 and curr < 10**66:
      print('\u001b[31;1mVigintillion\u001b[37m') # 20
   elif curr >= 10**66 and curr < 10**69:
      print('\u001b[36mUnvigintillion\u001b[37m') # 21
   elif curr >= 10**69 and curr < 10**72:
      print('\u001b[35mDuovigintillion\u001b[37m') # 22 
   elif curr >= 10**72 and curr < 10**75:
      print('\u001b[32mTresvigintillion\u001b[37m') # 23
   elif curr >= 10**75 and curr < 10**78:
      print('\u001b[34;1mQuattuorvigintillion\u001b[37m') # 24
   elif curr >= 10**78 and curr < 10**81:
      print('\u001b[33;1mQuinvigintillion\u001b[37m') # 25
   elif curr >= 10**81 and curr < 10**84:
      print('\u001b[31;1mSexvigintillion\u001b[37m') # 26
   elif curr >= 10**84 and curr < 10**87:
      print('\u001b[36mSeptemvigintillion\u001b[37m') # 27
   elif curr >= 10**87 and curr < 10**90:
      print('\u001b[35mOctovigintillion\u001b[37m') # 28
   elif curr >= 10**90 and curr < 10**93:
      print('\u001b[32mNovemvigintillion\u001b[37m') # 29
   elif curr >= 10**93 and curr < 10**96:
      print('\u001b[34;1mTrigintillion\u001b[37m') # 30
   elif curr >= 10**96 and curr < 10**99:
      print('\u001b[33;1mUntrigintillion\u001b[37m') # 31
   
   elif curr == fib_num_481:
      print('\u001b[31;1mTen-Duotrigintillion \u001b[33;1m(Googol)\u001b[37m') 
      print('\u001b[33;1m{:,}\u001b[37m'.format(Googol)) # 10^100
      print('\u001b[31;1mDuotrigintillion\u001b[37m')

   elif curr >= 10**99 and curr < 10**102:
      print('\u001b[31;1mDuotrigintillion\u001b[37m') # 32
   elif curr >= 10**102 and curr < 10**105:
      print('\u001b[36mTrestrigintillion\u001b[37m') # 33
   elif curr >= 10**105 and curr < 10**108:
      print('\u001b[35mQuattuortrigintillion\u001b[37m') # 34
   elif curr >= 10**108 and curr < 10**111:
      print('\u001b[32mQuintrigintillion\u001b[37m') # 35
   elif curr >= 10**111 and curr < 10**114:
      print('\u001b[34;1mSextrigintillion\u001b[37m') # 36
   elif curr >= 10**114 and curr < 10**117:
      print('\u001b[33;1mSeptentrigintillion\u001b[37m') # 37
   elif curr >= 10**117 and curr < 10**120:
      print('\u001b[31;1mOctotrigintillion\u001b[37m') # 38
   elif curr >= 10**120 and curr < 10**123:
      print('\u001b[36mNovemtrigintillion\u001b[37m') # 39
   elif curr >= 10**123 and curr < 10**126:
      print('\u001b[35mQuadragintillion\u001b[37m') # 40
   elif curr >= 10**126 and curr < 10**129:
      print('\u001b[32mUnquadragintillion\u001b[37m') # 41
   elif curr >= 10**129 and curr < 10**132:
      print('\u001b[34;1mDuoquadragintillion\u001b[37m') # 42
   elif curr >= 10**132 and curr < 10**135:
      print('\u001b[33;1mTrequadragintillion\u001b[37m') # 43
   elif curr >= 10**135 and curr < 10**138:
      print('\u001b[31;1mQuattuorquadragintillion\u001b[37m') # 44
   elif curr >= 10**138 and curr < 10**141:
      print('\u001b[36mQuinquadragintillion\u001b[37m') # 45
   elif curr >= 10**141 and curr < 10**144:
      print('\u001b[33mSexquadragintillion\u001b[37m') # 46
   elif curr >= 10**144 and curr < 10**147:
      print('\u001b[35mSeptenquadragintillion\u001b[37m') # 47
   elif curr >= 10**147 and curr < 10**150:
      print('\u001b[32mOctoquadragintillion\u001b[37m') # 48
   elif curr >= 10**150 and curr < 10**153:
      print('\u001b[34mNovemquadragintillion\u001b[37m') # 49
   elif curr >= 10**153 and curr < 10**156:
      print('\u001b[33mQuinquagintillion\u001b[37m') # 50
   elif curr >= 10**156 and curr < 10**159:
      print('\u001b[31mUnquinquagintillion\u001b[37m') # 51
   elif curr >= 10**159 and curr < 10**162:
      print('\u001b[36mDuoquinquagintillion\u001b[37m') # 52
   elif curr >= 10**162 and curr < 10**165:
      print('\u001b[33mTrequinquagintillion\u001b[37m') # 53
   elif curr >= 10**165 and curr < 10**168:
      print('\u001b[35mQuattuorquinquagintillion\u001b[37m') # 54
   elif curr >= 10**168 and curr < 10**171:
      print('\u001b[32mQuinquinquagintillion\u001b[37m') # 55
   elif curr >= 10**171 and curr < 10**174:
      print('\u001b[34mSexquinquagintillion\u001b[37m') # 56
   elif curr >= 10**174 and curr < 10**177:
      print('\u001b[33mSeptenquinquagintillion\u001b[37m') # 57
   elif curr >= 10**177 and curr < 10**180:
      print('\u001b[31mOctoquinquagintillion\u001b[37m') # 58
   elif curr >= 10**180 and curr < 10**183:
      print('\u001b[33mNovemquinquagintillion\u001b[37m') # 59
   elif curr >= 10**183 and curr < 10**186:
      print('\u001b[35mSexagintillion\u001b[37m') # 60
   elif curr >= 10**186 and curr < 10**189:
      print('\u001b[32mUnsexagintillion\u001b[37m') # 61
   elif curr >= 10**189 and curr < 10**192:
      print('\u001b[34mDuosexagintillion\u001b[37m') # 62
   elif curr >= 10**192 and curr < 10**195:
      print('\u001b[33mTresexagintillion\u001b[37m') # 63
   elif curr >= 10**195 and curr < 10**198:
      print('\u001b[35mQuattuorsexagintillion\u001b[37m') # 64
   elif curr >= 10**198 and curr < 10**201:
      print('\u001b[32mQuinsexagintillion\u001b[37m') # 65
   elif curr >= 10**201 and curr < 10**204:
      print('\u001b[34mSexsexagintillion\u001b[37m') # 66
   elif curr >= 10**204 and curr < 10**207:
      print('\u001b[33mSeptensexagintillion\u001b[37m') # 67
   elif curr >= 10**207 and curr < 10**210:
      print('\u001b[35mOctosexagintillion\u001b[37m') # 68
   elif curr >= 10**210 and curr < 10**213:
      print('\u001b[32mNovemsexagintillion\u001b[37m') # 69
   elif curr >= 10**213 and curr < 10**216:
      print('\u001b[34mSeptuagintillion\u001b[37m') # 70
   elif curr >= 10**216 and curr < 10**219:
      print('\u001b[33mUnseptuagintillion\u001b[37m') # 71
   elif curr >= 10**219 and curr < 10**222:
      print('\u001b[35mDuoseptuagintillion\u001b[37m') # 72
   elif curr >= 10**222 and curr < 10**225:
      print('\u001b[32mTreseptuagintillion\u001b[37m') # 73
   elif curr >= 10**225 and curr < 10**228:
      print('\u001b[34mQuattuorseptuagintillion\u001b[37m') # 74
   elif curr >= 10**228 and curr < 10**231:
      print('\u001b[33mQuinseptuagintillion\u001b[37m') # 75
   elif curr >= 10**231 and curr < 10**234:
      print('\u001b[35mSexseptuagintillion\u001b[37m') # 76
   elif curr >= 10**234 and curr < 10**237:
      print('\u001b[32mSeptenseptuagintillion\u001b[37m') # 77
   elif curr >= 10**237 and curr < 10**240:
      print('\u001b[34mOctoseptuagintillion\u001b[37m') # 78
   elif curr >= 10**240 and curr < 10**243:
      print('\u001b[33mNovemseptuagintillion\u001b[37m') # 79
   elif curr >= 10**243 and curr < 10**246:
      print('\u001b[35mOctogintillion\u001b[37m') # 80
   elif curr >= 10**246 and curr < 10**249:
      print('\u001b[32mUnoctogintillion\u001b[37m') # 81
   elif curr >= 10**249 and curr < 10**252:
      print('\u001b[34mDuooctogintillion\u001b[37m') # 82
   elif curr >= 10**252 and curr < 10**255:
      print('\u001b[33mTreoctogintillion\u001b[37m') # 83
   elif curr >= 10**255 and curr < 10**258:
      print('\u001b[35mQuattuoroctogintillion\u001b[37m') # 84
   elif curr >= 10**258 and curr < 10**261:
      print('\u001b[32mQuinoctogintillion\u001b[37m') # 85
   elif curr >= 10**261 and curr < 10**264:
      print('\u001b[34mSexoctogintillion\u001b[37m') # 86
   elif curr >= 10**264 and curr < 10**267:
      print('\u001b[33mSeptenoctogintillion\u001b[37m') # 87
   elif curr >= 10**267 and curr < 10**270:
      print('\u001b[35mOctooctogintillion\u001b[37m') # 88
   elif curr >= 10**270 and curr < 10**273:
      print('\u001b[32mNovemoctogintillion\u001b[37m') # 89
   elif curr >= 10**273 and curr < 10**276:
      print('\u001b[34mNonagintillion\u001b[37m') # 90
   elif curr >= 10**276 and curr < 10**279:
      print('\u001b[33mUnnonagintillion\u001b[37m') # 91
   elif curr >= 10**279 and curr < 10**282:
      print('\u001b[35mDuononagintillion\u001b[37m') # 92
   elif curr >= 10**282 and curr < 10**285:
      print('\u001b[32mTrenonagintillion\u001b[37m') # 93
   elif curr >= 10**285 and curr < 10**288:
      print('\u001b[34mQuattuornonagintillion\u001b[37m') # 94
   elif curr >= 10**288 and curr < 10**291:
      print('\u001b[33mQuinnonagintillion\u001b[37m') # 95
   elif curr >= 10**291 and curr < 10**294:
      print('\u001b[35mSexnonagintillion\u001b[37m') # 96
   elif curr >= 10**294 and curr < 10**297:
      print('\u001b[32mSeptennonagintillion\u001b[37m') # 97
   elif curr >= 10**297 and curr < 10**300:
      print('\u001b[34mOctononagintillion\u001b[37m') # 98
   elif curr >= 10**300 and curr < 10**303:
      print('\u001b[33mNovemnonagintillion\u001b[37m') # 99
   elif curr >= 10**303 and curr < 10**306:
      print('\u001b[35mCentillion\u001b[37m') # 100
   elif curr >= 10**306 and curr < 10**309:
      print('\u001b[34mUncentillion\u001b[37m') # 101
   elif curr >= 10**309 and curr < 10**312:
      print('\u001b[33mDuocentillion\u001b[37m') # 102
   elif curr >= 10**312 and curr < 10**315:
      print('\u001b[34mTrecentillion\u001b[37m') # 103
   elif curr >= 10**315 and curr < 10**318:
      print('\u001b[35mQuattuorcentillion\u001b[37m') # 104
   elif curr >= 10**318 and curr < 10**321:
      print('\u001b[33mQuincentillion\u001b[37m') # 105
   elif curr >= 10**321 and curr < 10**324:
      print('\u001b[34mSexcentillion\u001b[37m') # 106
   elif curr >= 10**324 and curr < 10**327:
      print('\u001b[35mSeptencentillion\u001b[37m') # 107
   elif curr >= 10**327 and curr < 10**330:
      print('\u001b[33mOctocentillion\u001b[37m') # 108
   elif curr >= 10**330 and curr < 10**333:
      print('\u001b[34mNovemcentillion\u001b[37m') # 109
   elif curr >= 10**333 and curr < 10**336:
      print('\u001b[35mDecicentillion\u001b[37m') # 110
   elif curr >= 10**336 and curr < 10**339:
      print('\u001b[33mUndecicentillion\u001b[37m') # 111
   elif curr >= 10**339 and curr < 10**342:
      print('\u001b[34mDuodecicentillion\u001b[37m') # 112
   elif curr >= 10**342 and curr < 10**345:
      print('\u001b[35mTredecicentillion\u001b[37m') # 113
   elif curr >= 10**345 and curr < 10**348:
      print('\u001b[33mQuattourdecicentillion\u001b[37m') # 114
   elif curr >= 10**348 and curr < 10**351:
      print('\u001b[34mQuindecicentillion\u001b[37m') # 115
   elif curr >= 10**351 and curr < 10**354:
      print('\u001b[35mSexdecicentillion\u001b[37m') # 116
   elif curr >= 10**354 and curr < 10**357:
      print('\u001b[33mSeptendecicentillion\u001b[37m') # 117
   elif curr >= 10**357 and curr < 10**360:
      print('\u001b[34mOctodecicentillion\u001b[37m') # 118
   elif curr >= 10**360 and curr < 10**363:
      print('\u001b[35mNovemdecicentillion\u001b[37m') # 119
   elif curr >= 10**363 and curr < 10**366:
      print('\u001b[33;1m120-illion\u001b[37m') # 120
   else:
      print('\u001b[31;1mUnknown\u001b[37m')
   print('{:,}'.format(curr))
   old_curr = curr
   curr = prev + curr
   prev = old_curr
print('\n')

# Googol = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# i = 0
# while i < Googol:
#    print(i)
#    i += 1000000000000000000000000000


# mil = 10**1000000
# f = open('mil.txt', 'w')
# f.write(str(mil))
# f.close()
#print(10**mil


# f = open('fib.txt', 'w')
# n = 1
# i = 0
# while i < 1000:
#    n += 1
#    m = '{}\n'.format(str(n))
#    f.write(m)
#    i += 1 


# prev = 0
# curr = 1
# f = open('fib.txt', 'w')
# f.write('Fibonacci Sequence\n')
# f.write('Units\n0\n')
# for i in range(0, 1760): # 1760
#    if curr >= 0 and curr < 10:
#       f.write('Units\n')
#    elif curr >= 10 and curr < 100:
#       f.write('Tens\n')
#    elif curr >= 100 and curr < 1000:
#       f.write('Hundreds\n')
#    elif curr >= 1000 and curr < 100000: # 10^2
#       f.write('Thousands\n')
#    elif curr >= 100000 and curr < 1000000: # 10^3
#       f.write('Hundred Thousands\n')
#    elif curr >= 10**6 and curr < 10**9:
#       f.write('Millions\n') # 10^6
#    elif curr >= 10**9 and curr < 10**12:
#       f.write('Billions\n') # 10^9
#    elif curr >= 10**12 and curr < 10**15:
#       f.write('Tillions\n') # 10^12
#    elif curr >= 10**15 and curr < 10**18:
#       f.write('Quadrillions\n') # 10^15
#    elif curr >= 10**18 and curr < 10**21:
#       f.write('Quintillions\n') # 10^18
#    elif curr >= 10**21 and curr < 10**24:
#       f.write('Sextillion\n') # 6
#    elif curr >= 10**24 and curr < 10**27:
#       f.write('Septillion\n') # 7
#    elif curr >= 10**27 and curr < 10**30:
#       f.write('Octillion\n') # 8
#    elif curr >= 10**30 and curr < 10**33:
#       f.write('Nonillion\n') # 9
#    elif curr >= 10**33 and curr < 10**36:
#       f.write('Decillion\n') # 10
#    elif curr >= 10**36 and curr < 10**39:
#       f.write('Undecillion\n') # 11
#    elif curr >= 10**39 and curr < 10**42:
#       f.write('Duodecillion\n') # 12
#    elif curr >= 10**42 and curr < 10**45:
#       f.write('Tredecillion\n') # 13
#    elif curr >= 10**45 and curr < 10**48:
#       f.write('Quattuordecillion\n') # 14
#    elif curr >= 10**48 and curr < 10**51:
#       f.write('Quindecillion\n') # 15
#    elif curr >= 10**51 and curr < 10**54:
#       f.write('Sexdecillion\n') # 16
#    elif curr >= 10**54 and curr < 10**57:
#       f.write('Septendecillion\n') # 17
#    elif curr >= 10**57 and curr < 10**60:
#       f.write('Octodecillion\n') # 18
#    elif curr >= 10**60 and curr < 10**63:
#       f.write('Novemdecillion\n') # 19
#    elif curr >= 10**63 and curr < 10**66:
#       f.write('Vigintillion\n') # 20
#    elif curr >= 10**66 and curr < 10**69:
#       f.write('Unvigintillion\n') # 21
#    elif curr >= 10**69 and curr < 10**72:
#       f.write('Duovigintillion\n') # 22 
#    elif curr >= 10**72 and curr < 10**75:
#       f.write('Tresvigintillion\n') # 23
#    elif curr >= 10**75 and curr < 10**78:
#       f.write('Quattuorvigintillion\n') # 24
#    elif curr >= 10**78 and curr < 10**81:
#       f.write('Quinvigintillion\n') # 25
#    elif curr >= 10**81 and curr < 10**84:
#       f.write('Sexvigintillion\n') # 26
#    elif curr >= 10**84 and curr < 10**87:
#       f.write('Septemvigintillion\n') # 27
#    elif curr >= 10**87 and curr < 10**90:
#       f.write('Octovigintillion\n') # 28
#    elif curr >= 10**90 and curr < 10**93:
#       f.write('Novemvigintillion\n') # 29
#    elif curr >= 10**93 and curr < 10**96:
#       f.write('Trigintillion\n') # 30
#    elif curr >= 10**96 and curr < 10**99:
#       f.write('Untrigintillion\n') # 31
   
#    elif curr == fib_num_481:
#       f.write('Ten-Duotrigintillion (Googol)\n') 
#       f.write('{:,} {}'.format(Googol, '\n')) # 10^100
#       f.write('Duotrigintillion\n')

#    elif curr >= 10**99 and curr < 10**102:
#       f.write('Duotrigintillion\n') # 32
#    elif curr >= 10**102 and curr < 10**105:
#       f.write('Trestrigintillion\n') # 33
#    elif curr >= 10**105 and curr < 10**108:
#       f.write('Quattuortrigintillion\n') # 34
#    elif curr >= 10**108 and curr < 10**111:
#       f.write('Quintrigintillion\n') # 35
#    elif curr >= 10**111 and curr < 10**114:
#       f.write('Sextrigintillion\n') # 36
#    elif curr >= 10**114 and curr < 10**117:
#       f.write('Septentrigintillion\n') # 37
#    elif curr >= 10**117 and curr < 10**120:
#       f.write('Octotrigintillion\n') # 38
#    elif curr >= 10**120 and curr < 10**123:
#       f.write('Novemtrigintillion\n') # 39
#    elif curr >= 10**123 and curr < 10**126:
#       f.write('Quadragintillion\n') # 40
#    elif curr >= 10**126 and curr < 10**129:
#       f.write('Unquadragintillion\n') # 41
#    elif curr >= 10**129 and curr < 10**132:
#       f.write('Duoquadragintillion\n') # 42
#    elif curr >= 10**132 and curr < 10**135:
#       f.write('Trequadragintillion\n') # 43
#    elif curr >= 10**135 and curr < 10**138:
#       f.write('Quattuorquadragintillion\n') # 44
#    elif curr >= 10**138 and curr < 10**141:
#       f.write('Quinquadragintillion\n') # 45
#    elif curr >= 10**141 and curr < 10**144:
#       f.write('Sexquadragintillion\n') # 46
#    elif curr >= 10**144 and curr < 10**147:
#       f.write('Septenquadragintillion\n') # 47
#    elif curr >= 10**147 and curr < 10**150:
#       f.write('Octoquadragintillion\n') # 48
#    elif curr >= 10**150 and curr < 10**153:
#        f.write('Novemquadragintillion\n') # 49
#    elif curr >= 10**153 and curr < 10**156:
#       f.write('Quinquagintillion\n') # 50
#    elif curr >= 10**156 and curr < 10**159:
#       f.write('Unquinquagintillion\n') # 51
#    elif curr >= 10**159 and curr < 10**162:
#       f.write('Duoquinquagintillion\n') # 52
#    elif curr >= 10**162 and curr < 10**165:
#       f.write('Trequinquagintillion\n') # 53
#    elif curr >= 10**165 and curr < 10**168:
#       f.write('Quattuorquinquagintillion\n') # 54
#    elif curr >= 10**168 and curr < 10**171:
#       f.write('Quinquinquagintillion\n') # 55
#    elif curr >= 10**171 and curr < 10**174:
#       f.write('Sexquinquagintillion\n') # 56
#    elif curr >= 10**174 and curr < 10**177:
#       f.write('Septenquinquagintillion\n') # 57
#    elif curr >= 10**177 and curr < 10**180:
#       f.write('Octoquinquagintillion\n') # 58
#    elif curr >= 10**180 and curr < 10**183:
#       f.write('Novemquinquagintillion\n') # 59
#    elif curr >= 10**183 and curr < 10**186:
#       f.write('Sexagintillion\n') # 60
#    elif curr >= 10**186 and curr < 10**189:
#       f.write('Unsexagintillion\n') # 61
#    elif curr >= 10**189 and curr < 10**192:
#       f.write('Duosexagintillion\n') # 62
#    elif curr >= 10**192 and curr < 10**195:
#       f.write('Tresexagintillion\n') # 63
#    elif curr >= 10**195 and curr < 10**198:
#       f.write('Quattuorsexagintillion\n') # 64
#    elif curr >= 10**198 and curr < 10**201:
#       f.write('Quinsexagintillion\n') # 65
#    elif curr >= 10**201 and curr < 10**204:
#       f.write('Sexsexagintillion\n') # 66
#    elif curr >= 10**204 and curr < 10**207:
#       f.write('Septensexagintillion\n') # 67
#    elif curr >= 10**207 and curr < 10**210:
#       f.write('Octosexagintillion\n') # 68
#    elif curr >= 10**210 and curr < 10**213:
#       f.write('Novemsexagintillion\n') # 69
#    elif curr >= 10**213 and curr < 10**216:
#       f.write('Septuagintillion\n') # 70
#    elif curr >= 10**216 and curr < 10**219:
#       f.write('Unseptuagintillion\n') # 71
#    elif curr >= 10**219 and curr < 10**222:
#       f.write('Duoseptuagintillion\n') # 72
#    elif curr >= 10**222 and curr < 10**225:
#       f.write('Treseptuagintillion\n') # 73
#    elif curr >= 10**225 and curr < 10**228:
#       f.write('Quattuorseptuagintillion\n') # 74
#    elif curr >= 10**228 and curr < 10**231:
#       f.write('Quinseptuagintillion\n') # 75
#    elif curr >= 10**231 and curr < 10**234:
#       f.write('Sexseptuagintillion\n') # 76
#    elif curr >= 10**234 and curr < 10**237:
#       f.write('Septenseptuagintillion\n') # 77
#    elif curr >= 10**237 and curr < 10**240:
#       f.write('Octoseptuagintillion\n') # 78
#    elif curr >= 10**240 and curr < 10**243:
#       f.write('Novemseptuagintillion\n') # 79
#    elif curr >= 10**243 and curr < 10**246:
#       f.write('Octogintillion\n') # 80
#    elif curr >= 10**246 and curr < 10**249:
#       f.write('Unoctogintillion\n') # 81
#    elif curr >= 10**249 and curr < 10**252:
#       f.write('Duooctogintillion\n') # 82
#    elif curr >= 10**252 and curr < 10**255:
#       f.write('Treoctogintillion\n') # 83
#    elif curr >= 10**255 and curr < 10**258:
#       f.write('Quattuoroctogintillion\n') # 84
#    elif curr >= 10**258 and curr < 10**261:
#       f.write('Quinoctogintillion\n') # 85
#    elif curr >= 10**261 and curr < 10**264:
#       f.write('Sexoctogintillion\n') # 86
#    elif curr >= 10**264 and curr < 10**267:
#       f.write('Septenoctogintillion\n') # 87
#    elif curr >= 10**267 and curr < 10**270:
#       f.write('Octooctogintillion\n') # 88
#    elif curr >= 10**270 and curr < 10**273:
#       f.write('Novemoctogintillion\n') # 89
#    elif curr >= 10**273 and curr < 10**276:
#       f.write('Nonagintillion\n') # 90
#    elif curr >= 10**276 and curr < 10**279:
#       f.write('Unnonagintillion\n') # 91
#    elif curr >= 10**279 and curr < 10**282:
#       f.write('Duononagintillion\n') # 92
#    elif curr >= 10**282 and curr < 10**285:
#       f.write('Trenonagintillion\n') # 93
#    elif curr >= 10**285 and curr < 10**288:
#       f.write('Quattuornonagintillion\n') # 94
#    elif curr >= 10**288 and curr < 10**291:
#       f.write('Quinnonagintillion\n') # 95
#    elif curr >= 10**291 and curr < 10**294:
#       f.write('Sexnonagintillion\n') # 96
#    elif curr >= 10**294 and curr < 10**297:
#       f.write('Septennonagintillion\n') # 97
#    elif curr >= 10**297 and curr < 10**300:
#       f.write('Octononagintillion\n') # 98
#    elif curr >= 10**300 and curr < 10**303:
#       f.write('Novemnonagintillion\n') # 99
#    elif curr >= 10**303 and curr < 10**306:
#       f.write('Centillion\n') # 100
#    elif curr >= 10**306 and curr < 10**309:
#       f.write('Uncentillion\n') # 101
#    elif curr >= 10**309 and curr < 10**312:
#       f.write('Duocentillion\n') # 102
#    elif curr >= 10**312 and curr < 10**315:
#       f.write('Trecentillion\n') # 103
#    elif curr >= 10**315 and curr < 10**318:
#       f.write('Quattuorcentillion\n') # 104
#    elif curr >= 10**318 and curr < 10**321:
#       f.write('Quincentillion\n') # 105
#    elif curr >= 10**321 and curr < 10**324:
#       f.write('Sexcentillion\n') # 106
#    elif curr >= 10**324 and curr < 10**327:
#       f.write('Septencentillion\n') # 107
#    elif curr >= 10**327 and curr < 10**330:
#       f.write('Octocentillion\n') # 108
#    elif curr >= 10**330 and curr < 10**333:
#       f.write('Novemcentillion\n') # 109
#    elif curr >= 10**333 and curr < 10**336:
#       f.write('Decicentillion\n') # 110
#    elif curr >= 10**336 and curr < 10**339:
#       f.write('Undecicentillion\n') # 111
#    elif curr >= 10**339 and curr < 10**342:
#       f.write('Duodecicentillion\n') # 112
#    elif curr >= 10**342 and curr < 10**345:
#       f.write('Tredecicentillion\n') # 113
#    elif curr >= 10**345 and curr < 10**348:
#       f.write('Quattourdecicentillion\n') # 114
#    elif curr >= 10**348 and curr < 10**351:
#       f.write('Quindecicentillion\n') # 115
#    elif curr >= 10**351 and curr < 10**354:
#       f.write('Sexdecicentillion\n') # 116
#    elif curr >= 10**354 and curr < 10**357:
#       f.write('Septendecicentillion\n') # 117
#    elif curr >= 10**357 and curr < 10**360:
#       f.write('Octodecicentillion\n') # 118
#    elif curr >= 10**360 and curr < 10**363:
#       f.write('Novemdecicentillion\n') # 119
#    elif curr >= 10**363 and curr < 10**366:
#       f.write('120-illion\n') # 120
#    else:
#       f.write('Unknown\n')

#    f.write('{:,}\n'.format(curr))
#    old_curr = curr
#    curr = prev + curr
#    prev = old_curr
# f.close()


#Viginticentillion, 
#Unviginticentillion, 
#Duoviginticentillion, 
#Tresviginticentillion, 
#Quattuorviginticentillion, 
#Quinviginticentillion, 
#Sexviginticentillion, 
#Septenviginticentillion, 
#Octoviginticentillion, 
#Novemviginticentillion, 
#Trigintacentillion, 
#Untrigintacentillion, 
#Duotrigintacentillion, 
#Trestrigintacentillion, 
#Quattuortrigintacentillion, 
#Quintrigintacentillion, 
#Sextrigintacentillion, 
#Septentrigintacentillion, 
#Octotrigintacentillion, 
#Novemtrigintacentillion, 
#Quadragintacentillion, 
#Unquadragintacentillion, 
#Duoquadragintacentillion, 
#Tresquadragintacentillion, 
#Quattuorquadragintacentillion, 
#Quinquadragintacentillion, 
#Sexquadragintacentillion, 
#Septenquadragintacentillion, 
#Octoquadragintacentillion, 
#Novemquadragintacentillion, 
#Quinquagintacentillion, 
#Unquinquagintacentillion, 
#Duoquinquagintacentillion, 
#Tresquinquagintacentillion, 
#Quattuorquinquagintacentillion, 
#Quinquinquagintacentillion, 
#Sexquinquagintacentillion, 
#Septenquinquagintacentillion, 
#Octoquinquagintacentillion, 
#Novemquinquagintacentillion
#Sexagintacentillion, 
#Unsexagintacentillion, 
#Duosexagintacentillion, 
#Tresexagintacentillion, 
#Quattuorsexagintacentillion, 
#Quinsexagintacentillion, 
#Sexsexagintacentillion, 
#Septensexagintacentillion, 
#Octosexagintacentillion, 
#Novemsexagintacentillion, 
#Septuagintacentillion, 
#Unseptuagintacentillion, 
#Duoseptuagintacentillion, 
#Treseptuagintacentillion, 
#Quattuorseptuagintacentillion, 
#Quinseptuagintacentillion, 
#Sexseptuagintacentillion, 
#Septenseptuagintacentillion, 
#Octoseptuagintacentillion, 
#Novemseptuagintacentillion, 
#Octogintacentillion, 
#Unoctogintacentillion, 
#Duooctogintacentillion, 
#Treoctogintacentillion, 
#Quattuoroctogintacentillion, 
#Quinoctogintacentillion, 
#Sexoctogintacentillion, 
#Septenoctogintacentillion, 
#Octooctogintacentillion, 
#Novemoctogintacentillion, 
#Nonagintacentillion, 
#Unnonagintacentillion, 
#Duononagintacentillion, 
#Trenonagintacentillion, 
#Quattuornonagintacentillion, 
#Quinnonagintacentillion, 
#Sexnonagintacentillion, 
#Septennonagintacentillion, 
#Octononagintacentillion, 
#Novemnonagintacentillion,
# Ducentillon # 200-illion 10**603

# Trecentillion # 300-illion 10**903

# Duotrigintatrecentillion # ?-illion 10**999

# Quadringentillion # 400-illion 10**1203

# Quingentillion # 500-illion 10**1503

# Sescentillion # 600-illion 10**1803

# Septuagintisescentillion # ?-illion 10**2013

# Septingentillion # 700-illion 10**2103

# Octingentillion # 800-illion 10**2403

# Nongentillion # 900-illion 10**2703

# Millillion # 1000-illion 10**3003

# Dumillillion # 2000-illion 10**6003



# 0 1 1
# 0 1 1 2
# 0 1 1 2 3
# 0 1 1 2 3 5
# 0 1 1 2 3 5 8

# n = 5
# prev = 0
# curr = 1
# print(0)
# i = 0
# while i < n - 1:
#    print(curr)
#    old_curr = curr
#    curr = prev + curr
#    prev = old_curr
#    i += 1
# print('\n')

# n = 1
# prev = 0
# curr = 1
# print(0)
# i = 0
# while i < n - 1:
#    if n > curr:
#       print(curr)
#    old_curr = curr
#    curr = prev + curr
#    prev = old_curr
#    i += 1
# print('\n')

# prev = 0
# curr = 1
# for i in range(0, 100):
#    print(curr)
#    old_curr = curr
#    curr = prev + curr
#    prev = old_curr
# print('\n')

#                        Group  = (000)
# Hundred        2     0 Group  = (100)
# Thousand       3     1 Group  = (1,000)
# Hun-Thousand   5     1 Group  = (100,000)
# Million        6     2 Groups = (1,000,000)
# Billion        9     3 Groups = (1,000,000,000)
# Trillion      12     4 Groups
# Quadrillion   15     5 Groups
# Quintillion   18     6 Groups = 10^18
# Sextillion    21     7 Groups
# Septillion    24     8 Groups
# Octillion     27     9 Groups
# Nonillion     30    10 Groups
# Decillion     33    11 Gruops = 10^33
# Undecillion   36    12 Groups
# Googol       100
# Centrillion  303   101 Groups (Largest illion)