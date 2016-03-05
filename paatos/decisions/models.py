from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _


class Case(models.Model):
    iri = models.CharField(max_length=255,
                           verbose_name=_('IRI for this case'))
    title = models.CharField(max_length=255,
                             verbose_name=_('A high level matter to be decided'))
    description = models.CharField(max_length=255, blank=True,
                                   verbose_name=_('A descriptive compact title for the case'))
    summary = models.CharField(max_length=255, blank=True,
                               verbose_name=_('Summary of this case. Typically a few sentences.'))
    attachments = models.ManyToManyField('Attachment')
    category = models.CharField(max_length=255, blank=True,
                                verbose_name=_('Category this case belongs to ("tehtäväluokka")'))
    # Areas Foreignkey to this model
    originator = models.ForeignKey('Person')
    creation_date = models.DateField(blank=True)
    public = models.BooleanField(default=True)


class Post(models.Model):
    pass


class Organization(models.Model):
    pass


class Action(models.Model):
    iri = models.CharField(max_length=255,
                           verbose_name=_('IRI for this action'))
    title = models.CharField(max_length=255,
                             verbose_name=_('Title for this action'))
    case = models.ForeignKey(Case, verbose_name=_('Case this action affects'))
    ordering = models.IntegerField(verbose_name=_('Ordering of this action within a meeting'))
    article_number = models.CharField(max_length=255,
                                      verbose_name=_('The article number given to this action after decision'))
    proposal_identifier = models.CharField(max_length=255,
                                           verbose_name=_('Identifier for this action used inside the meeting minutes. The format will vary between cities.'))
    responsible_party = models.ForeignKey(Organization, verbose_name=_('The city organization responsible for this decision. If decision is delegated, this is the organization that delegated the authority.'))
    delegation = models.ForeignKey(Post, verbose_name=_('If this decision was delegated, this field will be filled and refers to the post that made the decision'))
    # Contents for this action refer to this
    # Votes for this action refer here


class Content(models.Model):
    iri = models.CharField(max_length=255, verbose_name=_('IRI for this content'))
    ordering = models.IntegerField(verbose_name=_('Ordering of this content within the larger context (like action)'))
    title = models.CharField(max_length=255, verbose_name=_('Title of this content'))
    type = models.CharField(max_length=255, verbose_name=_('Type of this content (options include: decision, proposal, proceedings...)'))
    hypertext = models.CharField(max_length=255, verbose_name=_('Content formatted with pseudo-HTML. Only a very restricted set of tags is allowed. These are: first and second level headings (P+H1+H2) and table (more may be added, but start from a minimal set)'))


class Attachment(models.Model):
    iri = models.CharField(max_length=255, verbose_name=_('IRI for this attachment'))
    file = models.CharField(max_length=255, verbose_name=_('FIXME: i should refer to a file'))
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')

# Popoloish models begin here
class Event(models.Model):

    pass


class VoteEvent(models.Model):
    pass


class VoteCount(models.Model):
    pass


class Membership(models.Model):
    pass


class Person(models.Model):
    pass


class Area(models.Model):
    pass
