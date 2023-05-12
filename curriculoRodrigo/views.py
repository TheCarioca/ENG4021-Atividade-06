from django.shortcuts import render, redirect
from .models import Task, University, Language, Hability
from .forms import TaskForm, UniversityForm, LanguageForm, HabilityForm

# Create your views here.
def home(request):
  universities = University.objects.all()
  languages = Language.objects.all()
  habilities = Hability.objects.all()
  context = { "universities": universities, "languages": languages, "habilities": habilities }
  return render(request, "home.html", context = context)

def list_tasks(request):
  tasks = Task.objects.all()
  form = TaskForm()
  context = { "tasks": tasks, "form": form }
  return render(request, "list_tasks.html", context=context)

def task_create(request):
    if request.method == 'POST':
      form = TaskForm(request.POST)
      if form.is_valid():
          form.save()

          return redirect('/')

def list_universities(request):
  universities = University.objects.all()
  form = UniversityForm()
  context = { "universities": universities, "form": form }
  return render(request, "list_universities.html", context=context)

def university_create(request):
    if request.method == 'POST':
      form = UniversityForm(request.POST)
      if form.is_valid():
          form.save()

          return redirect('/')

def list_languages(request):
  languages = Language.objects.all()
  form = LanguageForm()
  context = { "languages": languages, "form": form }
  return render(request, "list_languages.html", context=context)

def language_create(request):
    if request.method == 'POST':
      form = LanguageForm(request.POST)
      if form.is_valid():
          form.save()

          return redirect('/')

def list_habilities(request):
  habilities = Hability.objects.all()
  form = HabilityForm()
  context = { "habilities": habilities, "form": form }
  return render(request, "list_habilities.html", context=context)

def hability_create(request):
    if request.method == 'POST':
      form = HabilityForm(request.POST)
      if form.is_valid():
          form.save()

          return redirect('/')

def update(request, element_id, list_key):
    model = get_model(list_key)
    instance = model.objects.get(id=element_id)
    if request.method == "POST":
        form = get_form(request, list_key, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = get_form(request, list_key, instance=instance)
    return render(request, "update.html", context={"form": form})



def delete(request, element_id, list_key):
    model = get_model(list_key) # 
    instance = model.objects.get(id=element_id)
    if request.method == "POST":
      if "confirm" in request.POST:
        print(instance)
        instance.delete()
      return redirect("/")
        
    return render(request, "delete.html", context={"instance": instance})

def get_model(list_key):
    models = {
      'tasks': Task,
      'universities': University,
      'languages': Language,
      'habilities': Hability
    }
    return models.get(list_key) 
  
def get_form(request, list_key, instance=None):
    forms = {
      'tasks': TaskForm,
      'universities': UniversityForm,
      'languages': LanguageForm,
      'habilities': HabilityForm
    }
    Form = forms.get(list_key)
    return Form(request.POST or None, instance=instance)

