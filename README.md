# KnowledgeTracker

A mini web application for searching Altmetric’s API.

## Running the app

0. Make sure you have `git`, `python3` (3.6.6 or earlier), `pip` and `virtualenv` already installed.
1. Clone the repository locally:
  ```
  git clone https://github.com/sssoz/altmetric-test.git
  cd altmetric-test
  ```  
2. Create a virtualenv and activate it.
  ```
  virtualenv env
  . env/bin/activate
  ```
3. Install the requirements:
  ```
  pip install -r requirements.txt
  ```
4. Run the migrations:
  ```
  cd knowledgetracker
  python manage.py migrate
  ```
5. Run the development server:
  ```
  python manage.py runserver
  ```
6. The app will be available at `127.0.0.1:8000`.


## Todo

- [ ] Pagination: either use infinite scroll or display page navigation widget
- [ ] Use SASS as CSS pre-processor and minify CSS output
- [ ] Declare SASS variables for colour palette and typography
- [ ] Break up and organise CSS into separate files
- [ ] Add an option to sort by: _Total Altmetric score_, _Altmetric score in the last X timeframe_, and _Publication date_
- [x] Test and improve a11y
- [ ] Test and improve performance, speed, & [Progressive Web App features](https://developers.google.com/web/progressive-web-apps/checklist)
