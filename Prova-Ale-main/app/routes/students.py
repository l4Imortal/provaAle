from flask import Blueprint, request, jsonify
from app.models import db, Student

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['POST'])
def create_student():
    data = request.json
    student = Student(**data)
    db.session.add(student)
    db.session.commit()
    return jsonify(id=student.id), 201
