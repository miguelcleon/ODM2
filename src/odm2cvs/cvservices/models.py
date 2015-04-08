from __future__ import unicode_literals
import datetime
from django.utils import timezone
from uuid import uuid4

from django.db import models


class ControlVocabulary(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.TextField()
    category = models.CharField(max_length=255, blank=True)
    provenance = models.TextField(blank=True)
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        abstract = True
        ordering = ["-name"]


class ControlVocabularyRequest(models.Model):
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    ACCEPTED = 'Accepted'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (ACCEPTED, 'Accepted'),
    )

    term = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    definition = models.TextField()
    category = models.CharField(max_length=255, blank=True)
    provenance = models.TextField(blank=True)
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)
    request_id = models.CharField(max_length=255, db_column='requestId', primary_key=True, default=uuid4)
    status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    date_submitted = models.DateField(db_column='dateSubmitted', default=timezone.now)
    date_status_changed = models.DateField(db_column='dateStatusChanged', default=timezone.now)
    request_notes = models.TextField(db_column='requestNotes')
    submitter_name = models.CharField(max_length=255, db_column='submitterName')
    submitter_email = models.CharField(max_length=255, db_column='submitterEmail', blank=True)
    request_reason = models.CharField(max_length=255, db_column='requestReason')
    original_request = models.ForeignKey('self', db_column='originalRequestId', null=True)

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


class AbstractSpatialOffsetType(models.Model):
    offset1 = models.TextField(db_column='offset1', blank=True)
    offset2 = models.TextField(db_column='offset2', blank=True)
    offset3 = models.TextField(db_column='offset3', blank=True)

    class Meta:
        abstract = True


class ActionType(ControlVocabulary, AbstractActionType):
    class Meta:
        managed = False
        db_table = 'actiontypecv'
        verbose_name = 'Action Type'
        ordering = ["name"]

class ActionTypeRequest(ControlVocabularyRequest, AbstractActionType):
    class Meta:
        managed = False
        db_table = 'actiontypecvrequests'
        verbose_name = 'Action Type Request'
        ordering = ["name"]


class MethodType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'methodtypecv'
        verbose_name = 'Method Type'
        ordering = ["name"]


class MethodTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'methodtypecvrequests'
        verbose_name = 'Method Type Request'
        ordering = ["name"]


class OrganizationType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'organizationtypecv'
        verbose_name = 'Organization Type'
        ordering = ["name"]


class OrganizationTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'organizationtypecvrequests'
        verbose_name = 'Organization Type Request'
        ordering = ["name"]


class SamplingFeatureGeotype(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'samplingfeaturegeotypecv'
        verbose_name = 'Sampling Feature Geo-type'
        ordering = ["name"]


class SamplingFeatureGeotypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'samplingfeaturegeotypecvrequests'
        verbose_name = 'Sampling Feature Geo-type Request'


class SamplingFeatureType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'samplingfeaturetypecv'
        verbose_name = 'Sampling Feature Type'


class SamplingFeatureTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'samplingfeaturetypecvrequests'
        verbose_name = 'Sampling Feature Type Request'


class SiteType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sitetypecv'
        verbose_name = 'Site Type'


class SiteTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'sitetypecvrequests'
        verbose_name = 'Site Type Request'


class AggregationStatistic(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'aggregationstatisticcv'
        verbose_name = 'Aggregation Statistic'


class AggregationStatisticRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'aggregationstatisticcvrequests'
        verbose_name = 'Aggregation Statistic Request'


class AnnotationType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'annotationtypecv'
        verbose_name = 'Annotation Type'

class AnnotationTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'annotationtypecvrequests'
        verbose_name = 'Annotation Type Request'


class CensorCode(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'censorcodecv'
        verbose_name = 'Censor Code'


class CensorCodeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'censorcodecvrequests'
        verbose_name = 'Censor Code Request'


class DatasetType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'datasettypecv'
        verbose_name = 'Dataset Type'


class DatasetTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'datasettypecvrequests'
        verbose_name = 'Dataset Type Request'

class DirectiveType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'directivetypecv'
        verbose_name = 'Directive Type'


class DirectiveTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'directivetypecvrequests'
        verbose_name = 'Directive Type Request'


class ElevationDatum(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'elevationdatumcv'
        verbose_name = 'Elevation Datum'


class ElevationDatumRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'elevationdatumcvrequests'
        verbose_name = 'Elevation Datum Request'


class EquipmentType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'equipmenttypecv'
        verbose_name = 'Equipment Type'


class EquipmentTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'equipmenttypecvrequests'
        verbose_name = 'Equipment Type Request'


class PropertyDataType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'propertydatatypecv'
        verbose_name = 'Property Data Type'


class PropertyDataTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'propertydatatypecvrequests'
        verbose_name = 'Property Data Type Request'


class QualityCode(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'qualitycodecv'
        verbose_name = 'Quality Code'


class QualityCodeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'qualitycodecvrequests'
        verbose_name = 'Quality Code Request'


class ReferenceMaterialMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'referencematerialmediumcv'
        verbose_name = 'Reference Material Medium'


class ReferenceMaterialMediumRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'referencematerialmediumcvrequests'
        verbose_name = 'Reference Material Medium Request'


class ResultType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'resulttypecv'
        verbose_name = 'Result Type'


class ResultTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'resulttypecvrequests'
        verbose_name = 'Result Type Request'


class SampledMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sampledmediumcv'
        verbose_name = 'Sampled Medium'


class SampledMediumRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'sampledmediumcvrequests'
        verbose_name = 'Sampled Medium Request'


class SpatialOffsetType(ControlVocabulary, AbstractSpatialOffsetType):
    class Meta:
        managed = False
        db_table = 'spatialoffsettypecv'
        verbose_name = 'Spatial Offset Type'


class SpatialOffsetTypeRequest(ControlVocabularyRequest, AbstractSpatialOffsetType):
    class Meta:
        managed = False
        db_table = 'spatialoffsettypecvrequests'
        verbose_name = 'Spatial Offset Type Request'


class Speciation(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'speciationcv'
        verbose_name = 'Speciation'


class SpeciationRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'speciationcvrequests'
        verbose_name = 'Speciation Request'


class SpecimenMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'specimenmediumcv'
        verbose_name = 'Specimen Medium'


class SpecimenMediumRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'specimenmediumcvrequests'
        verbose_name = 'Specimen Medium Request'


class SpecimenType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'specimentypecv'
        verbose_name = 'Specimen Type'


class SpecimenTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'specimentypecvrequests'
        verbose_name = 'Specimen Type Request'


class Status(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'statuscv'
        verbose_name = 'Status'


class StatusRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'statuscvrequests'
        verbose_name = 'Status Request'


class TaxonomicClassifierType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'taxonomicclassifiertypecv'
        verbose_name = 'Taxonomic Classifier Type'


class TaxonomicClassifierTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'taxonomicclassifiertypecvrequests'
        verbose_name = 'Taxonomic Classifier Type Request'


class VariableName(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'variablenamecv'
        verbose_name = 'Variable Name'


class VariableNameRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'variablenamecvrequests'
        verbose_name = 'Variable Name Request'


class VariableType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'variabletypecv'
        verbose_name = 'Variable Type'


class VariableTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'variabletypecvrequests'
        verbose_name = 'Variable Type Request'


