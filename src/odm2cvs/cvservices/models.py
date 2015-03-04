from __future__ import unicode_literals
from django.utils import timezone
from uuid import uuid4

from django.db import models


class ControlVocabulary(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.TextField()
    category = models.CharField(max_length=255)
    provenance = models.TextField(blank=True)
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        abstract = True


class ControlVocabularyRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    )
    request_id = models.CharField(max_length=255, db_column='requestId', primary_key=True, default=uuid4)
    status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    date_submitted = models.DateField(db_column='dateSubmitted', default=timezone.now())
    date_status_changed = models.DateField(db_column='dateStatusChanged', default=timezone.now())
    request_notes = models.TextField(db_column='requestNotes')
    submitter_name = models.CharField(max_length=255, db_column='submitterName')
    submitter_email = models.CharField(max_length=255, db_column='submitterEmail', blank=True)
    request_reason = models.CharField(max_length=255, db_column='requestReason')

    class Meta:
        abstract = True


class AbstractActionType(models.Model):
    PRODUCES_RESULT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    produces_result = models.CharField(db_column='producesResult', max_length=5, choices=PRODUCES_RESULT_CHOICES)

    class Meta:
        abstract = True


class ActionType(ControlVocabulary, AbstractActionType):
    class Meta:
        managed = False
        db_table = 'ActionTypeCV'
        verbose_name = 'Action Type Control Vocabulary'


class ActionTypeRequest(ControlVocabularyRequest, ControlVocabulary, AbstractActionType):
    class Meta:
        managed = False
        db_table = 'ActionTypeCVRequests'
        verbose_name = 'Action Type CV Request'


class MethodType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'MethodTypeCV'
        verbose_name = 'Method Type Control Vocabulary'


class MethodTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'MethodTypeCVRequests'
        verbose_name = 'Method Type CV Request'


class OrganizationType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'OrganizationTypeCV'
        verbose_name = 'Organization Type Control Vocabulary'


class OrganizationTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'OrganizationTypeCVRequests'
        verbose_name = 'Organization Type CV Request'


class SamplingFeatureGeotype(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureGeotypeCV'
        verbose_name = 'Sampling Feature Geo-type CV'


class SamplingFeatureGeotypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureGeotypeCVRequests'
        verbose_name = 'Sampling Feature Geo-type CV Request'


class SamplingFeatureType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureTypeCV'
        verbose_name = 'Sampling Feature Type CV'


class SamplingFeatureTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureTypeCVRequests'
        verbose_name = 'Sampling Feature Type CV Request'


class SiteType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sitetypecv'
        verbose_name = 'Site Type Control Vocabulary'


class SiteTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sitetypecvrequests'
        verbose_name = 'Site Type CV Request'

# Denver
class AggregationStatistic(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'aggregationstatisticcv'
	verbose_name = 'Aggregation Statistic CV'

class AggregationStatisticRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'aggregationstatisticcvrequests'
	verbose_name = 'Aggregation Statistic CV Request'


class AnnotationType(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'annotationtypecv'
	verbose_name = 'Annotation Type CV'

class AnnotationTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'annotationtypecvrequests'
	verbose_name = 'Annotation Type CV Request'


class CensorCode(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'censorcodecv'
	verbose_name = 'Censor Code CV'

class CensorCodeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'censorcodecvrequests'
	verbose_name = 'Censor Code CV Request'

class DatasetType(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'datasettypecv'
	verbose_name = 'Dataset Type CV'

class DatasetTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'datasettypecvrequests'
	verbose_name = 'Dataset Type CV Request'

class DirectiveType(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'directivetypecv'
	verbose_name = 'Directive Type CV'

class DirectiveTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'directivetypecvrequests'
	verbose_name = 'Directive Type CV Request'


class ElevationDatum(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'elevationdatumcv'
	verbose_name = 'Elevation Datum CV'

class ElevationDatumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'elevationdatumcvrequests'
	verbose_name = 'Elevation Datum CV Request'


class EquipmentType(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'equipmenttypecv'
	verbose_name = 'Equipment Type CV'

class EquipmentTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'equipmenttypecvrequests'
	verbose_name = 'Equipment Type CV Request'


class PropertyDataType(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'propertydatatypecv'
	verbose_name = 'Property Data Type CV'

class PropertyDataTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'propertydatatypecvrequests'
	verbose_name = 'Property Data Type CV Request'

class QualityCode(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'qualitycodecv'
	verbose_name = 'Quality Code CV'

class QualityCodeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'qualitycodecvrequests'
	verbose_name = 'Quality Code CV Request'


class ReferenceMaterialMedium(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'referencematerialmediumcv'
	verbose_name = 'Reference Material Medium CV'

class ReferenceMaterialMediumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'referencematerialmediumcvrequests'
	verbose_name = 'Reference Material Medium CV Request'

class ResultType(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'resulttypecv'
	verbose_name = 'Result Type CV'

class ResultTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'resulttypecvrequests'
	verbose_name = 'Result Type CV Request'

class SampledMedium(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'sampledmediumcv'
	verbose_name = 'Sampled Medium CV'

class SampledMediumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'sampledmediumcvrequests'
	verbose_name = 'Sampled Medium CV Request'

class SpatialOffsetType(ControlVocabulary):    
    offset1 = models.TextField(blank=True)
    offset2 = models.TextField(blank=True)
    offset3 = models.TextField(blank=True)

    class Meta:
	managed = False
	db_table = 'spatialoffsettypecv'
	verbose_name = 'Spatial Offset Type CV'

class SpatialOffsetTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'spatialoffsettypecvrequests'
	verbose_name = 'Spatial Offset Type CV Request'


class Speciation(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'speciationcv'
	verbose_name = 'Speciation CV'

class SpeciationRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'peciationcvrequests'
	verbose_name = 'Speciation CV Request'


class SpecimenMedium(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'specimenmediumcv'
	verbose_name = 'Specimen Medium CV'

class SpecimenMediumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'specimenmediumcvrequests'
	verbose_name = 'Specimen Medium CV Request'


class SpecimenType(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'specimentypecv'
	verbose_name = 'Specimen Type CV'

class SpecimenTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'specimentypecvrequests'
	verbose_name = 'Specimen Type CV Request'

class Status(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'statuscv'
	verbose_name = 'Status CV'

class StatusRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'statuscvrequests'
	verbose_name = 'Status CV Request'

class TaxonomicClassifierType(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'taxonomicclassifiertypecv'
	verbose_name = 'Taxonomic Classifier Type CV'

class TaxonomicClassifierTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'taxonomicclassifiertypecvrequests'
	verbose_name = 'Taxonomical Classifier Type CV Request'

class VariableName(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'variablenamecv'
	verbose_name = 'Variable Name CV'

class VariableNameRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'variablenamecvrequests'
	verbose_name = 'Variable Name CV Request'


class VariableType(ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'variabletypecv'
	verbose_name = 'Variable Type CV'

class VariableTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
	managed = False
	db_table = 'variabletypecvrequests'
	verbose_name = 'Variable Type CV Request'


