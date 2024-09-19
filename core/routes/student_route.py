from flask import Blueprint, request, jsonify
from core.services.student_service import (
    list_assignments,
    create_assignment,
    edit_assignment,
    submit_assignment
)

student_bp = Blueprint('student', __name__)

@student_bp.route('/student/assignments', methods=['GET'])
def get_assignments():
    student_id = request.headers.get('student_id')
    assignments = list_assignments(student_id)
    return jsonify({'data': assignments}), 200

@student_bp.route('/student/assignments', methods=['POST'])
def post_assignment():
    data = request.get_json()
    student_id = request.headers.get('student_id')
    content = data.get('content')
    assignment_id = data.get('id')
    if assignment_id:
        assignment = edit_assignment(assignment_id, content, student_id)
    else:
        assignment = create_assignment(content, student_id)
    return jsonify({'data': assignment}), 200

@student_bp.route('/student/assignments/submit', methods=['POST'])
def submit_assignment():
    data = request.get_json()
    student_id = request.headers.get('student_id')
    assignment_id = data.get('id')
    teacher_id = data.get('teacher_id')
    result = submit_assignment(assignment_id, teacher_id, student_id)
    return jsonify({'data': result}), 200
