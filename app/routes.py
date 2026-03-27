from flask import Blueprint, request, jsonify, render_template
from .models import get_all_tasks, add_task, delete_task, update_task, init_db

bp = Blueprint('main', __name__)

# Initialize DB once
@bp.before_app_request
def setup():
    init_db()


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(get_all_tasks())


@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    # Validation
    if not data.get("title"):
        return {"error": "Title required"}, 400

    add_task(data["title"])
    return {"message": "Task added"}


@bp.route("/tasks/<int:id>", methods=["DELETE"])
def remove_task(id):
    delete_task(id)
    return {"message": "Task deleted"}


@bp.route("/tasks/<int:id>", methods=["PUT"])
def toggle_task(id):
    data = request.json
    update_task(id, data["completed"])
    return {"message": "Updated"}