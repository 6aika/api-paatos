from django.core.management.base import BaseCommand, CommandError
from decisions.models import Case
import random

class Command(BaseCommand):
    help = 'Create dummy case'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--title',
            dest='title',
            help="Case's title")

    def handle(self, *args, **options):
        title = options['title']
        c = Case(
            title=title,
            iri=str(random.randint(0, 99999999)),
        )
        c.save()
        self.stdout.write(self.style.SUCCESS(
            'Successfully created case "%s"' % c.pk)
        )
