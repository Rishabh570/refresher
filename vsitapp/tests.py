from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post
from unittest.mock import patch
from . import views

class TestCoreClass(TestCase):

    def setUp(self):
        self.c = Client()
        user = User.objects.create(username='foo')
        user.set_password('bar')
        user.save()

        Post.objects.create(first_name='post', author='foo', title='dev', story='hi there', votings=1, id=111)
        print("\n===============\nSetUp worked!\n===============\n")

    def tearDown(self):
        User.objects.get(username='foo').delete()
        Post.objects.get(author='foo').delete()
        print("\n===============\nTear Down applied!\n===============\n")


    def test_home_login_get_view(self):
        response = self.c.get('/home_login/', follow=True)
        self.assertTemplateUsed(response, 'home_loggedin.html')
        self.assertEqual(response.status_code, 200)

    def test_home_login_post_view(self):
        pass
        
    def test_list_view_get_method(self):
        response = self.c.get('/list/', {'title': ''},  follow=True)
        self.assertTemplateUsed(response, 'list.html')
        self.assertEqual(response.status_code, 200)

    # THIS TEST IS MESSED UP RIGHT NOW ==================================================================

    # def test_list_view_post_method(self):
        # self.c.login(username='foo', password='bar')
        # response = self.c.post('/list/', {'g-recaptcha-response': 'something'}, follow=True)
        
        # print('\n', response.content, '\n')
        # print('Redirect_chain: ', response.redirect_chain, '\n')
        # print(response.status_code,'\n')
        
        # with patch('views.list.requests.post') as mocked_response:
        #     mocked_response.return_value.json = "{'success': 'present'}"
        #     mocked_response.return_value.text = 'Success'
        #     mocked_response.return_value.ok = True

        #     if mocked_response.return_value.ok:
        #         self.assertRedirects(response, '/list/')
        #     else:
        #         self.assertRedirects(response, '/help/')
    # ===================================================================================================

    def test_help_view(self):
        self.c.login(username='foo', password='bar')
        response = self.c.get('/help/', follow=True)
        self.assertTemplateUsed(response, 'help_form.html')
        self.assertEqual(response.status_code, 200)

    def test_sign_up_view(self):
        response = self.c.get('/signup/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')

    def test_signup_post_view(self):
        pass

    def test_login_get_view(self):
        response = self.c.get('/login/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_post_view(self):
        pass

    def test_logout_view(self):
        self.c.login(username='foo', password='bar')
        response = self.c.get('/logout/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/home_login/')

    def test_password_change_get_view(self):
        self.c.login(username='foo', password='bar')
        response = self.c.get('/passchangeform/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'passchangeform.html')

    # todo
    def test_password_change_post_view(self):
        pass

    # todo
    def test_upvote_view(self):
        self.c.login(username='foo', password='bar')
        response = self.c.get('/upvote/', {'filter': 111})
        self.assertEqual(response.status_code, 200)

    # todo
    def test_downvote_view(self):
        self.c.login(username='foo', password='bar')
        response = self.c.get('/downvote/', {'filter': 111})
        self.assertEqual(response.status_code, 200)

    # todo
    def test_delete_post_view_success(self):
        self.c.login(username='foo', password='bar')
        response = self.c.get('/delete/', {'post_id': 111})
        self.assertEqual(response.content, b"Success")
        # Created post object again (below) because tearDown will search for the post which is deleted above
        Post.objects.create(first_name='post', author='foo', title='dev', story='hi there', votings=1, id=111)

    # todo
    def test_delete_post_view_failed(self):
        response = self.c.get('/delete/', {'post_id': 111})
        self.assertEqual(response.content, b"You are not authorized to delete this record")

