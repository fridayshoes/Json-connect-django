import json
import os
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def read_json(request):
    """
    View function to read a local JSON file and return its content as an HTTP response.
    """
    # 1. Construct the absolute path to the JSON file.
    # settings.BASE_DIR points to your project root. 
    # This joins: /your/project/path + 'service1' + 'data.json'
    file_path = os.path.join(settings.BASE_DIR, 'service1', 'data.json')
    
    # 2. Open the file in 'r' (read) mode using a context manager ('with').
    # This ensures the file is closed automatically even if an error occurs.
    with open(file_path, 'r') as file:
        # 3. Parse the raw text from the file into a Python list or dictionary.
        data = json.load(file)

    # 4. Return a JsonResponse. 
    # 'safe=False' is required because 'data' is likely a list (from your dummy data).
    # By default, JsonResponse expects a dictionary (dict).
    return JsonResponse(data, safe=False)

def read_more_json(request):
    """
    Another view function to read a different JSON file and return its content.
    This is just an example of how you can have multiple endpoints for different files.
    """
    file_path2 = os.path.join(settings.BASE_DIR, 'service1', 'records.json')
    
    with open(file_path2, 'r') as file:
        data = json.load(file)

    return JsonResponse(data, safe=False)


# @csrf_exempt: This decorator allows external tools (like Postman or a frontend) 
# to send POST requests without needing a CSRF security token. 
# Use this cautiously in real banking apps!
@csrf_exempt
def filter_by_age(request):
    """
    View to filter a JSON list based on an 'age' sent via a POST request.
    """
    # 1. Check if the incoming request is a POST (sending data)
    if request.method == "POST":
        # 2. Parse the raw JSON body from the request into a Python dictionary
        body = json.loads(request.body)
        
        # 3. Extract the 'age' value from the dictionary
        age_to_match = body.get("age")
 
        # 4. Build the absolute path to your data.json file inside 'service1' folder
        file_path = os.path.join(settings.BASE_DIR, "service1", "data.json")
 
        # 5. Open and load the local JSON file
        with open(file_path, "r") as file:
            data = json.load(file)
 
        # 6. List Comprehension: Create a new list containing only the items 
        # where the "age" key matches the user's input.
        filtered_data = [record for record in data if record["age"] == age_to_match]
 
        # 7. Return the filtered list as JSON. safe=False is needed for lists.
        return JsonResponse(filtered_data, safe=False)
 
    # 8. Error handling: If someone tries to visit this via a browser URL (GET), 
    # return an error message.
    return JsonResponse({"error": "Only POST method allowed"}, status=405)


@csrf_exempt
def filter_by_bonus(request):
    """
    View to filter a JSON list based on a 'bonus' value sent via a GET request.
    """
    if request.method == "GET":
        # bonus_to_match = request.GET.get("bonus")

        file_path = os.path.join(settings.BASE_DIR, "service1", "records.json")

        with open(file_path, "r") as file:
            data = json.load(file)

        filtered_data = [record for record in data if record["bonus"] >= 3000]

        return JsonResponse(filtered_data, safe=False)

    return JsonResponse({"error": "Only GET method allowed"}, status=405)


@csrf_exempt
def filter_by_bonus_and_age(request):
    if request.method == "GET":
        # bonus_to_match = request.GET.get("bonus")
        # age_to_match = request.GET.get("age")

        file_path = os.path.join(settings.BASE_DIR, "service1", "records.json")

        with open(file_path, "r") as file:
            data = json.load(file)

        filtered_data = [
            record for record in data 
            if record["bonus"] >= 3000 and record["age"] == 34
        ]

        return JsonResponse(filtered_data, safe=False)

    return JsonResponse({"error": "Only GET method allowed"}, status=405)
