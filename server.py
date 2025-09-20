from flask import Flask, request, jsonify
from mcp_tools import classroom_tool, quizgen_tool, grading_tool

app = Flask(__name__)

# A dummy user for now
DUMMY_USER = "teacher_jane"

@app.route('/assignments', methods=['GET'])
def get_assignments():
    assignments = classroom_tool.get_assignments(DUMMY_USER)
    return jsonify(assignments)

@app.route('/students', methods=['GET'])
def get_students():
    course_id = request.args.get('course_id', 'default_course')
    students = classroom_tool.get_students(DUMMY_USER, course_id)
    return jsonify(students)

@app.route('/grade', methods=['POST'])
def post_grade():
    data = request.json
    assignment_id = data.get('assignment_id')
    student_id = data.get('student_id')
    grade = data.get('grade')
    comment = data.get('comment')

    if not all([assignment_id, student_id, grade is not None, comment]):
        return jsonify({"error": "Missing required fields"}), 400

    result = classroom_tool.post_grade(DUMMY_USER, assignment_id, student_id, grade, comment)
    return jsonify(result)

@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    data = request.json
    text = data.get('text')
    num_questions = data.get('num_questions', 5)

    if not text:
        return jsonify({"error": "Text field is required"}), 400

    quiz = quizgen_tool.generate_quiz(DUMMY_USER, text, num_questions)
    return jsonify(quiz)

@app.route('/grade_answer', methods=['POST'])
def grade_answer():
    data = request.json
    answer = data.get('answer')
    rubric = data.get('rubric')

    if not all([answer, rubric]):
        return jsonify({"error": "Missing required fields"}), 400

    result = grading_tool.grade_short_answer(DUMMY_USER, answer, rubric)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
