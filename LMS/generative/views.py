import json
import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from datetime import datetime


api_key = "AIzaSyAPu6-WHl506r8YuIZjE6uHLFQIm1gORC4"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")
chat_history = []

url = 'mongodb+srv://kmnaveen777:naveen@atlas.eokhe.mongodb.net/'

client = MongoClient(url)

db = client["test_mongo"]  
collection = db["questions"]
skills_collection = db["skills"]

@api_view(["GET"])
def get_skills(request):
    try:
        skills = list(skills_collection.find({}, {"_id": 0, "name": 1}))
        skill_names = [skill["name"] for skill in skills]
        # print(skill_names)
        return Response(skill_names, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


import re
from datetime import datetime

@login_required
def store_question(request):
    if request.method == "POST":
        try:
         
            raw_data = request.body.decode("utf-8")

 
            cleaned_data = re.sub(r"\\n", "", raw_data)

            # print("hii",    request.session.teacher_id)
            question_data = json.loads(cleaned_data)

       
            collection.insert_one({
               
                "questions": question_data,
                "timestamp": datetime.utcnow().isoformat() 
            })

            return JsonResponse({"message": "Question set stored successfully!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405) 








@api_view(["POST"])
def assign(request):
    try:
        assessment_id = request.data.get("assessment_id")
        if not assessment_id:
            return Response({"error": "Missing assessment ID"}, status=status.HTTP_400_BAD_REQUEST)

        assessment_oid = ObjectId(assessment_id)
        result = collection.update_one(
            {"_id": assessment_oid},
            {"$set": {"is_assigned": True}}
        )
        print(result.modified_count)

        if result.modified_count > 0:
            return Response({"message": "Assessment marked as assigned"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Assessment not found or already assigned"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    





@api_view(["POST"])
def store_questions(request):
    try:
        question_data = request.data.get("questions")
        teacher_id = request.data.get("teacher_id")
        time_allotment = request.data.get("time_allotment")
        assessment_name = request.data.get("assessment_name")
        ai= request.data.get("ai")
        question_type= request.data.get("question_type")
        print(ai)
        print(type(ai))
        
        if not all([question_data, teacher_id, time_allotment, assessment_name]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Store in MongoDB collection
        collection.insert_one({
            "teacher_id": teacher_id,
            "questions": question_data,
            "time_allotment": time_allotment,
            "assessment_name": assessment_name,
            "ai": ai,
            # "timestamp": datetime.utcnow().isoformat(),
            "date": datetime.now(),  
            "timestamp": datetime.now(),
            "question_type": question_type,
            "is_assigned": False,
        })

        return Response({"message": "Assessment stored successfully"}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@login_required(login_url="/loginteacher/")
def chat_page(request):
    """Render chat page."""
    return render(request, "chat.html")

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def chat_view(request):
    print("chat_view")
    if request.method == "POST":
        prompt = request.POST.get("message")
        if prompt:
            chat_history.append({"role": "user", "parts": [prompt]})
            try:
                response = model.generate_content(chat_history)
                chat_text = response.text
                chat_history.append({"role": "model", "parts": [chat_text]})
                return JsonResponse({"response": chat_text})
            except Exception as e:
                return JsonResponse({"response": f"An error occurred: {e}"})

    return JsonResponse({"error": "Invalid request"}, status=400)



@api_view(['POST'])
def generate_questions(request):
    print("generate_questions view")
    prompt = request.data.get("prompt")
    
    if not prompt:
        return Response({"error": "Prompt is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        chat_history.append({"role": "user", "parts": [prompt]})
        response = model.generate_content(chat_history)
        chat_text = response.text
        chat_history.append({"role": "model", "parts": [chat_text]})
        
        # Parse the JSON response if needed
        try:
            questions = json.loads(chat_text)
            return Response(questions)
        except json.JSONDecodeError:
            return Response({"response": chat_text})
            
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def download_chat_history(request):
    """Download chat history as JSON file."""
    
    if not chat_history:
        return JsonResponse({"error": "No chat history found"}, status=400)

    response = HttpResponse(
        json.dumps(chat_history, indent=4), content_type="application/json"
    )
    response["Content-Disposition"] = "attachment; filename=chat_history.json"
    return response
