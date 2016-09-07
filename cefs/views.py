from django.shortcuts import render
from django.utils import timezone
from .models import Chapter, supChapter
from django.shortcuts import render, get_object_or_404, redirect

def chapter_list(request):
	chapters = Chapter.objects.all()
	return render(request, 'cefs/chapter_list.html', {'chapters':chapters})


def subchapter_list(request, pk):
	subchapters = supChapter.objects.all()

	return render(request, 'cefs/subchapter_list.html', {'subchapters':subchapters})


def detail(request, pk):
	course = get_object_or_404(supChapter, pk=pk)
	return render(request, 'cefs/detail.html', {'course':course})