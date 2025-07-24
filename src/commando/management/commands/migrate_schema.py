from typing import Any
from django.db import connection
from django.core.management import BaseCommand, call_command

from django.contrib.auth import get_user_model

from django.core.management.base import BaseCommand

from helpers.db import statements as db_statements


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        shema_name = 'public'
        with connection.cursor() as cursor:
            cursor.execute(db_statements.CREATE_SCHEMA_SQL.format
                (schema_name='public')
            )
            cursor.execute(db_statements.ACTIVATE_SCHEMA_SQL.format
                (schema_name='public')
            )
            call_command("migrate", interactive=False)
        
        schemas = ['example']
        for shema_name in schemas: 
            with connection.cursor() as cursor:
                cursor.execute(db_statements.CREATE_SCHEMA_SQL.format
                            (schema_name=shema_name)
                        )
                cursor.execute(db_statements.ACTIVATE_SCHEMA_SQL.format
                            (schema_name=shema_name)
                        )
            # python manage.py migrate --noinput
            call_command("migrate", interactive=False)
        # User = get_user_model()
        # user_a = User.objects.create_superuser(
        #     username='example',
        #     password='example1233'
        # )            
    