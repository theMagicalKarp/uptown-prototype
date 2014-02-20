import logging
import random
import json

from flask import Blueprint
from flask import render_template
from flask import request

from app.models import student

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

