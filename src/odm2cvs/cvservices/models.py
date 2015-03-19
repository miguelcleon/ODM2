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

class ActionTypeRequest(ControlVocabularyRequest, ControlVocabulary, AbstractActionType):
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


class MethodTypeRequest(ControlVocabularyRequest, ControlVocabulary):
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


class OrganizationTypeRequest(ControlVocabularyRequest, ControlVocabulary):
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


class SamplingFeatureGeotypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'samplingfeaturegeotypecvrequests'
        verbose_name = 'Sampling Feature Geo-type Request'
        ordering = ["name"]


class SamplingFeatureType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'samplingfeaturetypecv'
        verbose_name = 'Sampling Feature Type'
        ordering = ["name"]


class SamplingFeatureTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'samplingfeaturetypecvrequests'
        verbose_name = 'Sampling Feature Type Request'
        ordering = ["name"]


class SiteType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sitetypecv'
        verbose_name = 'Site Type'
        ordering = ["name"]


class SiteTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sitetypecvrequests'
        verbose_name = 'Site Type Request'
        ordering = ["name"]


class AggregationStatistic(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'aggregationstatisticcv'
        verbose_name = 'Aggregation Statistic'
        ordering = ["name"]


class AggregationStatisticRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'aggregationstatisticcvrequests'
        verbose_name = 'Aggregation Statistic Request'
        ordering = ["name"]


class AnnotationType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'annotationtypecv'
        verbose_name = 'Annotation Type'
        ordering = ["name"]


class AnnotationTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'annotationtypecvrequests'
        verbose_name = 'Annotation Type Request'
        ordering = ["name"]


class CensorCode(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'censorcodecv'
        verbose_name = 'Censor Code'
        ordering = ["name"]


class CensorCodeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'censorcodecvrequests'
        verbose_name = 'Censor Code Request'
        ordering = ["name"]


class DatasetType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'datasettypecv'
        verbose_name = 'Dataset Type'
        ordering = ["name"]


class DatasetTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'datasettypecvrequests'
        verbose_name = 'Dataset Type Request'
        ordering = ["name"]


class DirectiveType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'directivetypecv'
        verbose_name = 'Directive Type'
        ordering = ["name"]


class DirectiveTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'directivetypecvrequests'
        verbose_name = 'Directive Type Request'
        ordering = ["name"]


class ElevationDatum(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'elevationdatumcv'
        verbose_name = 'Elevation Datum'
        ordering = ["name"]


class ElevationDatumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'elevationdatumcvrequests'
        verbose_name = 'Elevation Datum Request'
        ordering = ["name"]


class EquipmentType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'equipmenttypecv'
        verbose_name = 'Equipment Type'
        ordering = ["name"]


class EquipmentTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'equipmenttypecvrequests'
        verbose_name = 'Equipment Type Request'
        ordering = ["name"]


class PropertyDataType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'propertydatatypecv'
        verbose_name = 'Property Data Type'
        ordering = ["name"]


class PropertyDataTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'propertydatatypecvrequests'
        verbose_name = 'Property Data Type Request'
        ordering = ["name"]


class QualityCode(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'qualitycodecv'
        verbose_name = 'Quality Code'
        ordering = ["name"]


class QualityCodeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'qualitycodecvrequests'
        verbose_name = 'Quality Code Request'
        ordering = ["name"]


class ReferenceMaterialMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'referencematerialmediumcv'
        verbose_name = 'Reference Material Medium'
        ordering = ["name"]


class ReferenceMaterialMediumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'referencematerialmediumcvrequests'
        verbose_name = 'Reference Material Medium Request'
        ordering = ["name"]


class ResultType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'resulttypecv'
        verbose_name = 'Result Type'
        ordering = ["name"]


class ResultTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'resulttypecvrequests'
        verbose_name = 'Result Type Request'
        ordering = ["name"]


class SampledMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sampledmediumcv'
        verbose_name = 'Sampled Medium'
        ordering = ["name"]


class SampledMediumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sampledmediumcvrequests'
        verbose_name = 'Sampled Medium Request'
        ordering = ["name"]


class SpatialOffsetType(ControlVocabulary, AbstractSpatialOffsetType):
    class Meta:
        managed = False
        db_table = 'spatialoffsettypecv'
        verbose_name = 'Spatial Offset Type'
        ordering = ["name"]


class SpatialOffsetTypeRequest(ControlVocabularyRequest, ControlVocabulary, AbstractSpatialOffsetType):
    class Meta:
        managed = False
        db_table = 'spatialoffsettypecvrequests'
        verbose_name = 'Spatial Offset Type Request'
        ordering = ["name"]


class Speciation(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'speciationcv'
        verbose_name = 'Speciation'
        ordering = ["name"]


class SpeciationRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'speciationcvrequests'
        verbose_name = 'Speciation Request'
        ordering = ["name"]


class SpecimenMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'specimenmediumcv'
        verbose_name = 'Specimen Medium'
        ordering = ["name"]


class SpecimenMediumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'specimenmediumcvrequests'
        verbose_name = 'Specimen Medium Request'
        ordering = ["name"]


class SpecimenType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'specimentypecv'
        verbose_name = 'Specimen Type'
        ordering = ["name"]


class SpecimenTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'specimentypecvrequests'
        verbose_name = 'Specimen Type Request'
        ordering = ["name"]


class Status(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'statuscv'
        verbose_name = 'Status'
        ordering = ["name"]


class StatusRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'statuscvrequests'
        verbose_name = 'Status Request'
        ordering = ["name"]


class TaxonomicClassifierType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'taxonomicclassifiertypecv'
        verbose_name = 'Taxonomic Classifier Type'
        ordering = ["name"]


class TaxonomicClassifierTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'taxonomicclassifiertypecvrequests'
        verbose_name = 'Taxonomic Classifier Type Request'
        ordering = ["name"]


class VariableName(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'variablenamecv'
        verbose_name = 'Variable Name'
        ordering = ["name"]


class VariableNameRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'variablenamecvrequests'
        verbose_name = 'Variable Name Request'
        ordering = ["name"]


class VariableType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'variabletypecv'
        verbose_name = 'Variable Type'
        ordering = ["name"]


class VariableTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'variabletypecvrequests'
        verbose_name = 'Variable Type Request'
        ordering = ["name"]


