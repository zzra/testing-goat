# HOW TO
1. Run functional tests `python manage.py test functional_tests`
2. Run unit tests `python manage.py test lists`
3. Run server `python manage.py runserver`
4. Make migrations `python manage.py makemigrations`
5. Run docker 
```
docker build -t superlists . && docker run -p 8888:8888 \
--mount type=bind,source=./src/db.sqlite3,target=/src/db.sqlite3 \
-it superlists &
```

Git Location - `https://github.com/hjwp/book-example`

## POSITION
10.4, using env variables 

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