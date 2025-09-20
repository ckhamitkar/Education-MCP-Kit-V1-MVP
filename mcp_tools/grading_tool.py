from mcp_tools.logging_tool import log_action

def grade_short_answer(user: str, answer: str, rubric: dict):
    """Grades a short answer based on a rubric."""
    log_action(user, 'grade_short_answer', {'rubric': rubric})

    score = 0
    explanation = []

    for criterion, details in rubric.items():
        if details['keyword'].lower() in answer.lower():
            score += details['points']
            explanation.append(f"Gained {details['points']} points for mentioning '{details['keyword']}'.")
        else:
            explanation.append(f"Missed points for not mentioning '{details['keyword']}'.")

    return {
        'score': score,
        'explanation': " ".join(explanation)
    }
