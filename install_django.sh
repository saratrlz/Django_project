python3 -m venv .venv     #Create a new .venv
source .venv/bin/activate #Get inside the .venv to download correct packages

pip install django        #Download django in the .venv
python3 -m django startproject mysite app   #Check long comment

:'
Use Python 3 to run Django and create a new Django project named mysite inside the app directory.
    python3        # Run the Python 3 interpreter
    -m django      # Use Python to run the Django module
    startproject   # Django management command to create a new project
    mysite         # Name of the Django project (Python package)
    app            # Directory where the project will be created
'
#ADD PACKAGES VIA THE DOCKER
#docker compose run web python app/manage.py startapp webapp