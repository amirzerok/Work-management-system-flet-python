# ماژول‌های مورد نیاز از کتابخانه Flask را ایمپورت می‌کنیم:
from flask import Flask, render_template, request, redirect, url_for

# یک نمونه از برنامه Flask با نام app ایجاد می‌کنیم:
app = Flask(__name__)

# یک لیست خالی برای ذخیره‌سازی وظایف ایجاد می‌کنیم:
tasks = []

# مسیر ریشه ('/') را به تابع index مرتبط می‌کنیم:
@app.route('/')
def index():
   # قالب index.html را رندر کرده و لیست وظایف را به آن پاس می‌دهیم:
   return render_template('index.html', tasks=tasks)

# مسیر '/add' را برای اضافه کردن وظیفه جدید تعریف می‌کنیم:
@app.route('/add', methods=['POST'])
def add():
   # وظیفه جدید را از فرم دریافت می‌کنیم:
   task = request.form.get('task')
   # اگر وظیفه وارد شده معتبر است:
   if task:
       # آن را به لیست وظایف اضافه می‌کنیم:
       tasks.append(task)
   # کاربر را به صفحه اصلی بازمی‌گردانیم:
   return redirect(url_for('index'))

# مسیر '/delete/<int:task_id>' را برای حذف وظیفه تعریف می‌کنیم:
@app.route('/delete/<int:task_id>')
def delete(task_id):
   # اگر شناسه وظیفه معتبر است:
   if 0 <= task_id < len(tasks):
       # وظیفه مورد نظر را از لیست حذف می‌کنیم:
       del tasks[task_id]
   # کاربر را به صفحه اصلی بازمی‌گردانیم:
   return redirect(url_for('index'))

# اگر این فایل به عنوان فایل اصلی اجرا شده است:
if __name__ == '__main__':
   # برنامه را با حالت دیباگ اجرا می‌کنیم:
   app.run(debug=True)
