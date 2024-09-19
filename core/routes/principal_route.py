from flask import Blueprint, request, jsonify
from core.services.principal_service import (
    get_teachers,
    get_assignments,
    grade_assignment
)

principal_bp = Blueprint('principal', __name__)

@principal_bp.route('/principal/assignments', methods=['GET'])
def list_assignments():
    assignments = get_assignments()
    return jsonify({'data': assignments}), 200

@principal_bp.route('/principal/teachers', methods=['GET'])
def list_teachers():
    teachers = get_teachers()
    return jsonify({'data': teachers}), 200

@principal_bp.route('/principal/assignments/grade', methods=['POST'])
def grade_assignment():
    data = request.get_json()
    assignment_id = data.get('id')
    grade = data.get('grade')
    result = grade_assignment(assignment_id, grade)
    return jsonify({'data': result}), 200
