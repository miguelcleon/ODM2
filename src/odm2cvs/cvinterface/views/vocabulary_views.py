from django.core.urlresolvers import reverse

from cvinterface.views.base_views import *
from cvinterface.control_vocabularies import vocabularies, vocabulary_list_view, vocabulary_list_template, \
    vocabulary_detail_view, vocabulary_detail_template

from collections import OrderedDict
import operator

list_views = {}
for cv_name in vocabularies:
    vocabulary = vocabularies[cv_name]
    view = vocabulary['list_view'] if 'list_view' in vocabulary else vocabulary_list_view
    template = vocabulary['list_template'] if 'list_template' in vocabulary else vocabulary_list_template
    list_views[cv_name] = view.as_view(vocabulary=cv_name, vocabulary_def=vocabulary['definition'], vocabulary_verbose=vocabulary['name'],
        model=vocabulary['model'], template_name=template,
    )


detail_views = {}
for cv_name in vocabularies:
    vocabulary = vocabularies[cv_name]
    view = vocabulary['detail_view'] if 'detail_view' in vocabulary else vocabulary_detail_view
    template = vocabulary['detail_template'] if 'detail_template' in vocabulary else vocabulary_detail_template

    detail_views[cv_name] = view.as_view(vocabulary=cv_name, vocabulary_verbose=vocabulary['name'],
        model=vocabulary['model'], template_name=template,
    )


class VocabulariesView(ListView):
    queryset = []
    template_name = 'cvinterface/index.html'


    def get_context_data(self, **kwargs):
        sorted_vocabularies = sorted(vocabularies.items(), key=operator.itemgetter(0))
        context = super(VocabulariesView, self).get_context_data(**kwargs)
        print OrderedDict(sorted(vocabularies.items()))
        context['vocabulary_views'] = [{'definition': vocabularies[vocabulary_name]['definition'],'name': vocabularies[vocabulary_name]['name'], 'url': reverse(vocabulary_name)}
                                       for vocabulary_name in OrderedDict(sorted(vocabularies.items()))]

        return context
