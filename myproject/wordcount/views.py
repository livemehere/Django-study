from django.shortcuts import render

# Create your views here.


def wordcount(request):
    return render(request, "wordcount.html")


def result(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    word_dic = {}
    for word in wordlist:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    print(word_dic.items())
    return render(
        request, "result.html", {"wordlength": len(wordlist), "word_dic": word_dic}
    )
