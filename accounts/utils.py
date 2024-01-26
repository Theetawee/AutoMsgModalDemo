from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, username, name, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        if not name:
            raise ValueError("A valid name must be provided")
        # email = self.normalize_email(email)
        # email = email.lower()
        user = self.model(username=username, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, name, password, **extra_fields)


def clean_email(email):
    email = BaseUserManager.normalize_email(email)
    email = email.lower()
    return email
