from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Bouquet, Comment, Vote

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def bouquet_list(request):
    bouquets = Bouquet.objects.all().order_by('-created_at')
    return render(request, 'flowers/bouquet_list.html', {'bouquets': bouquets})

def bouquet_detail(request, share_id):
    bouquet = get_object_or_404(Bouquet, share_id=share_id)
    comments = bouquet.comments.all().order_by('-created_at')
    vote_count = bouquet.votes.count()
    user_has_voted = False
    if request.user.is_authenticated:
        user_has_voted = bouquet.votes.filter(user=request.user).exists()
    
    return render(request, 'flowers/bouquet_detail.html', {
        'bouquet': bouquet,
        'comments': comments,
        'vote_count': vote_count,
        'user_has_voted': user_has_voted,
    })

@login_required
def add_comment(request, share_id):
    if request.method == 'POST':
        bouquet = get_object_or_404(Bouquet, share_id=share_id)
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                bouquet=bouquet,
                author=request.user,
                text=text
            )
            messages.success(request, 'Comment added successfully!')
        return redirect('bouquet_detail', share_id=share_id)

@login_required
def toggle_vote(request, share_id):
    if request.method == 'POST':
        bouquet = get_object_or_404(Bouquet, share_id=share_id)
        vote, created = Vote.objects.get_or_create(
            bouquet=bouquet,
            user=request.user,
            defaults={'bouquet': bouquet, 'user': request.user}
        )
        if not created:
            vote.delete()
        
        return JsonResponse({
            'vote_count': bouquet.votes.count(),
            'user_has_voted': created
        })
