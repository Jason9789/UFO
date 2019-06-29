from django.urls import path, include
import tutorboard.views

urlpatterns = [
    path('tutees', tutorboard.views.tutees, name='tutees'),
    path('tutors', tutorboard.views.tutors, name='tutors'),
    path('tutorapply/<int:tutorapply_id>', tutorboard.views.tuteeComment, name='tutorapply'),
    path('tutorrequest/<int:tutorrequest_id>', tutorboard.views.tutorComment, name='tutorrequest'),
    path('tutorapply/<int:tutorapply_id>/edittutorapply', tutorboard.views.tutorapplyedit, name='tutorapplyedit'),
    path('tutorapply/<int:tutorapply_id>/tutorapplyremove', tutorboard.views.tutorapplyremove, name='tutorapplyremove'),
    path('tutorapply/newtutorapply', tutorboard.views.newtutorapply, name='newtutorapply'),
    path('tutorrequest/<int:tutorrequest_id>/edittutorrequest', tutorboard.views.tutorrequestedit, name='tutorrequestedit'),
    path('tutorrequest/newtutorrequest', tutorboard.views.newtutorrequest, name='newtutorrequest'),
    path('tutorrequest/<int:tutorrequest_id>/tutorrequestremove', tutorboard.views.tutorrequestremove, name='tutorrequestremove'),
]
