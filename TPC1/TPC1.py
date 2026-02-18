#-------1.given a string “s”, reverse it.-------

def reverse(s):
    #s[start:stop:step]
    return s[::-1]

palavra="amor"
print(f"The reverse of palavra is: {reverse(palavra)}")



#-------2.given a string “s”, returns how many “a” and “A” characters are present in it.-------

def how_many(s,c):
    counter=0
    for character in s:
        if character.upper()==c.upper():
            counter+=1
    return counter

palavra_2="AMarA"
character="a"
print(f"The string {palavra_2} are {how_many(palavra_2,character)} {character} present")

def how_many_count(s,c):
    return s.lower().count(c)

print(f"The string {palavra_2} are {how_many_count(palavra_2,character)} {character} present (count)")

#contar todas os caracteres de uma string
from collections import Counter
def how_many_all(s):
    return Counter(s.lower())
print(how_many_all("AmaRa"))



#-------3.given a string “s”, returns the number of vowels there are present in it.-------

def vowels_number(s):
    vowels=["A","E","I","O","U"]
    #vowels="AEIOU"
    counter=0
    for character in s:
        if character.upper() in vowels:
            counter+=1
    return counter

palavra_3="chapeu"
print(f"The string {palavra_3} are {vowels_number(palavra_3)} vowels")

def vowels_number_2(s):
    return sum(1 for c in s if c.lower() in "aeiou")

print(f"The string {palavra_3} are {vowels_number_2(palavra_3)} vowels (sum)")


#-------4.given a string “s”, convert it into lowercase.-------
def convert_lower(s):
    return s.lower()
palavra_lower="AdMinstradOR"
print(f"The string {palavra_lower} in lower is {convert_lower(palavra_lower)}")

#without lower
def convert_lower_2(s):
    result=""
    for char in s:
        #first check if char is in upper
        if 'A'<=char<='Z':
            lower=ord(char)+32
            result+=chr(lower)
        #if char in lower just add
        else:
            result+=char
    return result

print(f"The string {palavra_lower} in lower is {convert_lower_2(palavra_lower)} (without lower)")


#-------5.given a string “s”,  convert it into uppercase.-------

def convert_upper(s):
    return s.upper()

palavra_upper="Amigo"
print(f"The string {palavra_upper} in uppercase is {convert_upper(palavra_upper)}")

def convert_upper_2(s):
    result=""
    for char in s:
        if 'a'<=char<='z':
            upper=ord(char)-32
            result+=chr(upper)
        else:
            result+=char
    return result

print(f"The string {palavra_upper} in uppercase is {convert_upper_2(palavra_upper)} (without upper)")



#-------6.Verifica se uma string é capicua-------
def capicua(s):
    reverse=s[::-1]
    cond=False
    if s.lower()==reverse.lower():
        cond=True
    return cond

palavra_capicua="Radar"
print(f"A palavra {palavra_capicua} {'é capicua' if capicua(palavra_capicua) else 'não é capicua.'}")



#-------7.Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão balanceadas se todos os caracteres de s1 estão presentes em s2.)
def balanceadas(s1,s2):
    cond=True
    for char in s1:
        if char not in s2:
            cond=False
            #return False
    return cond

string_1="amar"
string_2="aemaklr"
print(f"As strings {string_1} e {string_2} {'são balanceadas' if balanceadas(string_1,string_2) else 'não são balanceadas'}")

def balanceadas_set(s1,s2):
    return set(s1).issubset(set(s2))

#-------8. Calcula o número de ocorrências de s1 em s2-------
def ocorrencias(s1,s2):
    count= 0
    i=0
    ind=0
    while ind<len(s2):
        if s2[ind]==s1[i]:
            if i==len(s1)-1:
                count+=1
                i=0
            i+=1
            ind+=1
        else:
            i=0
    return count

s1="abc"
s2="ababcababc"
print(f"O numero de ocorrencias de {s1} em {s2} são: {ocorrencias(s1,s2)}")

def ocorrencias_count(s1,s2):
    return s2.count(s1)

print(f"O numero de ocorrencias de {s1} em {s2} são: {ocorrencias_count(s1,s2)} (count)")
        

#-------9. Verifica se s1 é anagrama de s2.
#          ○ "listen" e "silent": Deve imprimir True
#          ○ "hello", "world": Deve imprimir False
def anagrama(s1,s2):
    s1_counter= Counter(s1)
    s2_counter= Counter(s2)
    return s1_counter==s2_counter
print(anagrama("listen","silent"))
print(anagrama("hello","world"))
