from taskmanager.cli import main
from taskmanager.database import init_db

if __name__ == "__main__":
    init_db()  # Initialize the database and create tables
    main()
