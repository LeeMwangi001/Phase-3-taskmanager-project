from taskmanager.database import init_db
from taskmanager.cli import main

if __name__ == "__main__":
    init_db() 
    main()
