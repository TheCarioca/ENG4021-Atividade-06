# Etapas para o projeto de ENG4021 de Django

## 1. Definindo secret key:

Abra a aba "shell" e digite as seguintes linhas de comando:

```
python
import secrets
secrets.token_urlsafe(32)
```

Em seguida, o codígo irá retornar um token. Selecione o texto e copie usando o botão direito do mouse (O CTRL+C não funciona). Depois se dirija a pagína de "Secrets" e adicione uma nova chave com título "SECRET_KEY" com seu valor sendo o token copiado. E pronto para essa etapa!

## 2. Criando o app:

No shell também iremos criar o app. Rode o seguinte comando:

```
python3 manage.py startapp <nomeDoApp>
```

(Substitua o <nomeDoApp> com o nome da aplicação, no meu caso curriculoRodrigo)

## 3. Iniciando a database:

Para a gente criar aquela pasta "migrations" e propriamente conseguir usar a database. Realize esses comandos:

```
python manage.py makemigrations
python manage.py migrate
```

## 4. Criando o acesso para o /admin:

Para acessar o /admin e conseguir fazer as alterações manuais na database, você precisa criar um superusuário. Realize os seguintes comandos:

```
python manage.py createsuperuser
```

Ele irá pedir o nome de usuario e você precisará digita-lo. No meu caso defini como padrão "admin":

```
Username (leave blank to use 'runner'):
admin
```

Ele irá pedir o nome de usuario e você precisará digita-lo. No meu caso defini como padrão "admin":

```
Username (leave blank to use 'runner'):
admin
```

Depois pedirá o email:

```
Email address:
<seuEmail@email.com>
```

Por fim, pedirá uma senha e depois repeti-la:

```
Password:
<suaSenha>
Password (again):
<suaSenha>
```
