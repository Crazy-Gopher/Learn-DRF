import json

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsInternal
from .serializers import UserSerializer
from .models import Question
from .signals import user_signup_success


def healthcheckview(request):
    return HttpResponse("Everything ok")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


# from django.template import loader
# 
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@csrf_exempt
def get_user(request):
    if request.method == 'GET':
        username = request.GET.get('username',None)
        user_id = request.GET.get('user_id',None)
        email = request.GET.get('email',None)
         
        if not username and not user_id and not email:
            return HttpResponse(json.dumps({"error":"missing_parameters"}),content_type='application/json; charset=utf-8',status=400)
         
        users = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=email) | Q(pk=user_id))
        if not users.exists():
            return HttpResponse(json.dumps({"error":"user_does_not_exist"}),content_type='application/json; charset=utf-8',status=400)
        if len(users)>1:
            return HttpResponse(json.dumps({"error":"multiple users exists"}),content_type='application/json; charset=utf-8',status=400)
        else:
            user= users[0]
            
        minimal_serializer = UserSerializer(user)
    
        return HttpResponse(json.dumps(minimal_serializer.data),content_type='application/json; charset=utf-8')
    else:
        return HttpResponse(json.dumps({"error":"invalid_method"}),content_type='application/json; charset=utf-8',status=400)

from django.views import View
class GetUserView(View):
    @csrf_exempt
    def get(self, request):
        username = request.GET.get('username',None)
        user_id = request.GET.get('user_id',None)
        email = request.GET.get('email',None)

        if not username and not user_id and not email:
            return HttpResponse(json.dumps({"error":"missing_parameters"}),content_type='application/json; charset=utf-8',status=400)

        users = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=email) | Q(pk=user_id))
        if not users.exists():
            return HttpResponse(json.dumps({"error":"user_does_not_exist"}),content_type='application/json; charset=utf-8',status=400)
        if len(users)>1:
            return HttpResponse(json.dumps({"error":"multiple users exists"}),content_type='application/json; charset=utf-8',status=400)
        else:
            user= users[0]
            
        minimal_serializer = UserSerializer(user)

        return HttpResponse(json.dumps(minimal_serializer.data),content_type='application/json; charset=utf-8')

@csrf_exempt
def user_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request, user_id):
    """
    Retrieve, update, partial update or delete a code user.
    """
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


class UserView(APIView):
    permission_classes = (IsInternal,)

    def post(self, request):
        username = request.data.get('username', '').strip().lower()
        email = request.data.get('email', '').strip().lower()
        password = request.data.get('password', '')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        if not password:
            password = User.objects.make_random_password(128)
        
        try:
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=email))
        except User.DoesNotExist:
            try:
                user = User.objects.create_user(username, email, password)
            except IntegrityError:
                # Most likely due to repeat requests, we can ignore this
                return Response({"error":"duplicate_user"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"user_already_exist"}, status=status.HTTP_400_BAD_REQUEST)
        #user.first_name = first_name
        #user.last_name = last_name
        #user.save()
        token, created = Token.objects.get_or_create(user=user)
        minimal_serializer = UserSerializer(user)
        
        user_signup_success.send(sender=self.__class__, user=user)
               
        return Response({"success":True,"user":minimal_serializer.data})

    def put(self, request,user_id):
        # Username and password are required. Other fields are optional.
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error":"user_id_does_not_exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self,request,user_id):
        user = User.objects.get(pk=user_id)
#         try:
#             user = User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return Response({"error":"user_does_not_exist"}, status=status.HTTP_400_BAD_REQUEST)

        minimal_serializer = UserSerializer(user)
               
        return Response({"success":True,"user":minimal_serializer.data})


    def delete(self, request, user_id): 
        try:
            user = User.objects.get(pk=user_id).delete()
        except User.DoesNotExist:
            return Response({"error":"user_does_not_exist"}, status=status.HTTP_400_BAD_REQUEST)
         
        return Response({"success":True})

    def patch(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error":"user_id_does_not_exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


class UsersListView(ListView):
    template_name = 'polls/users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'polls/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')


from django.core.cache import cache
def cache_view(request,user_id):
    cache_key = 'api_user_%d_json' % user_id # needs to be unique
    cache_time = 86400 # time in seconds for cache to be valid
    data = cache.get(cache_key) # returns None if no key-value pair
    print("getting caches") 
    if not data:
        print("setting caches")
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return JsonResponse({"error":"user_does_not_exist"}, status=status.HTTP_400_BAD_REQUEST)

        minimal_serializer = UserSerializer(user)
        data = minimal_serializer.data
        cache.set(cache_key, data, cache_time)
    return JsonResponse(data)