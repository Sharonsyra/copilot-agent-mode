# Tests for OctoFit collections
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test2@example.com', name='Test2', password='testpass')
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2025-06-24T00:00:00Z')
        self.assertEqual(activity.type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email='test3@example.com', name='Test3', password='testpass')
        activity = Activity.objects.create(user=user, type='walk', duration=20, date='2025-06-24T00:00:00Z')
        workout = Workout.objects.create(user=user, activity=activity, date='2025-06-24T00:00:00Z')
        self.assertEqual(workout.activity.type, 'walk')
