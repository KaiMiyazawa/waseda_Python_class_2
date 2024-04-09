from bottle import Bottle, run, template, request, redirect, static_file
import sqlite3

# SQLite3データベースの初期化
conn = sqlite3.connect('todo.db', check_same_thread=False, isolation_level=None)
cursor = conn.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS tasks (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title TEXT NOT NULL,
		description TEXT,
		status INTEGER DEFAULT 0
	)
''')
conn.commit()

# Bottleアプリケーションの初期化
app = Bottle()
app.config['autojson'] = False
app.config['charset'] = 'utf-8'

# 未完了タスク一覧画面
@app.route('/')
def index():
	conn = sqlite3.connect('todo.db', check_same_thread=False, isolation_level=None)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM tasks WHERE status = 0')
	tasks = cursor.fetchall()
	conn.close()
	return template('index', tasks=tasks)

# 完了タスク一覧画面
@app.route('/completed')
def completed():
	conn = sqlite3.connect('todo.db', check_same_thread=False, isolation_level=None)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM tasks WHERE status = 1')
	tasks = cursor.fetchall()
	conn.close()
	return template('completed', tasks=tasks)

# タスク詳細画面
@app.route('/task/<task_id>')
def task_detail(task_id):
	conn = sqlite3.connect('todo.db', check_same_thread=False, isolation_level=None)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
	task = cursor.fetchone()
	conn.close()
	return template('detail', task=task)

# タスクの追加
@app.route('/add_task', method='POST')
def add_task():
	title = request.forms.getunicode('title')
	description = request.forms.getunicode('description')
	conn = sqlite3.connect('todo.db', check_same_thread=False, isolation_level=None)
	cursor = conn.cursor()
	cursor.execute('INSERT INTO tasks (title, description, status) VALUES (?, ?, 0)', (title, description))
	conn.commit()
	conn.close()
	redirect('/')

@app.route('/add')
def add():
	return template('add')

# タスクの編集
@app.route('/edit/<task_id>', method='POST')
def edit_task(task_id):
	title = request.forms.getunicode('title')
	description = request.forms.getunicode('description')
	conn = sqlite3.connect('todo.db', check_same_thread=False, isolation_level=None)
	cursor = conn.cursor()
	cursor.execute('UPDATE tasks SET title=?, description=? WHERE id=?', (title, description, task_id))
	conn.commit()
	conn.close()
	redirect('/')

# タスクの完了／未完了の切り替え
@app.route('/toggle/<task_id>')
def toggle_status(task_id):
	conn = sqlite3.connect('todo.db', check_same_thread=False, isolation_level=None)
	cursor = conn.cursor()
	cursor.execute('UPDATE tasks SET status = 1 - status WHERE id = ?', (task_id,))
	conn.commit()
	conn.close()
	redirect('/')

# タスクの削除
@app.route('/delete/<task_id>')
def delete_task(task_id):
	conn = sqlite3.connect('todo.db', check_same_thread=False, isolation_level=None)
	cursor = conn.cursor()
	cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
	conn.commit()
	conn.close()
	redirect('/')

# 静的ファイルのルーティング
@app.route('/static/<filename>')
def static_files(filename):
	return static_file(filename, root='./static')

if __name__ == '__main__':
	run(app, debug=True)
