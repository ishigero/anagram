# -*- coding: utf-8 -*

#元の単語とアルファベット順に並べ替えた単語を辞書で返す
def _make_word_set(w_l):
    word_set = []
    for word in w_l:
        tmp = list(word)
        tmp.sort()
        sorted_word = ''.join(tmp)
        ret = (word, sorted_word)
        word_set.append(ret)
    return dict(word_set)
 

#アルファベット順に並べ替えたアナグラムから重複するものを削除
def _delete_duplicated_anagram(w_s):
   ret = []
   for anagram in w_s.itervalues():
       ret.append(anagram)
   return list(set(ret))


def _search(w_s, a):
    while a:
        ret = []
        for raw_word, anagram in w_s.items():
            if anagram == a[0]:
                ret.append(raw_word)
        del a[0]
        if len(ret) >= 2:
            print(ret)
        ret = []


f = open('words.txt')
#f = open('test.txt')
word_list = f.read().splitlines()
word_set = _make_word_set(word_list)
anagrams = _delete_duplicated_anagram(word_set)
_search(word_set, anagrams)
