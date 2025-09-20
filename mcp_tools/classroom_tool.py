from mcp_tools.logging_tool import log_action

def get_assignments(user: str):
    """Fetches a list of assignments from Google Classroom."""
    log_action(user, 'get_assignments', {'status': 'success'})
    return [
        {'id': '1', 'title': 'History Homework', 'deadline': '2025-10-01'},
        {'id': '2', 'title': 'Math Quiz', 'deadline': '2025-10-03'},
    ]

def get_students(user: str, course_id: str):
    """Fetches a list of students for a course."""
    log_action(user, 'get_students', {'course_id': course_id, 'status': 'success'})
    return [
        {'id': '101', 'name': 'Alice'},
        {'id': '102', 'name': 'Bob'},
    ]

def post_grade(user: str, assignment_id: str, student_id: str, grade: float, comment: str):
    """Posts a grade for a student's assignment."""
    log_action(user, 'post_grade', {'assignment_id': assignment_id, 'student_id': student_id, 'grade': grade, 'comment': comment, 'status': 'success'})
    return {'status': 'success', 'message': f'Grade for student {student_id} on assignment {assignment_id} posted.'}
