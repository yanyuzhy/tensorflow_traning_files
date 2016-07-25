
#Score1 = "9163984??????????????509234539??????????????8984598234981????834259328454324"
#Score2 = "???9488734?98??????????????32987534731876???????????????35738723897???????32"

f = open("B-large-practice.in")

times = int(f.readline())
for t in range(times):
    Score = f.readline()[:-1]

    Score1 = Score[:Score.index(' ')]
    Score2 = Score[Score.index(' ') + 1 : ]
    #Score1 = '5??4'
    #Score2 = '7?07'
    Score1 = list(Score1)
    Score2 = list(Score2)

    Score1_dig = ''
    Score1_dig_n = ''
    Score2_dig = ''
    Score2_dig_n = ''

    for i in range(len(Score1)):
        Score1_dig = Score1[i]
        Score2_dig = Score2[i]
        if i < len(Score1) - 1:
            Score1_dig_n = Score1[i+1]
            Score2_dig_n = Score2[i+1]
        else:
            Score1_dig_n = '0'
            Score2_dig_n = '0'
        if i > 0:
            Score1_dig_p = int(Score1[i-1]) + Score1_dig_p * 10
            Score2_dig_p = int(Score2[i-1]) + Score2_dig_p * 10
        else:
            Score1_dig_p = 0
            Score2_dig_p = 0



        if '?' == Score1_dig and '?' == Score2_dig:
            if Score1_dig_p == Score2_dig_p:
                if '?' == Score1_dig_n or '?' == Score2_dig_n:
                    Score1[i] = '0'
                    Score2[i] = '0'
                elif int(Score1_dig_n) - int(Score2_dig_n) >= -5 and int(Score1_dig_n) - int(Score2_dig_n) <= 5:
                    Score1[i] = '0'
                    Score2[i] = '0'
                elif int(Score1_dig_n) - int(Score2_dig_n) >= 5:
                    Score1[i] = '0'
                    Score2[i] = '1'
                elif int(Score1_dig_n) - int(Score2_dig_n) <= -5:
                    Score1[i] = '1'
                    Score2[i] = '0'
            elif Score1_dig_p > Score2_dig_p:
                Score1[i] = '0'
                Score2[i] = '9'
            elif Score1_dig_p < Score2_dig_p:
                Score1[i] = '9'
                Score2[i] = '0'


        elif '?' == Score1_dig and '?' != Score2_dig:
            if Score1_dig_p == Score2_dig_p:
                if '?' == Score1_dig_n or '?' == Score2_dig_n:
                    Score1[i] = Score2[i]
                elif int(Score1_dig_n) - int(Score2_dig_n) >= -5 and int(Score1_dig_n) - int(Score2_dig_n) <= 5:
                    Score1[i] = Score2[i]
                elif int(Score1_dig_n) - int(Score2_dig_n) >= 5:
                    Score1[i] = str((int(Score2[i]) - 1) % 10)
                elif int(Score1_dig_n) - int(Score2_dig_n) <= -5:
                    Score1[i] = str((int(Score2[i]) + 1) % 10)
            elif Score1_dig_p > Score2_dig_p:
                Score1[i] = '0'
            elif Score1_dig_p < Score2_dig_p:
                Score1[i] = '9'


        elif '?' != Score1_dig and '?' == Score2_dig:
            if Score1_dig_p == Score2_dig_p:
                if '?' == Score1_dig_n or '?' == Score2_dig_n:
                    Score2[i] = Score1[i]
                elif int(Score1_dig_n) - int(Score2_dig_n) >= -5 and int(Score1_dig_n) - int(Score2_dig_n) <= 5:
                    Score2[i] = Score1[i]
                elif int(Score1_dig_n) - int(Score2_dig_n) >= 5:
                    Score2[i] = str((int(Score1[i]) + 1) % 10)
                elif int(Score1_dig_n) - int(Score2_dig_n) <= -5:
                    Score2[i] = str((int(Score1[i]) - 1) % 10)
            elif Score1_dig_p > Score2_dig_p:
                Score2[i] = '9'
            elif Score1_dig_p < Score2_dig_p:
                Score2[i] = '0'

    Str1 = ''
    Str2 = ''

    for i in Score1:
        Str1 = Str1 + i
    for i in Score2:
        Str2 = Str2 + i

    print "Case #%d: %s %s" % (t + 1, Str1, Str2)
    #print Str1, Str2
