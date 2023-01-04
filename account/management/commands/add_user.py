from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
    help = "Create super user via cmd"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str, help="Add email for superuser")
        parser.add_argument("username", type=str, help="Add username for superuser")

    def handle(self, *args, **options):
        email = options.get("email")
        username = options.get("username")
        if User.objects.filter(email=email, username=username).exists():
            self.stdout.write(
                self.style.WARNING("Initial superuser already exists, doing nothing")
            )
            return

        psw = User.objects.make_random_password(
            length=10,
            allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789",
        )
        print(email, username, psw)
        # User.objects.create_superuser(email=email, username=username, password=psw)
        # try:
        #     link = f'{settings.ALLOWED_HOSTS[0]}{reverse("admin:index")}'
        # except IndexError:
        #     link = "unknown url"
        # except exceptions.NoReverseMatch:
        #     link = settings.ALLOWED_HOSTS[0]
        send_mail(
            f"Credentials for {settings.PROJECT_NAME} ",
            f"Credentials for project: {settings.PROJECT_NAME}\n\nsername: {username}\nPassword: {psw}",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        self.stdout.write(self.style.SUCCESS("Successfully created superuser"))
