from django.core.files.uploadedfile import UploadedFile

def sort_file_handler(formData):
  print(formData["file"].read())