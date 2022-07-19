import pytest
from django.test import TestCase
from django.urls import reverse


class TestTemplates(TestCase):
    def test_search_view_to_render_search_template(self):
        url = reverse('search')
        response = self.client.get(url)
        
        assert response.status_code ==  200
        self.assertTemplateUsed(response, 'medicines/search.html')
    
    def test_result_view_to_render_result_template(self):
        url = reverse('searchResult')
        response = self.client.get(url)
        
        assert response.status_code ==  200
        self.assertTemplateUsed(response, 'medicines/results.html')