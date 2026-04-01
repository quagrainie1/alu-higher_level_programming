# Python - Object-relational mapping

This project links Python with MySQL databases using two approaches:
MySQLdb for raw SQL queries and SQLAlchemy as an Object Relational Mapper (ORM).

## Requirements
- Python 3.8.5
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- MySQL 8.0

## Files

| File | Description |
|------|-------------|
| 0-select_states.py | Lists all states from the database |
| 1-filter_states.py | Lists states starting with N |
| 2-my_filter_states.py | Lists states matching user input |
| 3-my_safe_filter_states.py | SQL injection safe state filter |
| 4-cities_by_state.py | Lists all cities with their state |
| 5-filter_cities.py | Lists cities of a given state |
| model_state.py | State class mapped to MySQL table |
| model_city.py | City class mapped to MySQL table |
| 7-model_state_fetch_all.py | Lists all State objects via SQLAlchemy |
| 8-model_state_fetch_first.py | Prints first State object |
| 9-model_state_filter_a.py | Lists States containing letter a |
| 10-model_state_my_get.py | Gets State by name |
| 11-model_state_insert.py | Adds new State object |
| 12-model_state_update_id_2.py | Updates State where id=2 |
| 13-model_state_delete_a.py | Deletes States containing letter a |
| 14-model_city_fetch_by_state.py | Lists all City objects by state |
