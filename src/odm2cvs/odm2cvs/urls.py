from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

from cvinterface.views import HomeView, action_type_view, method_type_view, organization_type_view, \
    sampling_feature_geotype_view, sampling_feature_type_view, site_type_view

from cvservices.api import ActionTypeResource, ActionTypeRequestResource, MethodTypeResource, \
    MethodTypeRequestResource, OrganizationTypeResource, OrganizationTypeRequestResource, \
    SamplingFeatureGeotypeResource, SamplingFeatureGeotypeRequestResource, SamplingFeatureTypeResource, \
    SamplingFeatureTypeRequestResource, SiteTypeResource, SiteTypeRequestResource

v1_api = Api(api_name='v1')
v1_api.register(ActionTypeResource())
v1_api.register(ActionTypeRequestResource())
v1_api.register(MethodTypeResource())
v1_api.register(MethodTypeRequestResource())
v1_api.register(OrganizationTypeResource())
v1_api.register(OrganizationTypeRequestResource())
v1_api.register(SamplingFeatureGeotypeResource())
v1_api.register(SamplingFeatureGeotypeRequestResource())
v1_api.register(SamplingFeatureTypeResource())
v1_api.register(SamplingFeatureTypeRequestResource())
v1_api.register(SiteTypeResource())
v1_api.register(SiteTypeRequestResource())


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^actiontype/', action_type_view, name='actiontypecv'),
    url(r'^methodtype/', method_type_view, name='methodtypecv'),
    url(r'^organizationtype/', organization_type_view, name='organizationtypecv'),
    url(r'^samplingfeaturegeotype/', sampling_feature_geotype_view, name='samplingfeaturegeotypecv'),
    url(r'^samplingfeaturetype/', sampling_feature_type_view, name='samplingfeaturetypecv'),
    url(r'^sitetype/', site_type_view, name='sitetypecv'),
)
