from django.shortcuts import render

# Create your views here.


def task_board(request):
    return render(request, "your_game/task_board.html")
