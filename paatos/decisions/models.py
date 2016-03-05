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
    area = models.ForeignKey('Area', null=True,
                             verbose_name=_('Geographic area this case is related to'))
    originator = models.ForeignKey('Person', null=True)
    creation_date = models.DateField(blank=True, null=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    pass


class Organization(models.Model):
    abstract = models.CharField(max_length=255, verbose_name=_('A one-line description of an organization'))


class Action(models.Model):
    iri = models.CharField(max_length=255,
                           verbose_name=_('IRI for this action'))
    title = models.CharField(max_length=255,
                             verbose_name=_('Descriptive compact title for this case'))
    case = models.ForeignKey(Case, verbose_name=_('Case this action affects'))
    ordering = models.IntegerField(verbose_name=_('Ordering of this action within a meeting'))
    article_number = models.CharField(max_length=255,
                                      verbose_name=_('The article number given to this action after decision'))
    proposal_identifier = models.CharField(max_length=255,
                                           verbose_name=_(
                                               'Identifier for this action used inside the meeting minutes. The format will vary between cities.'))
    responsible_party = models.ForeignKey(Organization, verbose_name=_(
        'The city organization responsible for this decision. If decision is delegated, this is the organization that delegated the authority.'))
    delegation = models.ForeignKey(Post, null=True, verbose_name=_(
        'If this decision was delegated, this field will be filled and refers to the post that made the decision'))
    event = models.ForeignKey('Event', verbose_name=_('Event (if any) where this action took place'), null=True)
    # Contents for this action refer to this
    # Votes for this action refer here


class Content(models.Model):
    iri = models.CharField(max_length=255, verbose_name=_('IRI for this content'))
    ordering = models.IntegerField(verbose_name=_('Ordering of this content within the larger context (like action)'))
    title = models.CharField(max_length=255, verbose_name=_('Title of this content'))
    type = models.CharField(max_length=255, verbose_name=_(
        'Type of this content (options include: decision, proposal, proceedings...)'))
    hypertext = models.CharField(max_length=255, verbose_name=_(
        'Content formatted with pseudo-HTML. Only a very restricted set of tags is allowed. These are: first and second level headings (P+H1+H2) and table (more may be added, but start from a minimal set)'))
    action = models.ForeignKey('Action', verbose_name=_('Action that this content describes'))


class Attachment(models.Model):
    iri = models.CharField(max_length=255, verbose_name=_('IRI for this attachment'))
    file = models.CharField(max_length=255, verbose_name=_('FIXME: i should refer to a file'))
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')


# Popoloish models begin here

# "An event is an occurrence that people may attend."
class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("The event's name"))
    organization = models.ForeignKey(Organization, verbose_name=_('The organization organizing the event'))
    attendees = models.ManyToManyField('Person', verbose_name=_('People attending this event'), through='Attendance')


class Attendance(models.Model):
    event = models.ForeignKey('Event')
    attendee = models.ForeignKey('Person')
    role = models.CharField(max_length=50, verbose_name=_('Role of the person in the event (chairman, secretary...'))


class VoteEvent(models.Model):
    legislative_session = models.ForeignKey('Event', verbose_name=_('The meeting (event) where this vote took place'))
    vote_count = models.ForeignKey('VoteCount')


class VoteCount(models.Model):
    pass


class Membership(models.Model):
    person = models.ForeignKey('Person', verbose_name=_('Person who has membership in organization'))
    post = models.ForeignKey('Post', verbose_name=_('The post held by the member through this membership'))
    organization = models.ForeignKey('Organization',
                                     verbose_name=_('The organization in which the person or organization is a member'))


class Person(models.Model):
    pass


class Area(models.Model):
    pass
