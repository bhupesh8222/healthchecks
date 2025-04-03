from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from hc.api.models import Project
from hc.accounts.models import Member  # Updated import path


@receiver(post_save, sender=User)
def add_user_to_all_projects(sender, instance, created, **kwargs):
    """Add newly created user to all existing projects with read access."""
    if created:  # Only run this when a new user is created
        projects = Project.objects.all()
        for project in projects:
            # Check if the user is already a member of the project
            if not Member.objects.filter(user=instance, project=project).exists():
                Member.objects.create(
                    user=instance,
                    project=project,
                    role="r"  # 'r' represents read-only access
                )
