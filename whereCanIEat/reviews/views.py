from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

from .models import Restaurant


def index(request):
    return render(request, 'reviews/index.html', {})

def city(request, city):
    restaurant_list = Restaurant.objects.filter(city_name=city.capitalize())
    str_list = map(str, restaurant_list)
    context = {'restaurant_list': str_list, 'city': city}
    return render(request, 'reviews/restaurants.html', context)

def add(request):
    return render(request, 'reviews/add.html')

def add(request):
    restauant = get_object_or_404(Restaurant, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
