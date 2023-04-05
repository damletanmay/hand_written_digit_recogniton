import os
from django.shortcuts import render, redirect
from .hindi_english import predict_hindi_digit,predict_english_digit
from django.conf import settings

def root(request):
    return render(request, 'index.html')

def hindi_english(request):
    language = request.POST.get('language-select')

    uploaded_file = request.FILES.get('image')
    if uploaded_file:
        # create a temporary directory for the uploaded image
        temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp_images')
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        # save the uploaded image to the temporary directory
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

    result = -1

    print(file_path)
    print(language)

    if language == 'hindi':
        result = predict_hindi_digit(file_path)
    elif language == 'english':
        result = predict_english_digit(file_path)

    print(type(result))
    print(result)

    if result == -1:
        result_string = f'Unable to determine Image Provided'
    else:
        result_string = f'Your Image is Probably a {result}'

    if os.path.exists(file_path):
        os.remove(file_path)

    return render(request, 'index.html', {'result': result_string})
    # return render(request, 'result.html')
