# Refresher

A really impactful way to deal with stress related to _work-life balance_ is to **hear about the same from thousands of people...**

## Want to contribute/Improve it? :mag:

Its super easy to get started! Just follow the steps below :smiley:

- _Clone the repo_ by `git clone https://github.com/Rishabh570/refresher.git`

- _Head over to project folder_ in your local machine.

- _Create and Activate a virtualenv_ by `virtualenv {env_name_of_your_choice}`

- _Install all the requirements_ by `pip install -r requirements.txt`

- Do `python manage.py migrate` and finally `python manage.py runserver`..

**and you're good to go** :tada:

## Accessing API :book:

- **/api/people/** - _returns a list of people posted._
- **/api/people/{first_name}** - _returns posts posted by that particular person._
- **/api/people-delete/{target}** - _deletes the target post._
- **/api/create/** - _creates a post right from API_ :smiley:


### TODO :pushpin:

- [ ] Add Celery
- [x] Add Caching
- [ ] Work on front-end (React.js)
- [ ] Add Google Analytics