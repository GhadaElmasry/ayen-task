import csv
import os
from difflib import SequenceMatcher

from django.shortcuts import render
from django.template import loader


# search_result returns the values, matching precentage and results template 
def search_result(request):
    select_value = request.POST.get('medicines_keys', None) # this variable now contains the selected value.
    data = None

    results ={} 
    
    print(f'users key: {select_value}, users value: {data[select_value]}')
    
    for k, v in data.items():
        prec = get_matching_precentage(data[select_value], data[k])
        if prec > 50 :
            print(f'match key : {k}, match value: {v}, score: {prec}')
            results[k]= [v, prec]
 
    context = {
        "key" : select_value,
        "results": results
    }

    return render(request, 'medicines/results.html', context)


# search returns the search template with keys and values from file
def search(request):
    medicines = read_from_csv_file(os.path.dirname(__file__),"medical_dataset.csv")
    context = {
        "medicines": medicines
    }

    request.session["data"] = medicines

    return render(request, 'medicines/search.html', context)

# read_from_csv_file reads the records from csv file
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

def get_matching_precentage(str1, str2):
    s = SequenceMatcher(None, str1, str2)
    return s.ratio()*100