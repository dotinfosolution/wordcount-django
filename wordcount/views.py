from  django.shortcuts import render
import operator

def rock (requests):
    return render(requests, 'home.html')

def count (requests):
    fulltext =requests.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist :
        if word in worddictionary:
            # Increase the number
            worddictionary [word] += 1
        else:
            #Add 
            worddictionary [word] = 1

        sortedword = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)


    return render(requests, 'count.html', {'fulltext':fulltext, 'wordlist':len(wordlist),'sortedword':sortedword })