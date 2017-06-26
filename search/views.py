from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import TagForm
from api.models import Tag
from search.instagram import InstagramSearch


class ManagementView(TemplateView):
    """ view for managing search items.

        NOTE: since this is just a test project, i created this
            view to manually fetch the result and save it in the
            database but it should be set in a realtime/background job
    """
    template_name = "search/management.html"

    def get(self, *args, **kwargs):
        form = TagForm()
        tags = Tag.objects.all()
        return render(self.request, self.template_name, {
            'form': form,
            'tags': tags
        })

    def post(self, *args, **kwargs):
        form = TagForm(self.request.POST)
        if form.is_valid():
            form.save()
            return redirect('management')

        return render(self.request, self.template_name, {'form': form})


class SearchView(InstagramSearch, TemplateView):
    """ view for searching based on tags
    """
    template_name = "search/search.html"

    def get(self, *args, **kwargs):
        tags = Tag.objects.all()
        return render(self.request, self.template_name, {
            'tags': tags,
            'data': self.search_by_tag(self.request.GET.get('tag')),
        })