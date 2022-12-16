from django.shortcuts import render
from django.http import HttpResponse

class Finch: 
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species
        self.description = description
        self.age = age

finches = [
    Finch('Mary', 'Black Rosy Finch', 'This nearly black finch has a gray cap and pink highlights on the wings and belly.', 2 ),
    Finch('Bob', 'Brown-capped Rosy-Finches', 'With its rosy pink belly and brown upperparts, the Brown-capped Rosy-Finch looks like raspberry ice cream smothered in chocolate', 1 ),
    Finch('Sal', 'Darwin Finches', "Darwin's finches are a group of about 18 species of passerine birds. They are well known for their remarkable diversity in beak form and function.", 10 ),
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>');

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render (request, 'finches/index.html', { 'finches': finches })