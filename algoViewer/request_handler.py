from django.http import HttpResponseRedirect

def sort_file(request):
  if request.method == 'POST':
    