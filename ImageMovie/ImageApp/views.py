from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import TestModel
from django import forms
from .forms import SingleUploadModelForm
from django.forms import formset_factory,modelformset_factory
from django.core.files.storage import FileSystemStorage
from . import forms
import os

def index(request):
    TestModel.objects.all().delete()

    #ファイルの削除
    path = "image/"
    files = os.listdir(path)
    if files !=[]:
        for file in files:
            os.remove('image/'+file)

    return render(request,'index.html')

def uploadfunc(request):
    EXTRA = 3000
    num=len(TestModel.objects.all())

    UploadModelFormSet = modelformset_factory(TestModel, form=SingleUploadModelForm,extra=EXTRA)
    # print(len(request.FILES))
    formset = UploadModelFormSet(request.POST or None, files=request.FILES or None, queryset=TestModel.objects.none())
    if request.method == 'POST': #画像が選択され，送信されたとき
        #file_path = os.path.join('',request.FILES)
        formset.save() #データベースに保存
        #print(request.POST)

        if 'button'in request.POST:
            TestModel.objects.all().delete()
            #ファイルの削除
            path = "image/"
            files = os.listdir(path)
            if files !=[]:
                for file in files:
                    os.remove('image/'+file)
        
        num = len(TestModel.objects.all())
        # last_file = TestModel.objects.all()

        
    context = {
        'form': formset,
        'number_list': list(range(EXTRA)),
        'total_number': EXTRA,
        'num':num,
        # 'last_file':last_file
        
    }
    return render(request, 'image_upload.html', context)

def ImageMovie(request):
    #file_path = TestModel.objects.get(pk=1)
    # file_path={}
    # file_name=""
    # for i,name in enumerate(TestModel.objects.all()):
    #     file_name = "image"+str(i)
    #     file_path[file_name]=name
    # len_list=[k for k in range(0,len(file_path))]
    # file_path['len']=len_list

    file_path = []
    for i,name in enumerate(TestModel.objects.all()):
        #  file_path.append("image"+str(i))
        #  file_path.append(f'{name}')
         file_path.append(name)

    return render(request,'image_movie.html',

    context={"file_path":file_path,
    "file" : file_path[0],
    "len": len(file_path)
    })

