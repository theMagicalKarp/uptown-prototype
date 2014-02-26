import logging
import random
import json

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from app.models import student
from app.models import user

blueprint = Blueprint('views', __name__)


@blueprint.route('/', methods=['GET'])
def home():
    # chooses a random youtube link to display on the home page!
    youtube_links = [
        'NNXQAp0m5nA',
        'EDXMrLoME8U',
        'XeDM1ZjMK50',
        'blpe_sGnnP4',
        'ECceiU32vGs',
        'KJRRCbrVQp4',
        'UBQP9gEldRk',
        'UhHhXukovMU',
        't_jEm6FnaPM',
        'hhP8Da1qTs8',
        'A_aJBAzw_ls',
        '7QLSRMoKKS0',
        'KhrJI2zbE04',
        '4txVqr1eNwc'
    ]
    return render_template('home.html', youtube_link=random.choice(youtube_links))


@blueprint.route('/bootstrap', methods=['GET'])
def bootstrap():
    return render_template('bootstrap_examples.html')


@blueprint.route('/model_example', methods=['GET'])
def model_example():
    all_students = student.fetch_students()
    return render_template('modeling.html', students=all_students)


@blueprint.route('/chart_demo', methods=['GET'])
def chart_demo():
    return render_template('chart.html')


@blueprint.route('/post_student', methods=['POST'])
def post_student():
    student_data = json.loads(request.data)
    student.create_student(student_data['name'], student_data['age'])
    return 'success!', 200


@blueprint.route('/student_graph_data', methods=['GET'])
def get_graph_data():
    students = student.fetch_students()

    age_distribution = {}
    for s in students:
        age_distribution[s.age] = age_distribution.get(s.age, 0) + 1

    return json.dumps({
        'age_distribution': age_distribution
    })


@blueprint.route('/auth/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('views.home'), code=302)

    if request.method == 'POST':
        login_form = request.form
        user.login(login_form.get('email'), login_form.get('password'))

        if current_user.is_authenticated():
            next_url = request.args.get('next',url_for('views.home'))
            return redirect(next_url, code=302)
        else:
            return render_template('login.html', failure=True, email=login_form.get('email'))

    return render_template('login.html', failure=False, email='')


@blueprint.route('/auth/logout', methods=['GET'])
def logout():
    user.logout()
    return redirect(url_for('views.home'), code=302)


@blueprint.route('/auth/register/<registration_id>', methods=['GET', 'POST'])
def register(registration_id):
    new_user = user.get_by_registration_id(registration_id)
    if not new_user or new_user.is_registered:
        return redirect(url_for('views.home'), code=302)

    if request.method == 'POST':
        registration_form = request.form
        new_password = registration_form.get('password', '')
        if len(new_password) < 6:
            return render_template('register.html', attempt={'failure':True}, user=new_user)

        user.register(registration_id, new_password)
        return redirect(url_for('views.home'), code=302)

    return render_template('register.html', attempt={}, user=new_user)


@blueprint.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if not current_user.is_admin():
        return redirect(url_for('views.home'), code=302)

    if request.method == 'POST':
        admin_form = request.form
        user_role = user.ADMIN_ROLE if 'is-admin' in admin_form else user.BASE_USER_ROLE

        new_user = user.create_user(admin_form.get('email'), user_role)
        registration_url = url_for('views.register', registration_id=new_user.registration_id)

        return render_template('admin.html', new_user=new_user,
                                             registration_url=registration_url,
                                             users=user.get_users())

    return render_template('admin.html', new_user=None, users=user.get_users())

