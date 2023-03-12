# -*- coding: utf-8 -*-
"""A UserManager that doesn't require username."""

from typing import Any

from django.contrib.auth.models import BaseUserManager

User = Any  # Can't import ..models.User or see how to get type from self.model.


class UserManager(BaseUserManager):
    """A UserManager that doesn't require username."""

    def _create_user(
        self,
        email: str,
        password: str,
        **extra_fields: dict[str, Any],
    ) -> User:
        """Create and save a user with the given email, and password.

        As parent but without username.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            extra_fields: Other keyword arguments.

        Raises:
            ValueError: If no email is given.

        Returns:
            User: The newly created user.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        email: str,
        password: str,
        **extra_fields: dict[str, Any],
    ) -> User:
        """Create and save a user with the given email, and password.

        Default to False for is_staff and is_superuser.
        As parent but without username.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            extra_fields: Other keyword arguments.

        Returns:
            User: The newly created user.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(
        self,
        email: str,
        password: str,
        **extra_fields: dict[str, Any],
    ) -> User:
        """Create and save a user with the given email, and password.

        Default to True for is_staff and is_superuser.
        As parent but without username.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            extra_fields: Other keyword arguments.

        Raises:
            ValueError: If no email is given.

        Returns:
            User: The newly created user.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)
