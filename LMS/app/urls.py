from django.urls import include, path
from . import views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('teachersignup/',views.teacher_signup,name='teachersignup'),
    path('loginauth/',views.login_view,name='login'),
    path('teacherlogin/',views.teacher_login,name='teacherlogin'),
    path('loginteacher/',views.teacher,name='loginteacher'),
    path('',views.dashbord,name='dashbord'),
    # path('dashbord1/',views.dashbord1,name='dashbord1'),
   
    path('logout/', views.logout_view, name='logout'),
    
    path('login/', views.index, name='index'),
    path('teacher/', views.teacherpage, name='teacherpage'),
    
    path('check-auth/', views.check_auth, name='check_auth'),
    
     path('teacher/google/login/', views.teacher_google_login, name='teacher_google_login'),
     path('teacher/github/login/', views.teacher_github_login, name='teacher_github_login'),
     path('assessment/', views.assessment, name='assessment'),
     path('courses/',views.courses,name='courses'),
     path('courses/add_course/', views.add_course, name='add_course'),
     path('api/login_auth/', views.login_react, name='login_react'),
     path('api/login_admin/', views.login_react_admin),
     path('api/login_auth_teacher/', views.login_react_teacher, name='login_react_teacher'),
    path('api/signup_auth/', views.signup_react, name='signup_react'),
    path('api/signup_admin/', views.signup_react_admin),
    path('api/signup_auth_teacher/', views.signup_react_teacher, name='signup_react_teacher'),
    path('api/getting_assesment_id/', views.getting_assesment_id, name='getting_assesment_id'),
    path('api/assessment_details/<str:assessment_id>/', views.assessment_details, name='assessment_details'),
    path('api/test/',views.test, name='test'),
    path('api/tests/get', views.get_test),
    path('api/tests/submit', views.submit_test),
    path('api/tests/completed', views.completed_tests),
    path('api/tests/results', views.test_results),
    path('api/delete-assessment', views.delete_assessment),
    path('api/create_course', views.create_course),
    path('api/get_student_courses/<str:course_id>/', views.get_course ),
    path('api/get_teacher_courses/<str:teacher_id>/', views.get_teacher_courses ),
    path('api/get_teacher_blogs/<str:author_id>/', views.get_teacher_blogs ),
    path('api/get_courses/', views.get_courses ),
    path('api/get_blogs/', views.get_blogs ),
    path('api/add_student/', views.add_student ),
    path('api/students', views.get_all_students, name='get_all_students'),
    path('api/updated_student/<str:student_id>', views.update_student, name='update_student'),
    path('api/deleted_student/<str:student_id>', views.archive_student, name='archive_student'),
    path('api/teachers', views.get_all_teachers),
    path('api/add_teacher/', views.add_teacher),
    path('api/updated_teacher/<str:teacher_id>', views.update_teacher),
    path('api/deleted_teacher/<str:teacher_id>', views.archive_teacher),
    path('api/hr/', views.get_all_hrs, name='get_all_hr'),                    
    path('api/add_hr/', views.add_hr, name='add_hr'),                        
    path('api/update_hr/<str:id>/', views.update_hr, name='update_hr'),      
    path('api/delete_hr/<str:id>/', views.archive_hr, name='archive_hr'),
    path('api/updatecourses/<str:course_id>/', views.update_course),
    path('api/updatetests/<str:test_id>/', views.edit_test, name='edit_test'),
    path('api/tests/<str:id>/', views.get_test_by_id1),
    path('api/updatetest/<str:id>/', views.update_test_by_id), 
    path('api/create_blog/', views.create_blog), 
    path('api/viewblogs/<str:blog_id>/', views.get_blog_by_id, name='get_blog_by_id'),  # GET one blog by ID
    path('api/updateblogs/<str:blog_id>/', views.update_blog, name='update_blog'),
    

]