from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import TutorApply, TutorRequest, TutorComment, TuteeComment
from .forms import TutorApplyForm, TutorRequestForm, CommentForm, CommentForm2

# Create your views here.
def tutors(request):
    tutorApplys = TutorApply.objects.all()
    paginator = Paginator(tutorApplys, 6)
    page = request.GET.get('page')
    tutor_page = paginator.get_page(page)
    return render(request, 'tutorboard/tutors.html', {'tutor_page': tutor_page, 'tutorApplys': tutorApplys})

def tutees(request):
    tutorRequests = TutorRequest.objects.all()
    paginator = Paginator(tutorRequests, 6)
    page = request.GET.get('page')
    tutee_page = paginator.get_page(page)
    return render(request, 'tutorboard/tutees.html', {'tutee_page': tutee_page, 'tutorRequests': tutorRequests})

def tutorapply(request, tutorapply_id):
    tutorApply = get_object_or_404(TutorApply, pk=tutorapply_id)
    return render(request, 'tutorboard/tutorapply.html', {'tutorApply': tutorApply})

def tutorrequest(request, tutorrequest_id):
    tutorRequest = get_object_or_404(TutorRequest, pk=tutorrequest_id)
    return render(request, 'tutorboard/tutorrequest.html', {'tutorRequest': tutorRequest})

def newtutorapply(request):
    if request.method == "POST":
        form = TutorApplyForm(request.POST, request.FILES)
        if form.is_valid():
            tutorapply = form.save(commit = False) # commit은 데이터베이스의 모든 작업이 저장되었을 때 True가 되는데, 그러면 comment를 더이상 수정하지 못 하게 됨, 우선 commit = False를 해서 뒤에 작업들을 할 수 있게 해줌
            tutorapply.author = request.user
            tutorapply.save()  # 여기는 default가 commit = True라서 따로 설정 안 해줌
            return redirect('tutorapply', tutorapply.pk)
    else:
        form = TutorApplyForm()
    return render(request, 'tutorboard/newtutorapply.html', {'form':form})

def tutorapplyedit(request, tutorapply_id):
    if request.method == "POST":
        tutorApply = get_object_or_404(TutorApply, pk=tutorapply_id)
        form = TutorApplyForm(request.POST, request.FILES, instance=tutorApply)
        if form.is_valid():
            tutorApply = form.save()
            tutorApply.save()
            return redirect('tutorapply', tutorapply_id)
    else:
        tutorApply = get_object_or_404(TutorApply, pk=tutorapply_id)
        form = TutorApplyForm(instance=tutorApply)
    return render(request, 'tutorboard/tutorapplyedit.html', {'tutorApply': tutorApply, 'form': form})

def newtutorrequest(request):
    if request.method == "POST":
        form = TutorRequestForm(request.POST, request.FILES)
        if form.is_valid():
            tutorrequest = form.save(commit = False) # commit은 데이터베이스의 모든 작업이 저장되었을 때 True가 되는데, 그러면 comment를 더이상 수정하지 못 하게 됨, 우선 commit = False를 해서 뒤에 작업들을 할 수 있게 해줌
            tutorrequest.author = request.user
            tutorrequest.save()  # 여기는 default가 commit = True라서 따로 설정 안 해줌
            return redirect('tutorrequest', tutorrequest.pk)
    else:
        form = TutorRequestForm()
    return render(request, 'tutorboard/newtutorrequest.html', {'form': form})

def tutorrequestedit(request, tutorrequest_id):
    if request.method == "POST":
        tutorRequest = get_object_or_404(TutorRequest, pk=tutorrequest_id)
        form = TutorRequestForm(request.POST, request.FILES, instance=tutorRequest)
        if form.is_valid():
            tutorRequest = form.save()
            tutorRequest.save()
            return redirect('tutorrequest', tutorrequest_id)
    else:
        tutorRequest = get_object_or_404(TutorRequest, pk=tutorrequest_id)
        form = TutorRequestForm(instance=tutorRequest)
    return render(request, 'tutorboard/tutorrequestedit.html', {'tutorrequest': tutorrequest, 'form': form})

def tutorrequestremove(request, tutorrequest_id):
    tutorrequest = get_object_or_404(TutorRequest, pk=tutorrequest_id)
    tutorrequest.delete()
    # messages.success(request, 'Post Successfully removed')
    return redirect('tutees')

def tutorapplyremove(request, tutorapply_id):
    tutorapply = get_object_or_404(TutorApply, pk=tutorapply_id)
    tutorapply.delete()
    # messages.success(request, 'Post Successfully removed')
    return redirect('tutors')


def tutorComment(request, tutorrequest_id):
    post = get_object_or_404(TutorRequest, pk=tutorrequest_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.save()
            return redirect('tutorrequest', post.pk)
    else:
        form = CommentForm()
        return render(request, 'tutorboard/tutorrequest.html', {'form': form, 'tutorRequest': post})

def tuteeComment(request, tutorapply_id):
    post = get_object_or_404(TutorApply, pk=tutorapply_id)
    if request.method == 'POST':
        form = CommentForm2(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.save()
            return redirect('tutorapply', post.pk)
    else:
        form = CommentForm2()
        return render(request, 'tutorboard/tutorapply.html', {'form': form, 'tutorApply': post})
