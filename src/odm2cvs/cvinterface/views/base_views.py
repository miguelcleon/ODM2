from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from rdfserializer.api import *

# Vocabulary Basic Views
class DefaultVocabularyListView(ListView):
    vocabulary = None
    vocabulary_verbose = None
    vocabulary_def = None

    def __init__(self, **kwargs):
        self.vocabulary = kwargs['vocabulary']
        self.vocabulary_verbose = kwargs['vocabulary_verbose']
        self.vocabulary_def = kwargs['vocabulary_def']
        super(DefaultVocabularyListView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(DefaultVocabularyListView, self).get_context_data(**kwargs)
        context['vocabulary_verbose'] = self.vocabulary_verbose
        context['create_url'] = self.vocabulary + '_form'
        context['detail_url'] = self.vocabulary + '_detail'
        #context['vocabulary_def'] = self.vocabulary_def
        context['vocabulary'] = self.vocabulary
        return context


class DefaultVocabularyDetailView(DetailView):
    vocabulary = None
    vocabulary_verbose = None

    def __init__(self, **kwargs):
        self.vocabulary = kwargs['vocabulary']
        self.vocabulary_verbose = kwargs['vocabulary_verbose']
        super(DefaultVocabularyDetailView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(DefaultVocabularyDetailView, self).get_context_data(**kwargs)
        context['vocabulary_verbose'] = self.vocabulary_verbose
        context['vocabulary'] = self.vocabulary
        return context


# Request Basic Views
class DefaultRequestListView(ListView):
    request = None
    vocabulary = None
    request_verbose = None

    def __init__(self, **kwargs):
        self.request = kwargs['request']
        self.vocabulary = kwargs['vocabulary']
        self.request_verbose = kwargs['request_verbose']
        super(DefaultRequestListView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(DefaultRequestListView, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['request_verbose'] = self.request_verbose
        context['update_url'] = self.vocabulary + '_update'
        return context


class DefaultRequestCreateView(CreateView):
    request = None
    vocabulary = None
    request_verbose = None
    success_view = 'request_success'
    fields = ['term', 'name', 'definition', 'category', 'provenance', 'provenance_uri',
              'note', 'request_notes', 'submitter_name', 'submitter_email', 'request_reason']

    def __init__(self, **kwargs):
        self.request = kwargs['request']
        self.vocabulary = kwargs['vocabulary']
        self.request_verbose = kwargs['request_verbose']
        self.success_url = reverse_lazy(self.success_view, kwargs={'vocabulary': self.vocabulary})
        super(DefaultRequestCreateView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(DefaultRequestCreateView, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['request_verbose'] = self.request_verbose
        context['vocabulary'] = self.vocabulary
        context['success_view'] = 'request_success'
        return context


class ActionTypeRequestCreateView(DefaultRequestCreateView):
    fields = DefaultRequestCreateView.fields + ['produces_result']

class SpatialOffsetTypeCreateView(DefaultRequestCreateView):
    fields = DefaultRequestCreateView.fields + ['offset1', 'offset2', 'offset3']
