from __future__ import unicode_literals
import datetime
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
    note = models.TextField(blank=True, verbose_name='Reason for request')

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
        db_table = 'ActionTypeCV'
        verbose_name = 'Action Type'

class ActionTypeRequest(ControlVocabularyRequest, ControlVocabulary, AbstractActionType):
    class Meta:
        managed = False
        db_table = 'ActionTypeCVRequests'
        verbose_name = 'Action Type Request'

class MethodType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'MethodTypeCV'
        verbose_name = 'Method Type'


class MethodTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'MethodTypeCVRequests'
        verbose_name = 'Method Type Request'


class OrganizationType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'OrganizationTypeCV'
        verbose_name = 'Organization Type'


class OrganizationTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'OrganizationTypeCVRequests'
        verbose_name = 'Organization Type Request'


class SamplingFeatureGeotype(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureGeotypeCV'
        verbose_name = 'Sampling Feature Geo-type'


class SamplingFeatureGeotypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureGeotypeCVRequests'
        verbose_name = 'Sampling Feature Geo-type Request'


class SamplingFeatureType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureTypeCV'
        verbose_name = 'Sampling Feature Type'


class SamplingFeatureTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureTypeCVRequests'
        verbose_name = 'Sampling Feature Type Request'


class SiteType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SiteTypeCV'
        verbose_name = 'Site Type'


class SiteTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SiteTypeCVRequests'
        verbose_name = 'Site Type Request'


class AggregationStatistic(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'AggregationStatisticCV'
        verbose_name = 'Aggregation Statistic'


class AggregationStatisticRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'AggregationStatisticCVRequests'
        verbose_name = 'Aggregation Statistic Request'


class AnnotationType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'AnnotationTypeCV'
        verbose_name = 'Annotation Type'


class AnnotationTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'AnnotationTypeCVRequests'
        verbose_name = 'Annotation Type Request'


class CensorCode(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'CensorCodeCV'
        verbose_name = 'Censor Code'


class CensorCodeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'CensorCodeCVRequests'
        verbose_name = 'Censor Code Request'


class DatasetType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'DatasetTypeCV'
        verbose_name = 'Dataset Type'


class DatasetTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'DatasetTypeCVRequests'
        verbose_name = 'Dataset Type Request'


class DirectiveType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'DirectiveTypeCV'
        verbose_name = 'Directive Type'


class DirectiveTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'DirectiveTypeCVRequests'
        verbose_name = 'Directive Type Request'


class ElevationDatum(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'ElevationDatumCV'
        verbose_name = 'Elevation Datum'


class ElevationDatumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'ElevationDatumCVrequests'
        verbose_name = 'Elevation Datum Request'


class EquipmentType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'EquipmentTypeCV'
        verbose_name = 'Equipment Type'


class EquipmentTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'EquipmentTypeCVRequests'
        verbose_name = 'Equipment Type Request'


class PropertyDataType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'PropertyDataTypeCV'
        verbose_name = 'Property Data Type'


class PropertyDataTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'PropertyDataTypeCVRequests'
        verbose_name = 'Property Data Type Request'


class QualityCode(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'QualityCodeCV'
        verbose_name = 'Quality Code'


class QualityCodeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'QualityCodeCVRequests'
        verbose_name = 'Quality Code Request'


class ReferenceMaterialMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'ReferenceMaterialMediumCV'
        verbose_name = 'Reference Material Medium'


class ReferenceMaterialMediumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'ReferenceMaterialMediumCVRequests'
        verbose_name = 'Reference Material Medium Request'


class ResultType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'ResultTypeCV'
        verbose_name = 'Result Type'


class ResultTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'ResultTypeCVRequests'
        verbose_name = 'Result Type Request'


class SampledMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SampledMediumCV'
        verbose_name = 'Sampled Medium'


class SampledMediumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SampledMediumCVRequests'
        verbose_name = 'Sampled Medium Request'


class SpatialOffsetType(ControlVocabulary, AbstractSpatialOffsetType):
    class Meta:
        managed = False
        db_table = 'SpatialOffsetTypeCV'
        verbose_name = 'Spatial Offset Type'


class SpatialOffsetTypeRequest(ControlVocabularyRequest, ControlVocabulary, AbstractSpatialOffsetType):
    class Meta:
        managed = False
        db_table = 'SpatialOffsetTypeCVRequests'
        verbose_name = 'Spatial Offset Type Request'


class Speciation(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SpeciationCV'
        verbose_name = 'Speciation'


class SpeciationRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SpeciationCVrequests'
        verbose_name = 'Speciation Request'


class SpecimenMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SpecimenMediumCV'
        verbose_name = 'Specimen Medium'


class SpecimenMediumRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SpecimenMediumCVRequests'
        verbose_name = 'Specimen Medium Request'


class SpecimenType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SpecimenTypeCV'
        verbose_name = 'Specimen Type'


class SpecimenTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SpecimenTypeCVRequests'
        verbose_name = 'Specimen Type Request'


class Status(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'StatusCV'
        verbose_name = 'Status'


class StatusRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'StatusCVRequests'
        verbose_name = 'Status Request'


class TaxonomicClassifierType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'TaxonomicClassifierTypeCV'
        verbose_name = 'Taxonomic Classifier Type'


class TaxonomicClassifierTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'TaxonomicClassifierTypeCVRequests'
        verbose_name = 'Taxonomical Classifier Type Request'


class VariableName(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'VariableNameCV'
        verbose_name = 'Variable Name'


class VariableNameRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'VariableNameCVRequests'
        verbose_name = 'Variable Name Request'


class VariableType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'VariableTypeCV'
        verbose_name = 'Variable Type'


class VariableTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'VariableTypeCVRequests'
        verbose_name = 'Variable Type Request'


