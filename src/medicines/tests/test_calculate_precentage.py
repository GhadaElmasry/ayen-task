from medicines.views import get_matching_precentage

class TestGetMatchingPrecentage:
    def test_get_matching_precentage_successfully(self):
        ratio = get_matching_precentage("abcd", "ab123")
        assert ratio == 44.44
    
    def test_get_matching_precentage_with_empty_strings(self):
        ratio = get_matching_precentage("", "ab123")
        assert ratio == 0.0
        
    def test_get_matching_precentage_with_same_string(self):
        ratio = get_matching_precentage("ab123", "ab123")
        assert ratio == 100
    