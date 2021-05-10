from django.shortcuts import render
import requests
import bs4
from django.contrib import messages

# Create your views here.

def index(request):
    image = None
    if request.method == "POST":
        url = request.POST.get('url')
        if url != "":
            first = url[:29]
            second = url[:25]
            third = url[:30]
            print(third)
            first_condition = "https://in.pinterest.com/pin/"
            second_condition = "in.pinterest.com/pin/"
            third_condition = "https://www.pinterest.com/pin/"
            if first==first_condition or second==second_condition or third==third_condition:
                response = requests.get(url)
                bs = bs4.BeautifulSoup(response.content, "html.parser")
                formatted_text = bs.prettify()
                # print(formatted_text)
                lits_meta = bs.find_all('link')
                # total = len(lits_meta)
                # print(lits_meta[8]['href'])
                try :
                  image = lits_meta[8]['href']
                except:
                    messages.error(request, "Sorry, Try again later....")
            else:
                messages.error(request, "Please enter a valid  pinterest image link.....")
        else:
            messages.error(request, "Please enter the pinterest image link....")
    context = {'image':image}
    return render(request, 'index.html', context)
