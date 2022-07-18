from django.shortcuts import render
from django.template import loader
import csv
import os
# Create your views here.
from django.http import HttpResponse

# 
def search(request):
    medicines = read_from_csv_file(os.path.dirname(__file__),"medical_dataset.csv")
    context = {
        "medicines": medicines
    }

    return render(request, 'medicines/search.html', context)

def read_from_csv_file(path, file_name):
    file= os.path.join(path, file_name)
    med_dict = {}
    
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1

            med_dict[row["Key"]]= row["Values"]
            line_count += 1

        print(f'Processed {line_count} lines.')

    return med_dict
