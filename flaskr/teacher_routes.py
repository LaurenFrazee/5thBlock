from datetime import date
from flask import Blueprint, request, session, abort

from flaskr.db import db
from flaskr.models import Course
from flaskr.auth_helpers import login_required, role_required

teacher_bp = Blueprint("teacher", __name__, url_prefix="/teacher")


def _require_course_owner(course: Course) -> None:
    """Abort if the logged-in teacher doesn't own this course."""
    teacher_id = session.get("user_id")
    if teacher_id is None:
        abort(401)
    if course.teacher_id != teacher_id:
        abort(403)


@teacher_bp.route("/courses", methods=["GET"])
@login_required
@role_required("teacher")
def list_courses():
    teacher_id = session["user_id"]
    courses = Course.query.filter_by(teacher_id=teacher_id).order_by(Course.id.desc()).all()

    # Minimal response for now (no UI yet)
    lines = [f"{c.id}: {c.title} (published={c.published})" for c in courses]
    return "Courses:\n" + ("\n".join(lines) if lines else "(none)")


@teacher_bp.route("/courses/new", methods=["GET"])
@login_required
@role_required("teacher")
def new_course_form():
    # Placeholder until templates exist
    return (
        "Create Course (POST to this URL)\n"
        "Fields: title (required), description, start_date (YYYY-MM-DD), end_date (YYYY-MM-DD)\n"
    )


@teacher_bp.route("/courses/new", methods=["POST"])
@login_required
@role_required("teacher")
def create_course():
    teacher_id = session["user_id"]

    title = (request.form.get("title") or "").strip()
    description = (request.form.get("description") or "").strip() or None

    start_date_raw = (request.form.get("start_date") or "").strip()
    end_date_raw = (request.form.get("end_date") or "").strip()

    if not title:
        return "Title is required", 400

    def parse_date(val: str):
        if not val:
            return None
        try:
            return date.fromisoformat(val)
        except ValueError:
            return None

    start_date_val = parse_date(start_date_raw)
    end_date_val = parse_date(end_date_raw)

    # If user supplied a date but it's invalid
    if start_date_raw and start_date_val is None:
        return "Invalid start_date. Use YYYY-MM-DD.", 400
    if end_date_raw and end_date_val is None:
        return "Invalid end_date. Use YYYY-MM-DD.", 400

    course = Course(
        title=title,
        description=description,
        teacher_id=teacher_id,   # IMPORTANT: from session, not form
        published=False,
        start_date=start_date_val,
        end_date=end_date_val,
    )

    db.session.add(course)
    db.session.commit()

    return f"Created course {course.id}: {course.title}", 201


@teacher_bp.route("/courses/<int:course_id>/edit", methods=["GET"])
@login_required
@role_required("teacher")
def edit_course_form(course_id: int):
    course = Course.query.get_or_404(course_id)
    _require_course_owner(course)

    # Placeholder until templates exist
    return (
        f"Edit Course {course.id}\n"
        f"Current: title={course.title!r}, published={course.published}\n"
        "POST to this URL with: title (required), description, start_date, end_date\n"
    )


@teacher_bp.route("/courses/<int:course_id>/edit", methods=["POST"])
@login_required
@role_required("teacher")
def update_course(course_id: int):
    course = Course.query.get_or_404(course_id)
    _require_course_owner(course)

    title = (request.form.get("title") or "").strip()
    description = (request.form.get("description") or "").strip() or None

    start_date_raw = (request.form.get("start_date") or "").strip()
    end_date_raw = (request.form.get("end_date") or "").strip()

    if not title:
        return "Title is required", 400

    def parse_date(val: str):
        if not val:
            return None
        try:
            return date.fromisoformat(val)
        except ValueError:
            return None

    start_date_val = parse_date(start_date_raw)
    end_date_val = parse_date(end_date_raw)

    if start_date_raw and start_date_val is None:
        return "Invalid start_date. Use YYYY-MM-DD.", 400
    if end_date_raw and end_date_val is None:
        return "Invalid end_date. Use YYYY-MM-DD.", 400

    course.title = title
    course.description = description
    course.start_date = start_date_val
    course.end_date = end_date_val

    db.session.commit()
    return f"Updated course {course.id}", 200


@teacher_bp.route("/courses/<int:course_id>/delete", methods=["POST"])
@login_required
@role_required("teacher")
def delete_course(course_id: int):
    course = Course.query.get_or_404(course_id)
    _require_course_owner(course)

    db.session.delete(course)
    db.session.commit()
    return f"Deleted course {course_id}", 200
