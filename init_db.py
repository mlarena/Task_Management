import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_NAME = "task_management"
DB_USER = "postgres"
DB_PASSWORD = "12345678"
DB_HOST = "localhost"
DB_PORT = "5432"

def init_database():
    try:
        # Connect to PostgreSQL (without specifying a database)
        conn = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Create database if not exists
        cursor.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [DB_NAME])
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
            print(f"Database '{DB_NAME}' created successfully.")
        
        # Connect to the new database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        
        # Create tasks table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT,
                result TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status VARCHAR(50) NOT NULL CHECK (status IN ('Новая', 'В работе', 'Готово', 'Архив', 'Тест'))
            )
        """)
        print("Table 'tasks' created successfully.")
        
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    init_database()