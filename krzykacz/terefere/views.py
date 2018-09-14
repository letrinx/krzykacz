from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from terefere import models, forms



class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class Home(View):
    def get(self, request):
        tweets = models.Tweet.objects.all()
        return render(request, "home.html")


class AddTweetView(View):
    def get(self, request):
        form = forms.AddTweetForm()
        return render(request, "add_tweet.html", {'form': form})
