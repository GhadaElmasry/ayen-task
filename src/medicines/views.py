import csv
import os
from difflib import SequenceMatcher

from django.shortcuts import render
from django.template import loader


# search_result returns the values, matching precentage and results template 
def search_result(request):
    selected_key = request.POST.get('medicines_keys', None) # this variable now contains the selected value.
    data = request.session.get("data")
       
    results = get_match_values_of_key(selected_key, data)
 
    context = {
        "key" : selected_key,
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
        csv_file.close()

    return med_dict


# get_matching_precentage returns the ratio of text matching 
def get_matching_precentage(str1, str2):
    s = SequenceMatcher(None, str1.lower(), str2.lower())
    
    return round(s.ratio()*100, 2)

# get_matched_values_of_key returns the match values of the specfic key
def get_match_values_of_key(key, data):
    results ={} 

    if data is None:
        return results
    
    for k, v in data.items():
        prec = get_matching_precentage(key, v)
        if prec > 50 :
            results[k]= [v, prec]
    
    return results