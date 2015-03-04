from tastypie.api import Api
from tastypie.resources import ModelResource

from rdfserializer.api import RdfSerializer, ModelRdfResource
from models import ActionType, ActionTypeRequest, MethodType, MethodTypeRequest, \
    OrganizationType, OrganizationTypeRequest, SamplingFeatureGeotype, SamplingFeatureGeotypeRequest, \
    SamplingFeatureType, SamplingFeatureTypeRequest, SiteType, SiteTypeRequest, AggregationStatistic, \
    AggregationStatisticRequest, AnnotationType, AnnotationTypeRequest, CensorCode, \
    CensorCodeRequest, DatasetType, DatasetTypeRequest, DirectiveType, DirectiveTypeRequest, \
    ElevationDatum, ElevationDatumRequest, EquipmentType, EquipmentTypeRequest, PropertyDataType, PropertyDataTypeRequest, \
    QualityCode, QualityCodeRequest, ReferenceMaterialMedium, ReferenceMaterialMediumRequest, \
    ResultType, ResultTypeRequest, SampledMedium, SampledMediumRequest, SpatialOffsetType, \
    SpatialOffsetTypeRequest, Speciation, SpeciationRequest, Status, StatusRequest, \
    TaxonomicClassifierType, TaxonomicClassifierTypeRequest, VariableName, VariableNameRequest, \
    VariableType, VariableTypeRequest, SpecimenMedium, SpecimenMediumRequest, SpecimenType, \
    SpecimenTypeRequest


class ActionTypeResource(ModelRdfResource):
    scheme = 'actionTypeCV'

    class Meta:
        queryset = ActionType.objects.using('control_vocabularies').all()
        resource_name = 'actiontypecv'
        max_limit = 0
        serializer = RdfSerializer()


class ActionTypeRequestResource(ModelResource):
    class Meta:
        queryset = ActionTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'actiontypecvrequest'
        max_limit = 0


class MethodTypeResource(ModelRdfResource):
    scheme = 'methodTypeCV'

    class Meta:
        queryset = MethodType.objects.using('control_vocabularies').all()
        resource_name = 'methodtypecv'
        max_limit = 0
        serializer = RdfSerializer()

class MethodTypeRequestResource(ModelResource):
    class Meta:
        queryset = MethodTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'methodtypecvrequest'
        max_limit = 0

class OrganizationTypeResource(ModelRdfResource):
    scheme = 'organizationTypeCV'

    class Meta:
        queryset = OrganizationType.objects.using('control_vocabularies').all()
        resource_name = 'organizationtypecv'
        max_limit = 0
        serializer = RdfSerializer()


class OrganizationTypeRequestResource(ModelResource):
    class Meta:
        queryset = OrganizationTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'organizationtypecvrequest'
        max_limit = 0


class SamplingFeatureGeotypeResource(ModelRdfResource):
    scheme = 'samplingFeatureGeotypeCV'

    class Meta:
        queryset = SamplingFeatureGeotype.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturegeotypecv'
        max_limit = 0
        serializer = RdfSerializer()


class SamplingFeatureGeotypeRequestResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureGeotypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturegeotypecvrequest'
        max_limit = 0


class SamplingFeatureTypeResource(ModelRdfResource):
    scheme = 'samplingFeatureTypeCV'

    class Meta:
        queryset = SamplingFeatureType.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturetypecv'
        max_limit = 0
        serializer = RdfSerializer()


class SamplingFeatureTypeRequestResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturetypecvrequest'
        max_limit = 0


class SiteTypeResource(ModelRdfResource):
    scheme = 'siteTypeCV'

    class Meta:
        queryset = SiteType.objects.using('control_vocabularies').all()
        resource_name = 'sitetypecv'
        max_limit = 0
        serializer = RdfSerializer()


class SiteTypeRequestResource(ModelResource):
    class Meta:
        queryset = SiteTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'sitetypecvrequests'
        max_limit = 0

# Denver
class AggregationStatisticResource(ModelRdfResource):
    scheme = 'aggregationStatisticCV'

    class Meta:
        queryset = AggregationStatistic.objects.using('control_vocabularies').all()
        resource_name = 'aggregationstatisticcv'
        max_limit = 0
        serializer = RdfSerializer()


class AggregationStatisticRequestResource(ModelResource):
    class Meta:
        queryset = AggregationStatisticRequest.objects.using('control_vocabularies').all()
        resource_name = 'aggregationstatisticcvrequest'
        max_limit = 0


class AnnotationTypeResource(ModelRdfResource):
    scheme = 'annotationTypeCV'

    class Meta:
        queryset = AggregationStatistic.objects.using('control_vocabularies').all()
        resource_name = 'annotationtypecv'
        max_limit = 0
        serializer = RdfSerializer()


class AnnotationTypeRequestResource(ModelResource):
    class Meta:
        queryset = AnnotationTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'annotationtypecvrequest'
        max_limit = 0


class CensorCodeResource(ModelRdfResource):
    scheme = 'censorCodeCV'

    class Meta:
        queryset = CensorCode.objects.using('control_vocabularies').all()
        resource_name = 'censorcodecv'
        max_limit = 0
        serializer = RdfSerializer()


class CensorCodeRequestResource(ModelResource):
    class Meta:
        queryset = CensorCodeRequest.objects.using('control_vocabularies').all()
        resource_name = 'censorcodecvrequest'
        max_limit = 0


class DatasetTypeResource(ModelRdfResource):
    scheme = 'datasetTypeCV'

    class Meta:
        queryset = DatasetType.objects.using('control_vocabularies').all()
        resource_name = 'datasettypecv'
        max_limit = 0
        serializer = RdfSerializer()


class DatasetTypeRequestResource(ModelResource):
    class Meta:
        queryset = DatasetTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'datasettypecvrequest'
        max_limit = 0


class DirectiveTypeResource(ModelRdfResource):
    scheme = 'directiveTypeCV'

    class Meta:
        queryset = DirectiveType.objects.using('control_vocabularies').all()
        resource_name = 'directivetypecv'
        max_limit = 0
        serializer = RdfSerializer()


class DirectiveTypeRequestResource(ModelResource):
    class Meta:
        queryset = DirectiveTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'directivetypecvrequest'
        max_limit = 0


class ElevationDatumResource(ModelRdfResource):
    scheme = 'elevationDatumCV'

    class Meta:
        queryset = ElevationDatum.objects.using('control_vocabularies').all()
        resource_name = 'elevationdatumcv'
        max_limit = 0
        serializer = RdfSerializer()


class ElevationDatumRequestResource(ModelResource):
    class Meta:
        queryset = ElevationDatumRequest.objects.using('control_vocabularies').all()
        resource_name = 'elevationdatumcvrequest'
        max_limit = 0


class EquipmentTypeResource(ModelRdfResource):
    scheme = 'equipmentTypeCV'

    class Meta:
        queryset = EquipmentType.objects.using('control_vocabularies').all()
        resource_name = 'equipmenttypecv'
        max_limit = 0
        serializer = RdfSerializer()


class EquipmentTypeRequestResource(ModelResource):
    class Meta:
        queryset = EquipmentTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'equipmenttypecvrequest'
        max_limit = 0


class PropertyDataTypeResource(ModelRdfResource):
    scheme = 'propertyDataTypeCV'

    class Meta:
        queryset = PropertyDataType.objects.using('control_vocabularies').all()
        resource_name = 'propertydatatypecv'
        max_limit = 0
        serializer = RdfSerializer()


class PropertyDataTypeRequestResource(ModelResource):
    class Meta:
        queryset = PropertyDataTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'propertydatatypecvrequest'
        max_limit = 0


class QualityCodeResource(ModelRdfResource):
    scheme = 'qualityCodeCV'

    class Meta:
        queryset = QualityCode.objects.using('control_vocabularies').all()
        resource_name = 'qualitycodecv'
        max_limit = 0
        serializer = RdfSerializer()


class QualityCodeRequestResource(ModelResource):
    class Meta:
        queryset = QualityCodeRequest.objects.using('control_vocabularies').all()
        resource_name = 'qualitycodecvrequest'
        max_limit = 0


class ReferenceMaterialMediumResource(ModelRdfResource):
    scheme = 'referenceMaterialMediumCV'

    class Meta:
        queryset = ReferenceMaterialMedium.objects.using('control_vocabularies').all()
        resource_name = 'referencematerialmediumcv'
        max_limit = 0
        serializer = RdfSerializer()


class ReferenceMaterialMediumRequestResource(ModelResource):
    class Meta:
        queryset = ReferenceMaterialMediumRequest.objects.using('control_vocabularies').all()
        resource_name = 'referencematerialmediumcvrequest'
        max_limit = 0


class ResultTypeResource(ModelRdfResource):
    scheme = 'resultTypeCV'

    class Meta:
        queryset = ResultType.objects.using('control_vocabularies').all()
        resource_name = 'resulttypecv'
        max_limit = 0
        serializer = RdfSerializer()


class ResultTypeRequestResource(ModelResource):
    class Meta:
        queryset = ResultTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'resulttypecvrequest'
        max_limit = 0


class SampledMediumResource(ModelRdfResource):
    scheme = 'sampledMediumCV'

    class Meta:
        queryset = SampledMedium.objects.using('control_vocabularies').all()
        resource_name = 'sampledmediumcv'
        max_limit = 0
        serializer = RdfSerializer()


class SampledMediumRequestResource(ModelResource):
    class Meta:
        queryset = SampledMediumRequest.objects.using('control_vocabularies').all()
        resource_name = 'sampledmediumcvrequest'
        max_limit = 0


class SpatialOffsetTypeResource(ModelRdfResource):
    scheme = 'spatialOffsetTypeCV'

    class Meta:
        queryset = SpatialOffsetType.objects.using('control_vocabularies').all()
        resource_name = 'spatialoffsettypecv'
        max_limit = 0
        serializer = RdfSerializer()


class SpatialOffsetTypeRequestResource(ModelResource):
    class Meta:
        queryset = SpatialOffsetTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'spatialoffsettypecvrequest'
        max_limit = 0


class SpeciationResource(ModelRdfResource):
    scheme = 'speciationCV'

    class Meta:
        queryset = Speciation.objects.using('control_vocabularies').all()
        resource_name = 'speciationcv'
        max_limit = 0
        serializer = RdfSerializer()


class SpeciationRequestResource(ModelResource):
    class Meta:
        queryset = SpeciationRequest.objects.using('control_vocabularies').all()
        resource_name = 'speciationcvrequest'
        max_limit = 0


class SpecimenMediumResource(ModelRdfResource):
    scheme = 'specimenMediumCV'

    class Meta:
        queryset = SpecimenMedium.objects.using('control_vocabularies').all()
        resource_name = 'specimenmediumcv'
        max_limit = 0
        serializer = RdfSerializer()


class SpecimenMediumRequestResource(ModelResource):
    class Meta:
        queryset = SpecimenMediumRequest.objects.using('control_vocabularies').all()
        resource_name = 'specimenmediumcvrequest'
        max_limit = 0


class SpecimenTypeResource(ModelRdfResource):
    scheme = 'specimenTypeCV'

    class Meta:
        queryset = SpecimenType.objects.using('control_vocabularies').all()
        resource_name = 'specimentypecv'
        max_limit = 0
        serializer = RdfSerializer()


class SpecimenTypeRequestResource(ModelResource):
    class Meta:
        queryset = SpecimenTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'specimentypecvrequest'
        max_limit = 0


class StatusResource(ModelRdfResource):
    scheme = 'statusCV'

    class Meta:
        queryset = Status.objects.using('control_vocabularies').all()
        resource_name = 'statuscv'
        max_limit = 0
        serializer = RdfSerializer()


class StatusRequestResource(ModelResource):
    class Meta:
        queryset = StatusRequest.objects.using('control_vocabularies').all()
        resource_name = 'statuscvrequest'
        max_limit = 0


class TaxonomicClassifierTypeResource(ModelRdfResource):
    scheme = 'taxonomicClassifierTypeCV'

    class Meta:
        queryset = TaxonomicClassifierType.objects.using('control_vocabularies').all()
        resource_name = 'taxonomicclassifiertypecv'
        max_limit = 0
        serializer = RdfSerializer()


class TaxonomicClassifierTypeRequestResource(ModelResource):
    class Meta:
        queryset = TaxonomicClassifierTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'taxonomicclassifiertypecvrequest'
        max_limit = 0


class VariableNameResource(ModelRdfResource):
    scheme = 'variableNameCV'

    class Meta:
        queryset = VariableName.objects.using('control_vocabularies').all()
        resource_name = 'variablenamecv'
        max_limit = 0
        serializer = RdfSerializer()


class VariableNameRequestResource(ModelResource):
    class Meta:
        queryset = VariableNameRequest.objects.using('control_vocabularies').all()
        resource_name = 'variablenamecvrequest'
        max_limit = 0


class VariableTypeResource(ModelRdfResource):
    scheme = 'variableTypeCV'

    class Meta:
        queryset = VariableType.objects.using('control_vocabularies').all()
        resource_name = 'variabletypecv'
        max_limit = 0
        serializer = RdfSerializer()


class VariableTypeRequestResource(ModelResource):
    class Meta:
        queryset = VariableTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'variabletypecvrequest'
        max_limit = 0



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
# Denver
v1_api.register(AggregationStatisticResource())
v1_api.register(AggregationStatisticRequestResource())
v1_api.register(AnnotationTypeResource())
v1_api.register(AnnotationTypeRequestResource())
v1_api.register(CensorCodeResource())
v1_api.register(CensorCodeRequestResource())
v1_api.register(DatasetTypeResource())
v1_api.register(DatasetTypeRequestResource())
v1_api.register(DirectiveTypeResource())
v1_api.register(DirectiveTypeRequestResource())
v1_api.register(ElevationDatumResource())
v1_api.register(ElevationDatumRequestResource())
v1_api.register(EquipmentTypeResource())
v1_api.register(EquipmentTypeRequestResource())
v1_api.register(PropertyDataTypeResource())
v1_api.register(PropertyDataTypeRequestResource())
v1_api.register(QualityCodeResource())
v1_api.register(QualityCodeRequestResource())
v1_api.register(ReferenceMaterialMediumResource())
v1_api.register(ReferenceMaterialMediumRequestResource())
v1_api.register(ResultTypeResource())
v1_api.register(ResultTypeRequestResource())
v1_api.register(SampledMediumResource())
v1_api.register(SampledMediumRequestResource())
v1_api.register(SpatialOffsetTypeResource())
v1_api.register(SpatialOffsetTypeRequestResource())
v1_api.register(SpeciationResource())
v1_api.register(SpeciationRequestResource())
v1_api.register(SpecimenMediumResource())
v1_api.register(SpecimenMediumRequestResource())
v1_api.register(SpecimenTypeResource())
v1_api.register(SpecimenTypeRequestResource())
v1_api.register(StatusResource())
v1_api.register(StatusRequestResource())
v1_api.register(TaxonomicClassifierTypeResource())
v1_api.register(TaxonomicClassifierTypeRequestResource())
v1_api.register(VariableNameResource())
v1_api.register(VariableNameRequestResource())
v1_api.register(VariableTypeResource())
v1_api.register(VariableTypeRequestResource())

