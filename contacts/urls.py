from django.urls import path

from contacts.views import create_contact, ContactAPIView, ContactListAPIView, ContactRetrieveAPIView

urlpatterns = [
    path('create', create_contact, name ='create_contact'),
    path('contacts-api', ContactAPIView.as_view(), name='create_contact_api'),
    path('contacts', ContactListAPIView.as_view(), name='contact_list'),
    path('contacts/<int:id>/', ContactRetrieveAPIView.as_view(), name='contact_detail'),
]
