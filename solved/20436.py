keyboard = {
    "q":(0,2),"w":(1,2),"e":(2,2),"r":(3,2),"t":(4,2),"y":(5,2),"u":(6,2),"i":(7,2),"o":(8,2),"p":(9,2),
    "a":(0,1),"s":(1,1),"d":(2,1),"f":(3,1),"g":(4,1),"h":(5,1),"j":(6,1),"k":(7,1),"l":(8,1),
    "z":(0,0),"x":(1,0),"c":(2,0),"v":(3,0),"b":(4,0),"n":(5,0),"m":(6,0)
    }


def calDist(keyboard,p1,p2):
    return abs(keyboard[p1][0]-keyboard[p2][0])+abs(keyboard[p1][1]-keyboard[p2][1])

def isLetterConsonant(keyboard, ch): #자음입니까???
    if ( (0 <= keyboard[ch][0] <= 3 and 0 <= keyboard[ch][1] <= 2) 
        or keyboard[ch] == (4,1) 
        or keyboard[ch] == (4,2) ):
        return True

sl, sr = input().split()
letters = input()

move_count = 0
for letter in letters:
    if isLetterConsonant(keyboard, letter): # 자음이면
        move_count += calDist(keyboard, sl,letter)
        sl = letter # update!!!
    else:
        move_count += calDist(keyboard, sr,letter)
        sr = letter # update!!!
    move_count +=1

print(move_count)
