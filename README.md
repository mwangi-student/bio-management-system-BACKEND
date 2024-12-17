## set-up migrations

- to set up migrations, run `alembic init migrations` . only run this command once.
- Modify alembic.ini file and set the `sqlalchemy url = sqlite:///school.db`. Choose your database name, mine is school.db, what's yours?
- Modify the `env.py` file in the migrations folder and import the Base class from models file and update the target_metadata.
- To create a migration run, `alembic revision --autogenerate -m "message"`.
- To apply the generated migration, run `alembic upgrade head`.
