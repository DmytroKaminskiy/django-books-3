from faker import Faker
import random

from user.models import User
from book.models import Book

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'generate random data'  # noqa

    def handle(self, *args, **options):
        fake = Faker()
        User.objects.all().delete()

        for _ in range(1_000):
            try:
                email = fake.email()
                User.objects.create(
                    email=email,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=random.randint(1, 100),
                )
            except IntegrityError:
                pass

        for i in range(1_000):
            author = User.objects.order_by('?').last()
            Book.objects.create(
                title=f'Title {i}',
                # author=author,
                author_id=author.id,
            )