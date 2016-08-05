
from django.shortcuts import render, get_object_or_404,redirect
from .models import Cupcake
from .forms import CupcakeForm,CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import CupcakeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def cupcake_list(request):
    cakes = Cupcake.objects.all().order_by('-createdAt')
    context = {"cakes": cakes}
    return render(request,"menu/list.html",context)

def cupcake_detail(request,pk):
    cake = get_object_or_404(Cupcake,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = cake
            comment.writer = request.user
            comment.approved_comment = True
            comment.save()
            return redirect('menu.views.cupcake_detail', pk=cake.pk)
    else:
        form = CommentForm()
    context = {"cake": cake, "form":form}
    return render(request,"menu/detail.html",context)

@login_required
def cupcake_new(request):
    if request.method == "POST":
        print("here - ")
        form = CupcakeForm(request.POST,request.FILES)
        if form.is_valid():
            print("here - 2")
            cake = form.save(commit=False)
            cake.createdAt = timezone.now()
            cake.writer = request.user
            cake.save()
            print("here ---")
            return redirect('cupcake_detail',pk=cake.pk)
    else:
        form = CupcakeForm()
    context = {'form':form}
    return render(request,"menu/cupcake_new.html",context)

# REST Framework

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET'])
def cupcakes_list(request):
    """
    REST Api V1
    List all cupcakes
    """
    if request.method == 'GET':
        cakes = Cupcake.objects.all().order_by('-createdAt')
        serializer = CupcakeSerializer(cakes, many=True)
        cake_json = Response(serializer.data)
        return JSONResponse(serializer.data)
