from django.views.generic import ListView, DetailView
from .models import Fitness, Training
from django.urls import reverse


class Training(ListView):
    model = Fitness
    template_name = 'fitness/training.html'
    context_object_name = 'fitness'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Фитнес'

        return context


class TypeOfTraining(DetailView):
    model = Training
    template_name = 'fitness/type_of_training'
    context_object_name = 'fitness'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['fitness']
        return context

    def get_absolut_url(self):
        return reverse('fitness', kwargs={'fitness_slug': self.slug})
