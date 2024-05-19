# AirBnB Clone - Web Framework

This project is part of the AirBnB clone series, focusing on the web framework aspect

## Description

The Web Framework project uses Flask, a Python web framework, to serve dynamic content for the AirBnB clone application. It integrates with the existing storage system (file or database) and provides routes and templates for displaying data in HTML pages.

## Files

The project contains the following files:

- `web_flask/`: The main directory for the Flask application.
  - `__init__.py`: Initializes the Flask application.
  - `0-hello_route.py`: Defines a route for displaying "Hello HBNB!".
  - `1-hbnb_route.py`: Defines a route for displaying "HBNB".
  - `2-c_route.py`: Defines a route for displaying "C " followed by a text value.
  - `3-python_route.py`: Defines routes for displaying "Python " followed by a text value.
  - `4-number_route.py`: Defines a route for displaying a number.
  - `5-number_template.py`: Defines a route for rendering an HTML template with a number.
  - `6-number_odd_or_even.py`: Defines a route for rendering an HTML template with a number and indicating if it's odd or even.
  - `7-states_list.py`: Defines a route for rendering an HTML template with a list of states.
  - `8-cities_by_states.py`: Defines a route for rendering an HTML template with a list of states and their cities.
  - `9-states.py`: Defines routes for rendering an HTML template with a list of states or a specific state and its cities.
  - `10-hbnb_filters.py`: Defines a route for rendering an HTML page with filters for states and amenities.
  - `100-hbnb.py`: Defines a route for rendering an HTML page with data for states, amenities, and places.
  - `templates/`: Contains HTML templates used by the Flask application.
    - `5-number.html`: Template for displaying a number.
    - `6-number_odd_or_even.html`: Template for displaying a number and indicating if it's odd or even.
    - `7-states_list.html`: Template for displaying a list of states.
    - `8-cities_by_states.html`: Template for displaying a list of states and their cities.
    - `9-states.html`: Template for displaying a list of states or a specific state and its cities.
    - `10-hbnb_filters.html`: Template for displaying filters for states and amenities.
    - `100-hbnb.html`: Template for displaying data for states, amenities, and places.
  - `static/`: Contains static files (CSS, images) used by the HTML templates.
    - `styles/`: Contains CSS files.
    - `images/`: Contains image files.

- `models/`: Contains the models used by the application.
  - `engine/`: Contains the storage engines.
    - `file_storage.py`: Defines the `FileStorage` class for storing data in a JSON file.
    - `db_storage.py`: Defines the `DBStorage` class for storing data in a MySQL database.
  - `state.py`: Defines the `State` model and a getter method for retrieving cities.
  - `city.py`: Defines the `City` model.
  - `amenity.py`: Defines the `Amenity` model.
  - `place.py`: Defines the `Place` model.

## Requirements

- Python 3.4.3
- Flask 1.0.2
- SQLAlchemy 1.3.10
- MySQL 5.7
