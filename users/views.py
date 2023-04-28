import json
import uuid
from django.contrib.auth import authenticate,get_user_model
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from .models import AppUser,ReportedCrimes

User=get_user_model()
def Homepage(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = AppUser.objects.get(email=email)
            if user.check_password(password):
                login(user)
                # serializer = UserSerializer(user)
                refresh=RefreshToken.for_user(user)
                # access_token=str(refresh.access_token)
                payload={
                    'email':user.email,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'phone_number':user.phone_number,
                    'gender':user.gender,
                    'emergency_contact':user.emergency_contact,
                }
                access_token = refresh.access_token
                access_token.payload.update(payload)
                # return Response({'Success':True,'Message':"Login Successfull",'first_name':user.first_name,'last_name':user.last_name,'email':user.email})
                return Response({
                    'Success': True,
                    'Message': 'Login successful',
                    'access_token': str(access_token),
                })
            else:
                return Response({'Success':False,'Message': 'Email and Password do not match'})
        except User.DoesNotExist:
            return Response({'Success':False,'Message':"The email is not registered"})

class SignUpView(APIView):
    def post(self,request):
        platform='website'
        first_name=request.data.get('first_name')
        last_name=request.data.get('last_name')
        email=request.data.get('email')
        phone_number=request.data.get('phone_number')
        emergency_contact=request.data.get('emergency_contact')
        password=request.data.get('password')
        gender=request.data.get('gender')
        if request.data.get('platform'):
            platform=request.data.get('platform')
        username=first_name+' '+last_name
        try:
            user=User.objects.get(email=email)
            return Response({'Success':False,'Message':"The email is already taken"})
        except User.DoesNotExist:
            user=AppUser.objects.create_user(username=username,email=email, password=password,
                                          first_name=first_name,last_name=last_name,phone_number=phone_number,
                                          emergency_contact=emergency_contact,platform=platform,gender=gender,is_active=True)
            return Response({'Success': True,'Message': "Account Created Successfully"})


@method_decorator(csrf_exempt, name='dispatch')
class Report(APIView):
    def post(self, request):
        print(request.POST.get('latitude'))
        print(request.FILES)
        email = request.POST.get('email')
        crimetype = request.POST.get('crimetype')
        latitude=float(request.POST.get('latitude'))
        longitude=float(request.POST.get('longitude'))
        description = request.POST.get('description')
        picture = request.FILES.get('picture')
        print(picture)
        print(email)
        audio_data = request.FILES.get('audio')
        user=User.objects.get(email=email)
        # Save the picture and audio files if they were included in the request
        # if picture!='No Image':
        #     picture_filename = f'{uuid.uuid4()}.jpg'
        #     picture_file = SimpleUploadedFile(picture_filename, picture, content_type='image/jpeg')
        # else:
        #     picture_file = None
        # if audio_data != 'No Audio':
        #     audio_filename = f'{uuid.uuid4()}.mp3'
        #     audio_file = SimpleUploadedFile(audio_filename, audio_data, content_type='audio/mpeg')
        # else:
            # audio_file = None
        
        # Create a new Report object and save it to the database
        report = ReportedCrimes(
            email=email,
            username=user.username,
            gender=user.gender,
            latitude=latitude,
            longitude=longitude, 
            crimetype=crimetype,
            description=description,
            image=picture,
            audio=audio_data,
           
        )
        report.save()
        
        return Response({'Success':True,'Message': 'Report submitted successfully.'})
