from flask import Flask, render_template, redirect, url_for, request
from sprint import *

app = Flask(__name__)
app.config.from_object(__name__)


def init_db():
    db.connect()
    db.create_tables([Sprint], safe=True)
    db.close()


@app.route('/new_sprint', methods=['GET', 'POST'])
def new_sprint():
    if request.method == 'POST':
        title = request.form['title']
        story = request.form['story']
        criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = request.form['status']
        Sprint.create(
            title=title,
            user_story=story,
            acceptance_criteria=criteria,
            business_value=business_value,
            estimation=estimation,
            status=status
        )
        return redirect(url_for('list'))
    else:
        return render_template('new_sprint.html', data=False)


@app.route('/list', methods=['get'])
def list():
    all_data = Sprint.select()
    return render_template('list.html', sprints=all_data)


@app.route('/delete', methods=['post'])
def delete_sprint():
    number = (request.form['sprint_id'])
    row_to_delete = Sprint.select().where(Sprint.sprint_id == number).get()
    row_to_delete.delete_instance()
    return redirect(url_for('list'))


@app.route('/new_sprint/<sprintname>', methods=['post'])
def update_sprint(sprintname):
    row = Sprint.select().where(Sprint.sprint_id == sprintname).get()
    return render_template('new_sprint.html', data=row)


@app.route('/update', methods=['post'])
def update():
    number = (request.form['sprint_id'])
    row_to_update = Sprint.select().where(Sprint.sprint_id == number).get()
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['acceptance_criteria']
    business_value = request.form['business_value']
    estimation = request.form['estimation']
    status = request.form['status']
    row_to_update.title = title
    row_to_update.user_story = story
    row_to_update.acceptance_criteria = criteria
    row_to_update.business_value = business_value
    row_to_update.estimation = estimation
    row_to_update.status = status
    row_to_update.save()
    return redirect(url_for('list'))

if '__main__' == __name__:
    init_db()
    app.run(debug=True)
