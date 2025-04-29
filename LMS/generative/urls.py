from django.urls import path
from .views import assign, chat_page, chat_view, download_chat_history, generate_questions, store_question, get_skills, store_questions
urlpatterns = [
    path("", chat_page, name="chat_page"),
    path("chat/", chat_view, name="chat_view"),  
    path("chat/download/", download_chat_history, name="download_chat"),
    path("gen/chat/download/", download_chat_history, name="download_chat"),
    path("store_question/", store_question, name="store_question"),
    path('api/skills/', get_skills, name='get_skills'),
    path('api/generate-questions/', generate_questions, name='generate_questions'),
    path('api/store_questions/', store_questions, name='store_questions'),
    path('api/assign/', assign, name='assign'),
    
]
