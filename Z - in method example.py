def findDog(string):
    string.lower()
    sString = string.split()
    for s in sString:
        if s == 'dog':
            return True
        else:
            return False
# Nós transformamos esse método a cima em:

def findDog2(s):
    return 'dog' in s.lower().split()

dogFrase = 'Is there a dog here?'
print(findDog2(dogFrase))