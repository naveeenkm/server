from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from pymongo import MongoClient

# MongoDB Connection
url = "mongodb+srv://kmnaveen777:naveen@atlas.eokhe.mongodb.net/"
client = MongoClient(url)
db = client["test_mongo"]
users_collection = db["auth_user"]  # Student collection
teacher_collection = db["auth_teachers"]  # Teacher collection

class StudentAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        user_data = users_collection.find_one({"username": username})
        if user_data and check_password(password, user_data["password"]):
            user, created = User.objects.get_or_create(username=username)
            user.role = "student"  # Assign role
            user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class TeacherAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        teacher_data = teacher_collection.find_one({"username": username})
        if teacher_data and check_password(password, teacher_data["password"]):
            user, created = User.objects.get_or_create(username=username)
            user.role = "teacher"  # Assign role
            user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
