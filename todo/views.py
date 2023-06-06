from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TodoWeekForm, TodoTodoForm
from .models import Week, Todo


@login_required
def week_list(request):
    """Shows the list of not archived 'Weeks'"""
    form = TodoWeekForm()
    weeks_list = Week.objects.filter(user=request.user, archived=False)
    context = {'form': form, 'weeks_list': weeks_list}
    return render(request, 'todo/week_list.html', context)


@login_required
def week_list_archive(request):
    """Shows the list of archived 'Weeks'"""
    weeks_list = Week.objects.filter(user=request.user, archived=True)
    context = {'weeks_list': weeks_list}
    return render(request, 'todo/week_archive.html', context)


@login_required
def week_show(request, week_pk):
    """Shows week content('To do' elements)"""
    current_week = get_object_or_404(Week, pk=week_pk, user=request.user)
    todo_list = Todo.objects.filter(week=week_pk)
    form = TodoTodoForm()
    context = {'week': current_week, 'todo_list': todo_list, 'form': form}
    return render(request, 'todo/week_show.html', context=context)


@login_required
def week_create(request):
    """Creates a new 'Week' element belongs to the User"""
    if request.method == 'GET':
        return redirect('week_list')
    else:
        try:
            form = TodoWeekForm(request.POST)
            new_week = form.save(commit=False)
            new_week.user = request.user
            new_week.save()
            return redirect('week_list')
        except ValueError:
            messages.add_message(request, messages.INFO, 'Bad data passed in. Try again')
            return redirect('week_list')


@login_required
def week_edit(request, week_pk):
    """Edits a 'Week' element"""
    if request.method == 'GET':
        return redirect('week_list')
    else:
        try:
            current_week = get_object_or_404(Week, pk=week_pk)
            week_changed = TodoWeekForm(request.POST, instance=current_week)
            week_changed.save()
            return redirect('week_list')
        except ValueError:
            messages.add_message(request, messages.INFO, 'Bad data passed in. Try again')
            return redirect('week_list')


@login_required
def week_delete(request, week_pk):
    """Deletes 'Week' element"""
    if request.method == "GET":
        pass
    else:
        week = get_object_or_404(Week, pk=week_pk, user=request.user)
        week.delete()
    referrer_array = str(request.META["HTTP_REFERER"]).split('/')
    referer = referrer_array[len(referrer_array) - 2]
    return redirect(referer)


@login_required
def week_archive(request, week_pk):
    """Archives 'Week' element"""
    if request.method == "GET":
        return redirect('week_list')
    else:
        week = get_object_or_404(Week, pk=week_pk, user=request.user)
        week.archived = True
        week.save()
        return redirect('week_list')


@login_required
def week_unarchive(request, week_pk):
    """Unarchives 'Week' element"""
    if request.method == "GET":
        return redirect('week_list_archive')
    else:
        week = get_object_or_404(Week, pk=week_pk, user=request.user)
        week.archived = False
        week.save()
        return redirect('week_list_archive')


@login_required
def todo_create(request, week_pk):
    """Creates a new 'To do' element belongs to the User connected to the Week"""
    if request.method == "GET":
        return redirect('week_show', week_pk=week_pk)
    else:
        week = get_object_or_404(Week, pk=week_pk, user=request.user)
        new_todo = Todo(title='', week_id=week.id)
        new_todo.save()
        return redirect('week_show', week_pk=week.id)


@login_required
def todo_edit(request, week_pk, todo_pk):
    if request.method == 'GET':
        return redirect('week_show', week_pk=week_pk)
    else:
        try:
            current_todo = get_object_or_404(Todo, pk=todo_pk)
            todo_changed = TodoTodoForm(request.POST, instance=current_todo)
            todo_changed.save()
            return redirect('week_show', week_pk=week_pk)
        except ValueError:
            messages.add_message(request, messages.INFO, 'Bad data passed in. Try again')
            return redirect('week_show', week_pk=week_pk)


@login_required
def todo_delete(request, week_pk, todo_pk):
    """Deletes 'To do' element"""
    if request.method == "GET":
        return redirect('week_show', week_pk=week_pk)
    else:
        week = get_object_or_404(Week, pk=week_pk, user=request.user)
        todo = get_object_or_404(Todo, pk=todo_pk, week_id=week.id)
        todo.delete()
        return redirect('week_show', week_pk=week.id)
