from django.urls import path

from new_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("loginpage", views.loginpage, name="loginpage"),



    path("base", views.base, name="base"),
    path("adm_registration", views.adm_registration, name="adm_registration"),
    path("add_mark", views.add_mark, name="add_mark"),
    path("view_mark", views.view_mark, name="view_mark"),
    path("edit_mark/<int:id>/", views.edit_mark, name="edit_mark"),
    path("adminstudents_data", views.adminstudents_data, name="adminstudents_data"),


    path("studentbase", views.studentbase, name="studentbase"),
    path("student_registration", views.student_registration, name="student_registration"),
    path("students_data", views.students_data, name="students_data"),
    path("delete_student/<int:id>/", views.delete_student, name="delete_student"),
    path("update_student/<int:id>/", views.update_student, name="update_student"),

    # path("students", views.students, name="students"),

]