from django.http import HttpResponse

def home(request):
   text = """<h1>This is sample page for AWS Beanstalk written in Python</h1>"""
   return HttpResponse(text)