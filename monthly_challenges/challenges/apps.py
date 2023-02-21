"""Challenges app entrypoint."""
from django.apps import AppConfig


class ChallengesConfig(AppConfig):
    """Default config for challenges app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "challenges"
