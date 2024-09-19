from flask import Blueprint, request, jsonify
from core.services.teacher_service import (
    list_assignments,
    grade_assignment
)

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teacher/assignments', methods=['GET'])
def get_assignments():
    teacher_id = request.headers.get('teacher_id')
    assignments = list_assignments(teacher_id)
    return jsonify({'data': assignments}), 200

@teacher_bp.route('/teacher/assignments/grade', methods=['POST'])
def grade_assignment():
    data = request.get_json()
    teacher_id = request.headers.get('teacher_id')
    assignment_id = data.get('id')
    grade = data.get('grade')
    result = grade_assignment(assignment_id, grade, teacher_id)
    return jsonify({'data': result}), 200
