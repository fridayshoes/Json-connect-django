import json
import os
from django.http import JsonResponse
from django.conf import settings

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