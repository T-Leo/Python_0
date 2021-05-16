def cpt_letters(words):
    uppercase = ''
    for lowercase in words:
        lowercase = lowercase[0].upper() + lowercase[1:]
        uppercase += lowercase + ' '
    return uppercase


wordX = input('enter words, use lowercase- ')
print(cpt_letters(wordX.split()))
