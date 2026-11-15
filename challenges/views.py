from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january" : 'January Challenge',
    "february" : 'february Challenge',
    "march" : 'march Challenge',
    "april" : 'april Challenge',
    "may" : 'may Challenge',
    "june" : 'june Challenge',
    "july" : 'july Challenge',
    "august" : 'august Challenge',
    "september" : 'september Challenge',
    "october" : 'october Challenge',
    "november" : 'november Challenge',
    "december" : 'december Challenge',
}

def index(request):

    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge',args=[month])
        list_items += f'<li><a href=\"{month_path}\">{capitalized_month}</a></li>'

    response_data = f'''
    <ul>
    {list_items}
    </ul>
'''
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        try:
            redirect_month = months[month-1]
            redirect_path = reverse('month-challenge', args=[redirect_month])
            return HttpResponseRedirect(redirect_path)
        except:
            return HttpResponseNotFound('<h1>This month is not supported!</h1>')
    else:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>!')


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')