from pymongo import MongoClient
from django.conf import settings


url = 'mongodb+srv://kmnaveen777:naveen@atlas.eokhe.mongodb.net/'
client = MongoClient(url)

db = client["test_mongo"]  
teacher_collection = db["auth_teachers"] 

def create_teacher(strategy, details, backend, user=None, *args, **kwargs):
    """
    Custom pipeline function to store teachers in MongoDB when logging in via Google or github.
    """
    print("teacherlogin")
    request = strategy.request
    user_type = request.session.get("user_type")  # Check if user logged in as teacher

    if user and user_type == "teacher":
        teacher = teacher_collection.find_one({"email": user.email})

        if not teacher:
            teacher_data = {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": "teacher",
                "is_active": True,
                "is_staff": False,
                "is_superuser": False,
            }
            teacher_collection.insert_one(teacher_data)
def custom_function(backend, user, response, *args, **kwargs):

    print("Custom pipeline function executed")
    return

def assign_user_type(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        user_type = strategy.session_get("user_type")  # Get stored session user_type
        if user_type:
            social = user.social_auth.get(provider=backend.name)
            social.extra_data["user_type"] = user_type 
            social.save()



