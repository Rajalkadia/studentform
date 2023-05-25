import sys

from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from demo.forms import Stdudent_form
from demo.models import Student


# Create your views here.


# def student(request):
#     std = Student.objects.all()
#     return render(request, 'student.html', {'student': std})


class std(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student.html'

    def get(self, request):
        stdu = Student.objects.all()
        return Response({'student': stdu})


class std_form(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_form.html'

    def get(self, request):
        return Response()

    def post(self, request):
        form = Stdudent_form(request.POST)
        print("-----------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/student/")
            except:
                print("-------------", sys.exc_info())
        else:
            form = Stdudent_form()
        return Response({'form': form})


class std_del(APIView):

    def get(self, request, id):
        dls = Student.objects.get(std_id=id)
        dls.delete()
        return redirect("/student/")


class std_update(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_update.html'

    def get(self, request, id):
        st = Student.objects.get(std_id=id)
        return Response({'std': st})

    def post(self, request, id):
        st = Student.objects.get(std_id=id)
        form = Stdudent_form(request.POST, instance=st)
        print("-----------------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/student/")
            except:
                print("-------------", sys.exc_info())
        else:
            form = Stdudent_form()
        return Response({'form': form, 'std': st})

