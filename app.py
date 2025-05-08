from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from psycopg2 import sql
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database configuration
DB_CONFIG = {
    'dbname': 'task_management',
    'user': 'postgres',
    'password': '12345678',
    'host': 'localhost',
    'port': '5432'
}

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE status != %s ORDER BY created_at DESC', ('Архив',))
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('tasks.html', tasks=tasks)

@app.route('/archive')
def archive():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE status = %s ORDER BY created_at DESC', ('Архив',))
    archived_tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('tasks.html', tasks=archived_tasks, is_archive=True)

@app.route('/task/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        result = request.form['result']
        status = request.form['status']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tasks (name, description, result, status) VALUES (%s, %s, %s, %s)',
            (name, description, result, status)
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash('Task created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('create_task.html')

@app.route('/task/<int:task_id>')
def view_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
    task = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if task is None:
        flash('Task not found!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('view_task.html', task=task)

@app.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        result = request.form['result']
        status = request.form['status']
        
        cursor.execute(
            'UPDATE tasks SET name = %s, description = %s, result = %s, status = %s WHERE id = %s',
            (name, description, result, status, task_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('view_task', task_id=task_id))
    
    cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
    task = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if task is None:
        flash('Task not found!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('edit_task.html', task=task)

@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/archive', methods=['POST'])
def archive_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = %s WHERE id = %s', ('Архив', task_id))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Task archived successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)