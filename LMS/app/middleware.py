from pymongo import MongoClient
from django.conf import settings

MONGO_URI = "mongodb+srv://kmnaveen777:naveen@atlas.eokhe.mongodb.net/"

client = MongoClient(MONGO_URI)
db = client["test_mongo"]
teacher_collection = db["auth_teachers"]

class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.is_teacher = False
        teacher_username = request.session.get("teacher_username")  # Get username from session
        
        print("🔹 Teacher Username from Session:", teacher_username)  # Debugging
        
        if teacher_username:
            teacher_data = teacher_collection.find_one({"username": teacher_username})
            if teacher_data:
                request.is_teacher = True
        
        print("🔹 request.is_teacher:", request.is_teacher)  # Debugging
        
        response = self.get_response(request)
        return response
