from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Week, Todo
from .forms import TodoWeekForm, TodoTodoForm


class WeekModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test_user', password='1234')
        Week.objects.create(title=f'test-week', user_id=user.id)

    def test_title(self):
        field_label = Week._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        max_length = Week._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_user(self):
        field_label = Week._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_archived(self):
        field_label = Week._meta.get_field('archived').verbose_name
        self.assertEqual(field_label, 'archived')
        default = Week._meta.get_field('archived').default
        self.assertEqual(default, False)

    def test_object_name_is_title(self):
        week = Week.objects.get(id=1)
        expected_object_name = week.title
        self.assertEqual(str(week), expected_object_name)


class TodoModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test_user', password='1234')
        week = Week.objects.create(title='test-week', user_id=user.id)
        for i in range(10):
            Todo.objects.create(title=f'test-todo-{i}', week_id=week.id)

    def test_title(self):
        field_label = Todo._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        max_length = Todo._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_md(self):
        field_label = Todo._meta.get_field('md').verbose_name
        self.assertEqual(field_label, 'md')
        default = Todo._meta.get_field('md').default
        self.assertEqual(default, 0)

    def test_td(self):
        field_label = Todo._meta.get_field('td').verbose_name
        self.assertEqual(field_label, 'td')
        default = Todo._meta.get_field('td').default
        self.assertEqual(default, 0)

    def test_wd(self):
        field_label = Todo._meta.get_field('wd').verbose_name
        self.assertEqual(field_label, 'wd')
        default = Todo._meta.get_field('wd').default
        self.assertEqual(default, 0)

    def test_th(self):
        field_label = Todo._meta.get_field('th').verbose_name
        self.assertEqual(field_label, 'th')
        default = Todo._meta.get_field('th').default
        self.assertEqual(default, 0)

    def test_fr(self):
        field_label = Todo._meta.get_field('fr').verbose_name
        self.assertEqual(field_label, 'fr')
        default = Todo._meta.get_field('fr').default
        self.assertEqual(default, 0)

    def test_st(self):
        field_label = Todo._meta.get_field('st').verbose_name
        self.assertEqual(field_label, 'st')
        default = Todo._meta.get_field('st').default
        self.assertEqual(default, 0)

    def test_sd(self):
        field_label = Todo._meta.get_field('sd').verbose_name
        self.assertEqual(field_label, 'sd')
        default = Todo._meta.get_field('sd').default
        self.assertEqual(default, 0)

    def test_week(self):
        field_label = Todo._meta.get_field('week').verbose_name
        self.assertEqual(field_label, 'week')

    def test_object_name_is_title(self):
        todo = Week.objects.get(id=1)
        expected_object_name = todo.title
        self.assertEqual(str(todo), expected_object_name)


class TodoWeekFormTestClass(TestCase):
    def test_title(self):
        form = TodoWeekForm()
        field_label = form.fields['title'].label
        self.assertEqual(field_label, 'Title')
        self.assertTrue(form.fields['title'].required)

    def test_title_valid_data(self):
        form = TodoWeekForm(data={'title': 'ValidTitle'})
        self.assertTrue(form.is_valid())

    def test_title_too_long_data(self):
        form = TodoWeekForm(data={'title': '123456789012345678901234567890123456789012345678901234567890123456789012 '
                                           '34567890123456789012345678901'})
        self.assertFalse(form.is_valid())

    def test_title_empty_data(self):
        form = TodoWeekForm(data={'title': ' '})
        self.assertFalse(form.is_valid())


class TodoTodoFormTestClass(TestCase):
    def test_title(self):
        form = TodoTodoForm()
        field_label = form.fields['title'].label
        self.assertEqual(field_label, 'Title')
        self.assertTrue(form.fields['title'].required)

    def test_title_valid_data(self):
        data = {'id': 1, 'title': 'ValidData', 'md': 1, 'td': 1, 'wd': 1, 'th': 1, 'fr': 1, 'st': 1, 'sd': 1}
        form = TodoTodoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_title_too_long_data(self):
        data = {'id': 1, 'title': '1234567890123456789012345678901234567890123456789012345678901234567890123456789 '
                                  '012345678901234567890q', 'md': 1, 'td': 1, 'wd': 1, 'th': 1, 'fr': 1, 'st': 1,
                'sd': 1}
        form = TodoTodoForm(data=data)
        self.assertFalse(form.is_valid())

    def test_title_empty_data(self):
        data = {'id': 1, 'title': ' ', 'md': 1, 'td': 1, 'wd': 1, 'th': 1, 'fr': 1, 'st': 1,
                'sd': 1}
        form = TodoTodoForm(data=data)
        self.assertFalse(form.is_valid())

    def test_md(self):
        form = TodoTodoForm()
        field_label = form.fields['md'].label
        self.assertEqual(field_label, 'Md')
        self.assertTrue(form.fields['md'].required)

    def test_td(self):
        form = TodoTodoForm()
        field_label = form.fields['td'].label
        self.assertEqual(field_label, 'Td')
        self.assertTrue(form.fields['td'].required)

    def test_wd(self):
        form = TodoTodoForm()
        field_label = form.fields['wd'].label
        self.assertEqual(field_label, 'Wd')
        self.assertTrue(form.fields['wd'].required)

    def test_th(self):
        form = TodoTodoForm()
        field_label = form.fields['th'].label
        self.assertEqual(field_label, 'Th')
        self.assertTrue(form.fields['th'].required)

    def test_fr(self):
        form = TodoTodoForm()
        field_label = form.fields['fr'].label
        self.assertEqual(field_label, 'Fr')
        self.assertTrue(form.fields['fr'].required)

    def test_st(self):
        form = TodoTodoForm()
        field_label = form.fields['st'].label
        self.assertEqual(field_label, 'St')
        self.assertTrue(form.fields['st'].required)

    def test_sd(self):
        form = TodoTodoForm()
        field_label = form.fields['sd'].label
        self.assertEqual(field_label, 'Sd')
        self.assertTrue(form.fields['sd'].required)


class ViewTestClass(TestCase):
    def setUp(self):
        self.test_user1 = User.objects.create_user(username='test1', password='test1')
        self.test_user1.save()
        self.week1 = Week.objects.create(title='test_week1', user_id=self.test_user1.id)
        self.week1.save()
        self.todo1 = Todo.objects.create(id=1, title='test_todo1', week_id=self.week1.pk)
        self.todo1.save()

    def test_week_list_if_not_authenticated(self):
        response = self.client.get(reverse('week_list'))
        self.assertRedirects(response, '/login/?next=/week_list/')

    def test_week_list_if_authenticated(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('week_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/week_list.html')

    def test_week_list_archive_if_not_authenticated(self):
        response = self.client.get(reverse('week_list_archive'))
        self.assertRedirects(response, '/login/?next=/week_list_archive/')

    def test_week_list_archive_if_authenticated(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('week_list_archive'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/week_archive.html')

    def test_week_show_if_not_authenticated(self):
        response = self.client.get(reverse('week_show', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/login/?next=/week/1')

    def test_week_show_archive_if_authenticated(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('week_show', kwargs={'week_pk': self.week1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/week_show.html')

    def test_week_create_if_not_authenticated(self):
        response = self.client.get(reverse('week_create'))
        self.assertRedirects(response, '/login/?next=/week/week_create')

    def test_week_create_archive_if_authenticated_get(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('week_create'))
        self.assertRedirects(response, '/week_list/')
        self.assertEqual(response.status_code, 302)

    def test_week_create_archive_if_authenticated_post_valid_data(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('week_create'), {'title': 'test2'})
        new_week = Week.objects.filter(title='test2')
        self.assertTrue(new_week is not None)
        self.assertRedirects(response, '/week_list/')
        self.assertEqual(response.status_code, 302)

    def test_week_create_archive_if_authenticated_post_invalid_data(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('week_create'), {'title': '   '})
        new_week = Week.objects.filter(title='test2')
        self.assertTrue(str(new_week) == '<QuerySet []>')
        self.assertRedirects(response, '/week_list/')
        self.assertEqual(response.status_code, 302)

    def test_week_edit_if_not_authenticated(self):
        response = self.client.get(reverse('week_edit', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/login/?next=/week/1/week_edit')

    def test_week_edit_archive_if_authenticated_get(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('week_edit', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/week_list/')
        self.assertEqual(response.status_code, 302)

    def test_week_edit_archive_if_authenticated_post_valid_data(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('week_edit', kwargs={'week_pk': self.week1.pk}), {'title': 'test2'})
        edited_week = Week.objects.filter(title='test2')
        self.assertTrue(str(edited_week) != '<QuerySet []')
        self.assertRedirects(response, '/week_list/')
        self.assertEqual(response.status_code, 302)

    def test_week_edit_archive_if_authenticated_post_invalid_data(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('week_edit', kwargs={'week_pk': self.week1.pk}), {'title': '   '})
        edited_week = Week.objects.filter(title='test2')
        self.assertTrue(str(edited_week) == '<QuerySet []>')
        self.assertRedirects(response, '/week_list/')
        self.assertEqual(response.status_code, 302)

    def test_week_edit_archive_if_authenticated_post_invalid_week_pk(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('week_edit', kwargs={'week_pk': 123}), {})
        self.assertEqual(response.status_code, 404)

    def test_week_delete_if_not_authenticated(self):
        response = self.client.get(reverse('week_delete', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/login/?next=/week/1/week_delete')

    def test_week_archive_if_not_authenticated(self):
        response = self.client.get(reverse('week_archive', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/login/?next=/week/1/week_archive')

    def test_week_archive_archive_if_authenticated_get(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('week_edit', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/week_list/')
        self.assertEqual(response.status_code, 302)

    def test_week_archive_archive_if_authenticated_post_valid_data(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('week_archive', kwargs={'week_pk': self.week1.pk}))
        archived_week = Week.objects.get(id=self.week1.pk)
        self.assertEqual(archived_week.archived, True)
        self.assertRedirects(response, '/week_list/')
        self.assertEqual(response.status_code, 302)

    def test_week_archive_archive_if_authenticated_post_invalid_week_pk(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('week_archive', kwargs={'week_pk': 123}), {})
        self.assertEqual(response.status_code, 404)

    def test_week_unarchive_if_not_authenticated(self):
        response = self.client.get(reverse('week_unarchive', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/login/?next=/week/1/week_unarchive')

    def test_week_unarchive_archive_if_authenticated_get(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('week_unarchive', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/week_list_archive/')
        self.assertEqual(response.status_code, 302)

    def test_week_unarchive_archive_if_authenticated_post_valid_data(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('week_unarchive', kwargs={'week_pk': self.week1.pk}))
        archived_week = Week.objects.get(id=self.week1.pk)
        self.assertEqual(archived_week.archived, False)
        self.assertRedirects(response, '/week_list_archive/')
        self.assertEqual(response.status_code, 302)

    def test_week_unarchive_archive_if_authenticated_post_invalid_week_pk(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('week_unarchive', kwargs={'week_pk': 123}), {})
        self.assertEqual(response.status_code, 404)

    def test_todo_create_if_not_authenticated(self):
        response = self.client.get(reverse('todo_create', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/login/?next=/week/1/todo_create')

    def test_todo_create_archive_if_authenticated_get(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('todo_create', kwargs={'week_pk': self.week1.pk}))
        self.assertRedirects(response, '/week/1')
        self.assertEqual(response.status_code, 302)

    def test_todo_create_archive_if_authenticated_post_valid_data(self):
        self.client.login(username='test1', password='test1')
        numOfTodos = len(Todo.objects.all())
        response = self.client.post(reverse('todo_create', kwargs={'week_pk': self.week1.pk}), {})
        numOfTodos -= len(Todo.objects.all())
        self.assertEqual(numOfTodos, -1)
        self.assertRedirects(response, '/week/1')
        self.assertEqual(response.status_code, 302)

    def test_todo_create_archive_if_authenticated_post_invalid_week_pk(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('todo_create', kwargs={'week_pk': 123}), {})
        self.assertEqual(response.status_code, 404)

    def test_todo_edit_if_not_authenticated(self):
        response = self.client.get(reverse('todo_edit', kwargs={'week_pk': self.week1.pk, 'todo_pk': self.todo1.pk}))
        self.assertRedirects(response, '/login/?next=/week/1/todo_edit/1')

    def test_todo_edit_archive_if_authenticated_get(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('todo_edit', kwargs={'week_pk': self.week1.pk, 'todo_pk': self.todo1.pk}))
        self.assertRedirects(response, '/week/1')
        self.assertEqual(response.status_code, 302)

    def test_todo_edit_archive_if_authenticated_post_valid_data(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('todo_edit', kwargs={'week_pk': self.week1.pk, 'todo_pk': self.todo1.pk}),
                                    {'title': 'test2', 'md': 1, 'td': 1, 'wd': 1, 'th': 1, 'fr': 1, 'st': 1, 'sd': 1})
        edited_todo = Todo.objects.get(title='test2')
        self.assertTrue(edited_todo is not None)
        self.assertRedirects(response, '/week/1')
        self.assertEqual(response.status_code, 302)

    def test_todo_edit_archive_if_authenticated_post_invalid_data(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('todo_edit', kwargs={'week_pk': self.week1.pk, 'todo_pk': self.todo1.pk}),
                                    {'title': '  ', 'md': 1, 'td': 1, 'wd': 1, 'th': 1, 'fr': 1, 'st': 1, 'sd': 1})
        edited_todo = Todo.objects.get(title='test_todo1')
        self.assertTrue(edited_todo is not None)
        self.assertRedirects(response, '/week/1')
        self.assertEqual(response.status_code, 302)

    def test_todo_edit_archive_if_authenticated_post_invalid_pk(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('todo_edit', kwargs={'week_pk': 123, 'todo_pk': 123}), {})
        self.assertEqual(response.status_code, 404)

    def test_todo_delete_if_not_authenticated(self):
        response = self.client.get(reverse('todo_delete', kwargs={'week_pk': self.week1.pk, 'todo_pk': self.todo1.pk}))
        self.assertRedirects(response, '/login/?next=/week/1/todo_delete/1')

    def test_todo_delete_archive_if_authenticated_get(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('todo_delete', kwargs={'week_pk': self.week1.pk, 'todo_pk': self.todo1.pk}))
        self.assertRedirects(response, '/week/1')
        self.assertEqual(response.status_code, 302)

    def test_todo_delete_archive_if_authenticated_post_valid_data(self):
        self.client.login(username='test1', password='test1')
        numOfTodos = len(Todo.objects.all())
        response = self.client.post(reverse('todo_delete', kwargs={'week_pk': self.week1.pk, 'todo_pk': self.todo1.pk}), {})
        numOfTodos -= len(Todo.objects.all())
        self.assertEqual(numOfTodos, 1)
        self.assertRedirects(response, '/week/1')
        self.assertEqual(response.status_code, 302)

    def test_todo_delete_archive_if_authenticated_post_invalid_pk(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post(reverse('todo_delete', kwargs={'week_pk': 123, 'todo_pk': 123}), {})
        self.assertEqual(response.status_code, 404)