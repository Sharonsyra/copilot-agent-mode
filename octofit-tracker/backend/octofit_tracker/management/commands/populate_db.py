from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        alice = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        bob = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        carol = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams (store member emails)
        team_alpha = Team.objects.create(name='Team Alpha', members=[alice.email, bob.email])
        team_beta = Team.objects.create(name='Team Beta', members=[carol.email])

        # Activities
        activity1 = Activity.objects.create(user=alice, type='run', duration=30, date=timezone.now())
        activity2 = Activity.objects.create(user=bob, type='walk', duration=45, date=timezone.now())
        activity3 = Activity.objects.create(user=carol, type='cycle', duration=60, date=timezone.now())

        # Workouts
        Workout.objects.create(user=alice, activity=activity1, date=timezone.now())
        Workout.objects.create(user=bob, activity=activity2, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(team=team_alpha, points=150)
        Leaderboard.objects.create(team=team_beta, points=80)

        self.stdout.write(self.style.SUCCESS('Test data inserted into octofit_db.'))
