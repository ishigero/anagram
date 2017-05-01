import sys

def _permutation(w):
    length = len(w)
    if(length == 1):
        return [w]

    ret = []
    for i in range(length):
        character =  w[i]
        other = w[0:i] + w[i + 1:]
        for j in _permutation(other):
            ret.append(character + j)
    return ret


def _search(a_l, w_l):
    ret = []    
    while a_l:
        if a_l[0] in w_l:
            ret.append(a_l[0])
            w_l.remove(a_l[0])
        del a_l[0]
    return ret


f = open('words.txt')
#f = open('test.txt')
word_list = f.read().splitlines()
while word_list:       
    anagram_list = _permutation(word_list[0])
    ret = _search(anagram_list, word_list)
    #自分自身しかない場合、1になる
    if len(ret) >= 2:
        print(ret)





