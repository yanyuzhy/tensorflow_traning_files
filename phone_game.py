f = open("A-small-practice.in")
Times = int(f.readline())
ZERO = "ZERO"
ONE = "ONE"
TWO = "TWO"
THREE = "THREE"
FOUR = "FOUR"
FIVE = "FIVE"
SIX = "SIX"
SEVEN = "SEVEN"
EIGHT = "EIGHT"
NINE = "NINE"

for t in range(Times):

    Str = "RTEERTEVRHEEEHTSEEHNEIGHT"
    Str = "ENRTENHOETEOOOWEN"
    Str = "RTEERTEVRHEEEHTSEEHNEIGHT"
    Str = f.readline()[:-1]
    #count the symbols of the input string
    O = Str.count('O')
    N = Str.count('E')
    E = Str.count('E')
    T = Str.count('T')
    W = Str.count('W')
    H = Str.count('H')
    R = Str.count('R')
    F = Str.count('F')
    U = Str.count('U')
    I = Str.count('I')
    V = Str.count('V')
    S = Str.count('S')
    X = Str.count('X')
    G = Str.count('G')
    Z = Str.count('Z')



    #zero and two are the special numbers because of the letter 'W' and 'z', so the zero count is
    # cacluate the special numbers

    zero = Z
    Z = Z - zero
    E = E - zero
    R = R - zero
    O = O - zero

    two = W
    T = T - two
    W = W - two
    O = O - two

    four = U
    F = F - four
    O = O - four
    U = U - four
    R = R - four

    six = X
    S = S - six
    I = I - six
    X = X - six

    eight = G
    E = E - eight
    I = I - eight
    G = G - eight
    H = H - eight
    T = T - eight

    #calculate the number in string

    #caculate the number max
    onemin = min(O, N, E)
    #caculate the number two
    twomin = min(T, W, O)
    #caclute the number three
    threemin = min(T, R, E/2)
    #caclute the number four
    fourmin = min(F, O, U, R)
    #caclute the number five
    fivemin = min(F, I, V, E)
    #caclute the number six
    sixmin = min(S, I, X)
    #caclute the number seven
    sevenmin = min(S, E/2, V, N)
    #caclute the number eight
    eightmin = min(E, I, G, H, T)
    #caclute the number nine
    ninemin = min(N/2, I, E)
    #caclute the number zero
    zeromin = min(Z, E, R, O)

    # calculate another numbers

    lost_letters = len(Str) - zero * 4 - two * 3 - four * 4 - six * 3 - eight * 5
    min_num = lost_letters / 5
    max_num = lost_letters / 3

    solution = [0,0,0,0,0]
    i = 0
    while i <= max_num ** 5:
    #for i in range(max_num ** 5):
        #print solution
        #print one, two, three, four, five, six, seven, eight, nine, zero
        i_num = i
        i = i + 1
        # code the i
        for j in range(0,5,1):
            solution[j] = i_num % max_num
            i_num = i_num /max_num

        if sum(solution) >= min_num and sum(solution) <= max_num:
            letter_count = solution[0] * len(ONE) + solution[1] * len(THREE) + solution[2] * len(FIVE) + solution[3] * len(SEVEN) + solution[4] * len(NINE)
            if lost_letters == letter_count:
                Str1 = solution[0] * ONE + solution[1] * THREE + solution[2] * FIVE + solution[3] * SEVEN + solution[4] * NINE + zero * ZERO + two * TWO + four * FOUR + six * SIX + eight * EIGHT
                Str1 = sorted(Str1)
                if Str1 == sorted(Str):
                    one = solution[0]
                    three = solution[1]
                    five = solution[2]
                    seven = solution[3]
                    nine = solution[4]
                    break
                else:
                    continue
            else:
                continue
        else:
            continue
    print one,two,three,four,five,six,seven,eight,nine,zero
