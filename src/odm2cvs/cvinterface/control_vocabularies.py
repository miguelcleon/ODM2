from cvservices.models import *
from cvinterface.views.base_views import *

vocabulary_list_view = DefaultVocabularyListView
vocabulary_detail_view = DefaultVocabularyDetailView
vocabulary_list_template = 'cvinterface/vocabularies/default_list.html'
vocabulary_detail_template = 'cvinterface/vocabularies/default_detail.html'

request_list_view = DefaultRequestListView
request_create_view = DefaultRequestCreateView
request_update_view = None
request_list_template = 'cvinterface/requests/default_list.html'
request_create_template = 'cvinterface/requests/default_form.html'
request_update_template = 'cvinterface/requests/default_update.html'


vocabularies = {
    # optional keys:
    # list_view, detail_view, list_template, detail_template

    'actiontype': {
        'name': ActionType._meta.verbose_name,
        'model': ActionType,
        'detail_template': 'cvinterface/vocabularies/actiontype_detail.html',
    },
    'methodtype': {
        'name': MethodType._meta.verbose_name,
        'model': MethodType,
    }
    # TODO: add the other vocabularies.
    # if the vocabulary has extra fields, take as an example action type:
    #   just add a new detail template with the same name convention (vocabulary_detail.html)
    # if the vocabulary does not have any extra fields, take as an example method type:
    #   just specify the model class and the name: Model._meta.verbose_name (doesn't really have to be that one, I'm using it because it's already there.)
}

requests = {
    # optional keys:
    # list_view, create_view, update_view, list_template, create_template, update_template

    'actiontyperequest': {
        'vocabulary': 'actiontype',
        'name': ActionTypeRequest._meta.verbose_name,
        'model': ActionTypeRequest,
        'create_view': ActionTypeRequestCreateView,
    },
    'methodtyperequest': {
        'vocabulary': 'methodtype',
        'name': MethodTypeRequest._meta.verbose_name,
        'model': MethodTypeRequest,
    }
    # TODO: add the other requests.
    # same as with the vocabularies.
    # here, for a request with extra fields, you have to write a new CreateView class in base_views.py. take actiontyperequest as an example for that.
    # if the request doesn't have extra fields, take methodtyperequest as an example.
}