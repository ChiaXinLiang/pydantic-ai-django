from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ChatSession, Message
from api.models import CustomUser


class ChatTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        # Get JWT token
        response = self.client.post(reverse('token_obtain_pair'), {
            'email': 'test@example.com',
            'password': 'testpass123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Create test chat session
        self.chat_session = ChatSession.objects.create(
            session_id='test-session-1',
            is_active=True
        )

    def test_create_chat_session(self):
        """Test creating a new chat session"""
        url = reverse('chat:chat-sessions')
        data = {
            'session_id': 'test-session-2',
            'is_active': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatSession.objects.count(), 2)
        self.assertEqual(ChatSession.objects.get(session_id='test-session-2').is_active, True)

    def test_list_chat_sessions(self):
        """Test listing all chat sessions"""
        url = reverse('chat:chat-sessions')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_message(self):
        """Test creating a new message in a chat session"""
        url = reverse('chat:messages')
        data = {
            'session': str(self.chat_session.id),
            'role': 'user',
            'content': 'Hello, this is a test message'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.first().content, 'Hello, this is a test message')

    def test_list_messages(self):
        """Test listing all messages"""
        # Create a test message first
        Message.objects.create(
            session=self.chat_session,
            role='user',
            content='Test message'
        )
        url = reverse('chat:messages')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_chat_session_detail(self):
        """Test retrieving a specific chat session"""
        url = reverse('chat:chat-session-detail', kwargs={'pk': self.chat_session.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['session_id'], 'test-session-1')

    def test_update_chat_session(self):
        """Test updating a chat session"""
        url = reverse('chat:chat-session-detail', kwargs={'pk': self.chat_session.id})
        data = {
            'session_id': 'test-session-1',
            'is_active': False
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ChatSession.objects.get(id=self.chat_session.id).is_active, False)

    def test_delete_chat_session(self):
        """Test deleting a chat session"""
        url = reverse('chat:chat-session-detail', kwargs={'pk': self.chat_session.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ChatSession.objects.count(), 0)
