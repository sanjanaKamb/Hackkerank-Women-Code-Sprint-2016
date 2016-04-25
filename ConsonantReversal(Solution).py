# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
vowels = 'aeiou'
for i in range(0,n):
    s1 = raw_input().strip()
    word_consonants = [x for x in s1 if x not in vowels]
    word_consonants.reverse()
    s2 = [word_consonants.pop(0) if x not in vowels else x for x in s1 ]
    print ''.join(s2)