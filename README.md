# Indoor Positioning System Backend

## Setting up the environment

Create a python virtual environment using virtualenv. Recommended python version is stated in runtime.txt which is python 3.6. (This step is optional because we have included a virtual environment in the repository)

```
# On MacOS and Linux
python3 -m venv venv

# On Windows
python -m venv venv
```

Activate the environment.

```
# On MacOS and Linux
source venv/bin/activate

# On Windows
.\venv\Scripts\activate
```

Extra note for Windows users: The embedded virtual environment is created under Linux environment. Therefore, the environment should be activated using the following command.

```
.\venv\bin\activate
```

Confirm that the Python interpreter is now pointed in the correct location.

```
# On MacOS and Linux
which python

# On Windows command prompt
where python

# On Windows Powershell
(Get-Command python).path
```

Install the dependencies.

```
python -m pip install -r requirements.txt
```

## Running locally

Migrate the database.

```
python manage.py migrate
```

Run the Django application.

```
python manage.py runserver
```

## Running on Heroku server

Install Heroku CLI tool.
Create a Heroku project.

```
heroku create ips-backend
```

Setting a git remote to the Heroku project.

```
heroku git:remote -a ips-backend
```

A Procfile has already been created under the repository, containing the command to run after deployed to Heroku.
Deploy the code by pushing the code using git.

```
git push heroku master
```

Migrate the database on Heroku server.

```
heroku run python manage.py migrate
```


