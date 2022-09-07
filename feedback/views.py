from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from feedback.models import Feedback, Category
from .forms import AddFeedback


class FeedbackHome(ListView):
    """ Главная страница """
    model = Feedback
    template_name = 'feedback/home.html'
    context_object_name = 'feedbacks'

    def get_queryset(self):
        return Feedback.objects.all().order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super(FeedbackHome, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['category_selected'] = 0
        context['categories'] = Category.objects.all()
        return context


def about(request):
    """ Страница о сайте """
    return render(request, 'feedback/about.html', context={'title': 'О сайте'})


class FeedbackAdd(LoginRequiredMixin, CreateView):
    """ Страница добавления отзыва """
    form_class = AddFeedback
    success_url = reverse_lazy('fb-home')
    template_name = 'feedback/add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FeedbackAdd, self).get_context_data(**kwargs)
        context['title'] = 'Добавить отзыв'
        context['category'] = Category.objects.all()
        return context


class FeedbackDetail(DetailView):
    """ Страница отображения отзыва и комментариев к нему """
    model = Feedback
    template_name = 'feedback/detail.html'
    slug_url_kwarg = 'fb_slug'
    context_object_name = 'feedback'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FeedbackDetail, self).get_context_data(**kwargs)
        context['title'] = 'Отзыв'
        return context


class FeedbackCategory(ListView):
    """ Страница отображения отзывов по выбранной категории """
    model = Feedback
    template_name = 'feedback/home.html'
    context_object_name = 'feedbacks'

    def get_queryset(self):
        feedbacks = Feedback.objects.filter(category_id=self.kwargs['category_pk'])
        if len(feedbacks) == 0:
            raise Http404()
        return feedbacks

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FeedbackCategory, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['category_selected'] = self.kwargs['category_pk']
        context['categories'] = Category.objects.all()
        return context

