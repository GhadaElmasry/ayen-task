import os
import pytest
from medicines.views import read_from_csv_file

# Create your tests here.
class TestReadCSVFile:
    def test_read_from_csv_file_successfully(self, rootdir):
        data = read_from_csv_file(rootdir, 'test_files/test_dummy_data.csv')
        assert len(data) == 7
    
    def test_read_from_csv_file_not_exisiting_file (self, rootdir):
        with pytest.raises(FileNotFoundError):
            data = read_from_csv_file(rootdir, 'test_files/test_dummy.csv')

