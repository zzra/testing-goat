# HOW TO
1. Run functional tests `python manage.py test functional_tests`
2. Run unit tests `python manage.py test lists`
3. Run server `python manage.py runserver`
4. Make migrations `python manage.py makemigrations`
5. Run docker for test
```
docker build -t superlists . && docker run -p 8888:8888 \
--mount type=bind,source=./src/db.sqlite3,target=/src/db.sqlite3 \
-it superlists &
```
6. Run docker for production
```
docker build -t superlists . && docker run -p 8888:80 \
--mount type=bind,source=./src/db.sqlite3,target=/src/db.sqlite3 \
-e DJANGO_SECRET_KEY=sekrit \
-e DJANGO_ALLOWED_HOSTS=localhost \
-it superlists &
```
7. Remove all old docker images `docker system prune -f`
8. Run ansible playbook `ansible-playbook --user=peter -i 164.92.125.221, infra/ansible-provision.yaml -vv --ask-become-pass`

Git Location - `https://github.com/hjwp/book-example`

## POSITION
11, getting our image onto the server, and setting up dns

## TO DO
* ~~don't save blank items for every request~~
* ~~code smell: post test is too long?~~
* ~~pass existing items to the template somehow~~
* ~~display multiple items in the table~~
* ~~cleaup after FT runs~~
* ~~adjust model so that items are assosciated with different lists~~
* ~~add unique urls for each list~~
* ~~add a url for creating a new list via POST~~
* ~~add urls for adding a new item to an existing list via POST~~
* ~~support more than one list!~~
* ~~refactor away duplication in urls.py~~
* review {% static %} template tag to get rid of hard coded urls
* review client-side packaging ie npm and bower
* review bootstrap and SASS