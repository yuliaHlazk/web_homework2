# web_homework2
Where to go project
to run project:
git clone 
cd project_name
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Endpoints
/ - main page
place/ - all places
add/ - add a new place
getplace/? - get one random place based on largest ratings (weighted)
details/?name=(name of the place) - show more detailed information about a specific place

