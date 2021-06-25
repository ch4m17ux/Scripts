#/usr/bin/python2
#coding = utf - 8
import codec
import string

tbl = {
    "AAAAA": "a",
    "AAAAB": "b",
    "AAABA": "c",
    "AAABB": "d",
    "AABAA": "e",
    "AABAB": "f",
    "AABBA": "g",
    "AABBB": "h",
    "ABAAA": "i",
    "ABAAB": "j",
    "ABABA": "k",
    "ABABB": "l",
    "ABBAA": "m",
    "ABBAB": "n",
    "ABBBA": "o",
    "ABBBB": "p",
    "BAAAA": "q",
    "BAAAB": "r",
    "BAABA": "s",
    "BAABB": "t",
    "BABAA": "u",
    "BABAB": "v",
    "BABBA": "w",
    "BABBB": "x",
    "BBAAA": "y",
    "BBAAB": "z"
}

def decode_bacon(dt):
    splt = [dt[i: i + 5]
        for i in range(0, len(dt), 5)
    ]
cc = ""
for ss in splt:
    print ss
cc += tbl[ss]
print cc
return cc
d = codecs.open("english_breakfast.txt", "rb", encoding = 'utf-8').read()
caps = u "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙"
norm = string.ascii_lowercase + string.ascii_uppercase
p4 = ""
unpart4 = ""
for i in d:
    c = i
ii = caps.find(i)
if ii != -1:
    p4 += 'B'
c = norm[ii]
else :
    p4 += 'A'
unpart4 += c
p3 = ""
unpart3 = ""
for i in unpart4:
    c = i
if c in string.ascii_uppercase:
    p3 += 'B'
c = string.lower(c)
else :
    p3 += 'A'
unpart3 += c
p2 = ""
for i in unpart3:
    if (ord(i) - ord('a')) % 2 == 0:
        p2 += 'A'
    else :
        p2 += 'B'
p1 = ""
for i in unpart3:
    if (ord(i) - ord('a')) < 13:
        p1 += 'A'
    else :
        p1 += 'B'
print decode_bacon(p1) + decode_bacon(p2) + decode_bacon(p3) +
    decode_bacon(p4)
