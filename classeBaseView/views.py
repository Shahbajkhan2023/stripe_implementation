from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import GeeksModel
from .forms import GeeksForm


class GeeksCreate(CreateView):
    model = GeeksModel
    # fields = ['title', 'description']
    form_class = GeeksForm


class GeeksList(ListView):
    model = GeeksModel

    def get_queryset(self, *args, **kwargs):
        qs = super(GeeksList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs


class GeeksDetailView(DetailView):
    model = GeeksModel


class GeeksUpdateView(UpdateView):
    model = GeeksModel
    fields = [
        "title",
        "description"
    ]
    template_name = 'update_form.html'
    success_url = "/"


class GeeksDeleteView(DeleteView):
    model = GeeksModel
    success_url = "/"


class GeeksFormView(FormView):
    form_class = GeeksForm
    template_name = 'geeksmodel_form.html'
    success_url = "/thanks"