import calendar

from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenge_by_number(request, month):
    month_name = str(calendar.month_name[month]).lower()
    challenge_text = monthly_challenges(request, month_name)
    return HttpResponseNotFound(challenge_text)


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no met the entire month!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day"
    elif month == "april":
        challenge_text = "Eat no met the entire month4!"
    elif month == "may":
        challenge_text = "Eat no met the entire month5!"
    elif month == "june":
        challenge_text = "Eat no met the entire month6!"
    elif month == "july":
        challenge_text = "Eat no met the entire month7!"
    elif month == "august":
        challenge_text = "Eat no met the entire month8!"
    elif month == "september":
        challenge_text = "Eat no met the entire month9!"
    elif month == "october":
        challenge_text = "Eat no met the entire month10!"
    elif month == "november":
        challenge_text = "Eat no met the entire month11!"
    elif month == "december":
        challenge_text = "Eat no met the entire month12!"
    else:
        return HttpResponseNotFound("This month is no supported!")
    return HttpResponse(challenge_text)
