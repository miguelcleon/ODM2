from django.contrib import messages
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse


from cvinterface.views.base_views import *
from cvinterface.control_vocabularies import requests, request_list_view, request_list_template, \
    request_create_view, request_create_template, request_update_view, request_update_template

request_list_views = {}
for request_name in requests:
    request = requests[request_name]
    view = request['list_view'] if 'list_view' in request else request_list_view
    template = request['list_template'] if 'list_template' in request else request_list_template

    request_list_views[request_name] = view.as_view(request=request_name, model=request['model'],
        vocabulary=request['vocabulary'], request_verbose=request['name'], template_name=template,
    )

request_create_views = {}
for request_name in requests:
    request = requests[request_name]
    view = request['create_view'] if 'create_view' in request else request_create_view
    template = request['create_template'] if 'create_template' in request else request_create_template

    request_create_views[request_name] = view.as_view(request=request_name, model=request['model'],
        vocabulary=request['vocabulary'], request_verbose=request['name'], template_name=template,
        vocabulary_model=request['vocabulary_model']
    )

request_update_views = {}
for request_name in requests:
    request = requests[request_name]
    view = request['update_view'] if 'update_view' in request else request_update_view
    template = request['update_template'] if 'update_template' in request else request_update_template

    request_update_views[request_name] = view.as_view(request=request_name, model=request['model'],
        vocabulary=request['vocabulary'], request_verbose=request['name'], template_name=template,
        vocabulary_model=request['vocabulary_model']
    )


class RequestsView(ListView):
    queryset = []
    template_name = 'cvinterface/requests/main_requests_list.html'

    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        context['requests'] = [{'name': requests[request_name]['name'], 'url': reverse(request_name)}
                               for request_name in requests]
        context['pending_requests'] = [(pending_object, pending_object._meta.verbose_name)
                                       for request_name in requests
                                       for pending_object in requests[request_name]['model'].objects.filter(status='Pending')
                                       if requests[request_name]['model'].objects.filter(status='Pending').count() > 0]

        return context


class SuccessRedirectView(RedirectView):
    message = None

    def get_redirect_url(self, redirect_model):
        messages.add_message(self.request, messages.SUCCESS, self.message)
        return reverse(redirect_model)