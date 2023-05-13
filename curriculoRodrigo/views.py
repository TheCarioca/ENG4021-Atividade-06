from django.shortcuts import render, redirect
from .models import Task, University, Language, Hability
from .forms import TaskForm, UniversityForm, LanguageForm, HabilityForm, LoginForm, RegisterForm
from django.contrib.auth import login, authenticate

# Define as views da aplicação.
# A partir dessas views, o Django gerará as páginas da aplicação.

# View da página inicial.
def home(request):
  # Seleciona todas as universidades, linguagens e habilidades
  # e as passa como contexto para serem usadas no template "home.html".
  universities = University.objects.all()
  languages = Language.objects.all()
  habilities = Hability.objects.all()
  context = { "universities": universities, "languages": languages, "habilities": habilities }
  
  # Renderiza a página "home.html" com o contexto passado.
  return render(request, "home.html", context=context)

# View da página que lista todas as tarefas.
def list_tasks(request):
  # Seleciona todas as tarefas.
  tasks = Task.objects.all()
  
  # Cria um objeto do formulário de tarefas.
  form = TaskForm()
  
  # Passa as tarefas e o formulário como contexto para a página "list_tasks.html".
  context = { "tasks": tasks, "form": form }
  
  # Renderiza a página "list_tasks.html" com o contexto passado.
  return render(request, "list_tasks.html", context=context)

# View que cria uma nova tarefa.
def task_create(request):
  # Verifica se o método da requisição é POST.
  if request.method == 'POST':
    # Cria um objeto do formulário de tarefas e passa os dados recebidos pela requisição.
    form = TaskForm(request.POST)
    
    # Verifica se o formulário é válido.
    if form.is_valid():
      # Salva a nova tarefa.
      form.save()

      # Redireciona o usuário para a página inicial.
      return redirect('/')
    
# View da página que lista todas as universidades.
def list_universities(request):
  # Seleciona todas as universidades.
  universities = University.objects.all()
  
  # Cria um objeto do formulário de universidades.
  form = UniversityForm()
  
  # Passa as universidades e o formulário como contexto para a página "list_universities.html".
  context = { "universities": universities, "form": form }
  
  # Renderiza a página "list_universities.html" com o contexto passado.
  return render(request, "list_universities.html", context=context)

# View que cria uma nova universidade.
def university_create(request):
  # Verifica se o método da requisição é POST.
  if request.method == 'POST':
    # Cria um objeto do formulário de universidades e passa os dados recebidos pela requisição.
    form = UniversityForm(request.POST)
    
    # Verifica se o formulário é válido.
    if form.is_valid():
      # Salva a nova universidade.
      form.save()

      # Redireciona o usuário para a página inicial.
      return redirect('/')

def list_languages(request):
  # Recupera todas as instâncias de Language do banco de dados
  languages = Language.objects.all()
  # Cria uma instância de LanguageForm vazia
  form = LanguageForm()
  # Define um dicionário que será enviado para o template list_languages.html
  context = { "languages": languages, "form": form }
  # Renderiza o template list_languages.html com o dicionário definido acima
  return render(request, "list_languages.html", context=context)

def language_create(request):
    # Verifica se a requisição é do tipo POST
    if request.method == 'POST':
      # Cria uma instância de LanguageForm com os dados da requisição POST
      form = LanguageForm(request.POST)
      # Verifica se os dados do form são válidos
      if form.is_valid():
          # Salva os dados do form no banco de dados
          form.save()
          # Redireciona para a página inicial
          return redirect('/')

def list_habilities(request):
  # Recupera todas as instâncias de Hability do banco de dados
  habilities = Hability.objects.all()
  # Cria uma instância de HabilityForm vazia
  form = HabilityForm()
  # Define um dicionário que será enviado para o template list_habilities.html
  context = { "habilities": habilities, "form": form }
  # Renderiza o template list_habilities.html com o dicionário definido acima
  return render(request, "list_habilities.html", context=context)

def hability_create(request):
    # Verifica se a requisição é do tipo POST
    if request.method == 'POST':
      # Cria uma instância de HabilityForm com os dados da requisição POST
      form = HabilityForm(request.POST)
      # Verifica se os dados do form são válidos
      if form.is_valid():
          # Salva os dados do form no banco de dados
          form.save()
          # Redireciona para a página inicial
          return redirect('/')

def update(request, element_id, list_key):
    # Recupera o modelo (Task, University, Language, Hability) correspondente à chave list_key
    model = get_model(list_key)
    # Recupera a instância do modelo com o id element_id
    instance = model.objects.get(id=element_id)
    if request.method == "POST":
        # Cria uma instância do formulário correspondente a list_key com os dados da requisição POST
        form = get_form(request, list_key, instance=instance)
        # Verifica se os dados do form são válidos
        if form.is_valid():
            # Salva os dados do form no banco de dados
            form.save()
            # Redireciona para a página inicial
            return redirect("/")
    else:
        # Cria uma instância do formulário correspondente a list_key com os dados da instância
        form = get_form(request, list_key, instance=instance)
    # Renderiza o template update.html com o formulário criado acima
    return render(request, "update.html", context={"form": form})

# Definindo a view delete que recebe como parâmetros o request, o id do elemento e a chave da lista
def delete(request, element_id, list_key):
    # Obtendo o modelo correspondente à chave da lista
    model = get_model(list_key)
    
    # Obtendo a instância correspondente ao id do elemento
    instance = model.objects.get(id=element_id)
    
    # Verificando se o método HTTP utilizado é POST
    if request.method == "POST":
        # Verificando se o botão confirmar foi pressionado
        if "confirm" in request.POST:
            # Imprimindo a instância a ser deletada (somente para debug)
            print(instance)
            # Deletando a instância
            instance.delete()
        # Redirecionando o usuário para a página inicial
        return redirect("/")
    
    # Renderizando a página de confirmação de exclusão
    return render(request, "delete.html", context={"instance": instance})

# Definindo a função get_model que recebe como parâmetro a chave da lista
def get_model(list_key):
    # Criando um dicionário com as chaves de lista e os respectivos modelos
    models = {
      'tasks': Task,
      'universities': University,
      'languages': Language,
      'habilities': Hability
    }
    # Obtendo o modelo correspondente à chave da lista
    return models.get(list_key)

# Definindo a função get_form que recebe como parâmetros o request, a chave da lista e uma instância (opcional)
def get_form(request, list_key, instance=None):
    # Criando um dicionário com as chaves de lista e os respectivos formulários
    forms = {
      'tasks': TaskForm,
      'universities': UniversityForm,
      'languages': LanguageForm,
      'habilities': HabilityForm
    }
    # Obtendo o formulário correspondente à chave da lista
    Form = forms.get(list_key)
    # Instanciando o formulário com o POST request e a instância (caso exista)
    return Form(request.POST or None, instance=instance)

# Definindo a função sign_up que recebe um request
def sign_up(request):
    # Verificando se o método da requisição é GET
    if request.method == 'GET':
        # Instanciando um objeto RegisterForm
        form = RegisterForm()
        # Renderizando a página register.html e passando o objeto form como contexto
        return render(request, 'register.html', {'form': form})    
    
    # Verificando se o método da requisição é POST
    if request.method == 'POST':
        # Instanciando um objeto RegisterForm com os dados da requisição POST
        form = RegisterForm(request.POST) 
        # Verificando se o formulário é válido
        if form.is_valid():
            # Salvando o usuário no banco de dados sem commit
            user = form.save(commit=False)
            # Convertendo o username para lowercase
            user.username = user.username.lower()
            # Salvando o usuário no banco de dados
            user.save()
            # Fazendo o login do usuário na sessão
            login(request, user)
            # Redirecionando para a página principal
            return redirect('/')
        else:
            # Renderizando a página register.html novamente, passando o objeto form como contexto
            return render(request, 'register.html', {'form': form})
        
# Definindo a função sign_in que recebe um request
def sign_in(request):
    # Verificando se o método da requisição é GET
    if request.method == 'GET':
        # Instanciando um objeto LoginForm
        form = LoginForm()
        # Renderizando a página register.html e passando o objeto form como contexto
        return render(request, 'register.html', {'form': form})    
    
    # Verificando se o método da requisição é POST
    if request.method == 'POST':
        # Instanciando um objeto LoginForm com os dados da requisição POST
        form = LoginForm(request.POST)
        # Verificando se o formulário é válido
        if form.is_valid():
            # Obtendo o username e a senha do formulário
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Autenticando o usuário com o username e a senha fornecidos
            user = authenticate(request, username=username, password=password)
            # Verificando se o usuário existe
            if user is not None:
                # Fazendo o login do usuário na sessão
                login(request, user)
                # Redirecionando para a página principal
                return redirect('/')
            else:
                # Adicionando um erro ao formulário
                form.add_error(None, 'Invalid username or password.')
        else:
            # Adicionando um erro ao formulário
            form.add_error(None, 'Invalid username or password.')
        # Renderizando a página login.html novamente, passando o objeto form como contexto
        return render(request, 'login.html', {'form': form})


