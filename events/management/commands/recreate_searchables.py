import datetime
import urllib

from django.core.management.base import BaseCommand, CommandError

from events.models.events import Event, update_event_searchable


class Command(BaseCommand):
    help = "Regenerated Searchable records from this node"

    def handle(self, *args, **options):
        for event in Event.objects.all():
            update_event_searchable(event)
