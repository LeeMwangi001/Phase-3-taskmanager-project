from taskmanager.database import create_tables
from taskmanager.cli import main

if __name__ == "__main__":
    create_tables()
    main()
