import Queue
f = open("A-large-practice.in")
#f2 = open('')
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
    Str = 'ISXRESZNRTRNRRREOVIRNGGNIEHGHOREEVIVORRINUINEXUIHOHEERINEFEVVIIOIHFIFEWTSNNREOZNOHTEEEEZHEIIEWUXNOROOHZEOSFETSORTSIEXTVEEWOSNOROIEHNZVOTHEVTTSXVIWTHTEEHWOGOOEHINRFINNFTRNERFIEFUNREVHFOWEUEEENVORVFIOEXEUZVOTTRZENIIFGONIEVEEVUEVFRZISNIENZOWEOOOGZHEIHIRIRXEONEENOERUOIETUEEEFIFNGOOEEOOEISOUNENNXOSEREREFGEIEEEEWIOOXHWNNTTEINERENOEREVTRRHTEENOITOGOROTHETNVSENFVITFRXOTZSZNFHNIIFIEIXTEFGWGENEETVEWTSNIRTTFEEFNXISWGEOIESEEEROHFWFWTNENHNTTFITIOIZGEEISNUEWZIOVOEOSWOOEZENHVHEOOISSFEEIITGFTNORSERRFUFNTRTOIETTRFTHEEETEHHOEEUEFROTOZRZEEZIEEINEOEIXFETEVFEEOIEIHVEHSISETETZEUIEOIOFXOZOOVNEOEWHHOTEFSSIOHIESNIHFVITEEEENHOITEGSIOFFNFNENXUESTHREIOUZOEEGHRRRIRFFREGSTFNZFEENSOITNHISEROVGRGEEOVIEGTFTTNUNFEZOEOOHHNTOOESORGZHEZOOOFESVSUIRIONEEEEGISETTOEVVEETZNOTIEXEVESRXEIIRFEETRFNTNIREFENGEWTONOREVEHOEEEFOGORNZISNRZERIIOITRNIOHEEOEEFOTEORENTESUINNNIEFFNNNEEOEFEFENSONSTVTIEOVVNOFSOEOTUUEZSTFHTFEREHUNGVHTOHETERVHRHFEEETSENIIEIESXHNNEITITSNERUEIVEERVTWTEOOGFNENIEERTTRNNRGFIINOVEEENEITNENTTFIOSEZEXNRNHFSXEENWEUEFOHETIETSIIFNOEORTEVEONRHWOGRSOEEHNNONGNRNOESHZVIEOSSROEHRFGEOTEVETRFEHUIENRUXENTOTRIGEIZOREESIFTVSHRWOIXNVETIEIGEVNERWTESREOETHEFRNNRONNTSVRVIENEFRNEGWTWEFUVXRWXNVVESEUZGVEETEIWORXEGHVWEIHTNOSEZRIHERSNZVHIEEETENINEEHXWEIUTSUITVEEIEOUIOIHGENERZVINZNNEIXXNOTORIREVTVTNEREIOIENXGEINOZOVWRSTVFONEFOSSVREITEENORWNNSEVIEINUREOEUROROIESUFERFUOGIEEHZIOSERESEVTEIROSVFEEFEEOEFVWOEFEVOEVHETSINIIEFWNHZEUESNIFOUZXNREREXFEEZEVOHRRNITTWIEVVNWEEEUIVEXVRTVISOXVIRNIVOVERUEESVETOVINITGENEETTTENIENIXEVNZOVRRXNREHSVTEEEIVTRIHENERNTHRXIFFETIGHETOOIRWUONWGNREFHRTIHIINIRGENEOIONRFSVFEUNIFEEEOOZIIIHWNVEENIETEGZENSHEEEOVEWNEZISHXXGXTEEHOEEIHVTSWESSROUNSOEOENTUNFESOERZETSWERIIORIOINNNERFRVRIVSETERXEEINRNNINTSOOTFIUVEROSEORTOTWNHHNIONEEORENIWOEWWEENOIXEITNVNEGEEEEEXFEOHEEEETGITEVEXRRXVTTHHEHEEEEEHISHEEUFERRNNTOIXZNTEIEUNRUEEEENEREEEVNNEEEGNTESIRSIEFFIFTEOEWVOOOFWEGREEVEHNSZHXOHIONIHEIEUVOOTEOTEOIXZIEGEEENSEEIETUNTVVONNRRFNOOIISNXHEWIWISNEOTENNHIEFNSHHSEEHNNNESIXTHOTERRRROSEEOEUESEHWEENEXOESOTOEINGHEEISESEIFVITINRHNTEO'
    #count the symbols of the input string
    O = Str.count('O')
    N = Str.count('N')
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

    one = O
    O = O - one
    N = N - one
    E = E -one

    three = T
    T = T - three
    H = H - three
    R = R - three
    E = E - 2*three

    five = F
    F = F - five
    I = I - five
    V = V - five
    E = E - five

    seven = S
    S = S - seven
    E = E - 2*seven
    V = V -seven
    N = N -seven


    nine = I
    N = N - 2*nine
    I = I - nine
    E = E - nine

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

    max_num_list = [onemin,threemin,fivemin,sevenmin,ninemin]

    # calculate another numbers

    lost_letters = len(Str) - zero * 4 - two * 3 - four * 4 - six * 3 - eight * 5
    min_num = lost_letters / 5
    max_num = lost_letters / 3

    solution = [0,0,0,0,0,0]#define the solution the last num is the i_layer
    i_layer = 0
    q = Queue.Queue()#define the FIFO Queue
    q.put(solution)
    flag_bingo = 0
    while False is q.empty():
        solution = q.get()
        for j in range(max_num_list[solution[-1]]+1):
            solution[solution[-1]] = j
            #check whether the new_solution_node is legal
            Str1 = solution[0] * ONE + solution[1] * THREE + solution[2] * FIVE + solution[3] * SEVEN + solution[4] * NINE + zero * ZERO + two * TWO + four * FOUR + six * SIX + eight * EIGHT
            Str1 = sorted(Str1)
            if Str1 == sorted(Str):
                flag_bingo = 1
                break
            flag_mini = 1
            for letter in 'ONETWHRFUIVSXGZ':
                if Str1.count(letter) > Str.count(letter):
                    flag_mini = 0
                    break
            if flag_mini == 1:
                child_solution = solution[:]
                child_solution[-1] = child_solution[-1] + 1
                if child_solution[-1] > 4:
                    child_solution[-1] = 4
                q.put(child_solution)
        if flag_bingo == 1:
            #print solution, t
            num_str = zero * '0' + solution[0] * '1' + two * '2' + solution[1] * '3' + four * '4' + solution[2] * '5' + six * '6' + solution[3] * '7' + eight * '8' + solution[4] *  '9'
            #print num_strs
            #strHello = "the length of (%s) is %d" % ('Hello World', len('Hello World'))

            print "Case #%d: %s" % (t+1, num_str)

            break

# first generate the child node for the first node in queue
#  then put the new child note in the queue
