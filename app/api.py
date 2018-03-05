import json, random, itertools
from rest_framework import viewsets, mixins
from django.conf.urls import include
from rest_framework.response import Response
from rest_framework import status

from .models import Participant
from django.contrib.auth.models import User

class ParticipantEntry(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    
    queryset = Participant.objects.none()
    
    
    def list (self, request):
        """
        Return Participant partner
        @parameters (string participant)
        @return (string partner) 
        """        
        
        try: 
            user_obj=User.objects.get(username=request.GET['user']) 
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        
        try:
            participant_name = request.GET['name']
            participant = Participant.objects.get(name=participant_name)
        except:
            Response("Participant doesn't exist.",status=status.HTTP_404_NOT_FOUND) 
        
        # Assign partner to the participant introduced by user is calling the API
        if not participant.partner:
            listOfParticipant = list(Participant.objects.filter(user=user_obj).values_list('name', flat=True).order_by('name'))
            
            for i in range(len(listOfParticipant)):
                p = Participant.objects.get(name=listOfParticipant[i], user=user_obj)
                buy_to=listOfParticipant[(i+1)%(len(listOfParticipant))]
                p.partner=buy_to
                p.save()
        
        return Response({"Buy to":participant.partner})  


    def create(self, request):
        """
        Add a participant
        @parameters (json file)
        """
        data = json.loads(request.body.decode('utf-8'))
        
        try: 
            user_obj,create=User.objects.get_or_create(username=data['user']) 
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        
        try: 
            Participant.objects.create(name=data['name'], email=data['email'], user=user_obj)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
                