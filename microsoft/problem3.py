from collections import Counter
def getHint(secret,guess):

    lookup=Counter(secret)

    bull=0
    cow=0

    # this is for finding bull
    for i in range(len(guess)):

        if secret[i]==guess[i]:
            bull+=1

            lookup[secret[i]]-=1
    # now finding for cow

    for i in range(len(guess)):

        if guess[i] in lookup and secret[i]!=guess[i] and lookup[guess[i]]>0:
            cow+=1
            lookup[guess[i]]-=1

    return str(bull)+'A'+str(cow)+'B'

secret = "1807"
guess = "7810"
print(getHint(secret,guess))