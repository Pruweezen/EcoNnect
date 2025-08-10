from flask import Blueprint, render_template, request
from app.models import Job
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'static')
jobseeker_bp = Blueprint(
    'jobseeker',
    __name__,
    template_folder=template_dir,
    static_folder=static_dir,
    static_url_path='/jobseeker/static'
)

@jobseeker_bp.route('/jobseeker', methods=['GET', 'POST'])
def jobseeker():
    jobs = []
    if request.method == 'POST':
        location = request.form.get('location')
        # Replace with the actual query logic 
        jobs = Job.query.filter_by(location=location).all()
    return render_template('jobseeker.html', jobs=jobs)