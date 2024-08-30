from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges_dict: dict[str, str] = {
    "january": "Eat no meat the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat the entire month!",
    "may": "Eat no meat the entire month!",
    "june": "Eat no meat the entire month!",
    "july": "Eat no meat the entire month!",
    "august": "Eat no meat the entire month!",
    "september": "Since September it feels like December is coming!",
    "october": "Eat no meat the entire month!",
    "november": "Eat no meat the entire month!",
    "december": "Eat no meat the entire month!",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges_dict.keys())
    if 1 <= month <= 12:
        redirect_month = months[month - 1]
        redireth_path = reverse(
            "month-challenge", args=[redirect_month]
        )  # /challenges/january
        return HttpResponseRedirect(redireth_path)
    else:
        return HttpResponseNotFound("Invalid month number!")


# def monthly_challenge_by_number(request, month):
#    if 1 <= month <= 12:
#        month_name = calendar.month_name[month].lower()
#        challenge_text = monthly_challenges_dict.get(month_name)
#        return HttpResponse(challenge_text)
#    else:
#        return HttpResponseNotFound("This month is not supported!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
