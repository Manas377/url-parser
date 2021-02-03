from django.shortcuts import render, redirect, get_object_or_404
from forms.forms import Form
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import csv
from .models import FrequentWords
from collections import Counter
from django.contrib import messages



def blackllist_generator():
    results = []
    with open('most_used_words.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row[0])

    return results


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def max_word_counter(lst):
    words = set(lst)
    counter = []
    for word in words:
        print(f"Frequency of {word} is {lst.count(word)}")


def word_save(url, word_list):
    FrequentWords.objects.create(URL=url,
                                  word_1=word_list[0],
                                  word_2=word_list[1],
                                  word_3=word_list[2],
                                  word_4=word_list[3],
                                  word_5=word_list[4],
                                  word_6=word_list[5],
                                  word_7=word_list[6],
                                  word_8=word_list[7],
                                  word_9=word_list[8],
                                  word_10=word_list[9])
    return None



def frequency(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            url = form.data["url"]
            try:
                job_done = FrequentWords.objects.get(URL=url)
            except:
                job_done = None
            if job_done:
                messages.add_message (request, messages.INFO, 'This Data was Pre-Fetched')
                request.session['url'] = url
                return redirect ('result')
            else:
                data = requests.get(url)
                html_page = data.content
                soup = BeautifulSoup(html_page, 'html.parser')
                text = soup.find_all(text=True)
                visible_text = filter (tag_visible, text)
                output = u" ".join(t.strip() for t in visible_text)
                output.casefold()
                output = list(output.split())
                final = []
                black_list = blackllist_generator()
                for i in range(len(output)):
                    if output[i] in black_list:
                        continue
                    else:
                        final.append(output[i])
                most_used_tuple = Counter(final).most_common(10)
                most_used_array = []
                for i, j in most_used_tuple:
                    most_used_array.append (f"Count of \"{i}\" was at {j}")
                word_save(url, most_used_array)
                request.session['url'] = url
                return redirect('result')

    form = Form()
    return render(request, 'home.html', {"form": form})


def result(request):

    url = request.session.get('url')
    word_list = get_object_or_404(FrequentWords, URL = url)
    if word_list:
        print("this was get req")
        context = {
            'data' : word_list
        }
        return render(request, template_name='result.html', context=context)
    else:
        print ("This was post req")
        url = request.session.get('URL')
        request.session.delete('URL')
        data_object = get_object_or_404(FrequentWords, URL=url)
        return render(request, template_name='result.html', context={'data': data_object})











# def result(request):
#     if request.method == 'GET':
#         word_list = request.session.get('temp_data')
#         print("this was get req")
#         context = {
#             'data' : word_list
#         }
#         return render(request, template_name='result.html', context=context)
#     else:
#         url = request.session.get('url')
#         obj = get_object_or_404(FrequentWords, URL=url)
#         print("this was post req")
#         context = {
#             'data': obj
#         }
#         return render(request, 'result.html', context=context)

















symbols = ['{', '}', '[', ']', '(' , ')', '=','+', '===', '\'', '\"']
