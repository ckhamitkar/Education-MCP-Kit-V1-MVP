# Education MCP Kit — V1 (MVP)

A toolkit of composable **education tools** — managing classroom data, generating quizzes, and grading short answers — exposed through a small Flask service. Built as an MVP for an MCP-style tool layer that an LLM agent (or any HTTP client) can call.

## What it does

Classroom workflows are packaged as discrete, individually testable tools:

- **Classroom tool** — list assignments, list students, post grades
- **Quiz-generation tool** — generate an *N*-question quiz from source text
- **Grading tool** — grade a short answer against a rubric
- **Logging tool** — shared activity logging

## API

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET  | `/assignments` | List assignments |
| GET  | `/students?course_id=...` | List students in a course |
| POST | `/grade` | Post a grade — `assignment_id`, `student_id`, `grade`, `comment` |
| POST | `/generate_quiz` | Generate a quiz — `text`, `num_questions` |
| POST | `/grade_answer` | Grade a short answer — `answer`, `rubric` |

## Run

```bash
pip install -r requirements.txt
python server.py            # serves on :8080
```

Or with Docker:

```bash
docker build -t education-mcp-kit .
docker run -p 8080:8080 education-mcp-kit
```

## Tests

Each tool has its own unit tests in `tests/`:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Structure

```
education-mcp-kit/
├── server.py        # Flask service exposing the tools
├── mcp_tools/       # classroom, quizgen, grading, logging tools
├── tests/           # one unit-test module per tool
├── Dockerfile
└── requirements.txt
```

> **V1 MVP.** Tools are modular by design, so new education capabilities can be added as standalone, testable units.
