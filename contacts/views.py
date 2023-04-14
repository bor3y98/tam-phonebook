from django.shortcuts import render, redirect
from .forms import ContactForm
from contacts.models import Contact

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user # Assuming there is a user associated with the contact
            contact.save()
            contact_number_formset = ContactForm.ContactNumberFormset(request.POST, instance=contact)
            if contact_number_formset.is_valid():
                contact_number_formset.save()
                return redirect('contacts:list')
    else:
        form = ContactForm()
        contact_number_formset = ContactForm.ContactNumberFormset(instance=Contact())
    return render(request, 'create_contact.html', {'form': form, 'contact_number_formset': contact_number_formset})


class ContactAPIView(APIView):

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactListAPIView(ListAPIView):
    """
      A view that lists all the contacts available in the database.

      Inherits from `ListAPIView`, which is a class-based view provided by Django REST Framework.
      """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRetrieveAPIView(RetrieveAPIView):
    """
       A view that retrieves the details of a specific contact with its related contact numbers.

       Inherits from `RetrieveAPIView`, which is a class-based view provided by Django REST Framework.

       Args:
           id (int): The ID of the contact to retrieve.

       Attributes:
           queryset (QuerySet): The queryset of Contact objects to retrieve from the database.
           serializer_class (Serializer): The serializer to use to serialize the retrieved Contact object.
           lookup_field (str): The field to use for looking up the Contact object, in this case the 'id' field.
       """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        """
             Retrieves the details of a specific contact with its related contact numbers.

             Returns:
                 Response: A Response object with the serialized data of the retrieved Contact object and its related ContactNumber objects.
             """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)