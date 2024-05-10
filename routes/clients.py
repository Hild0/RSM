from flask import Blueprint, render_template, request
from database.client import CLIENTS


clientroute = Blueprint("clients", __name__)

@clientroute.route("/")
def list_clients():
    return render_template("list_clients.html", clients=CLIENTS)

@clientroute.route("client", methods=["POST"])
def add_clients():
    data = request.json

    new_user = {
        "id": len(CLIENTS) + 1,
        "nome": data["nome"],
        "email": data["email"],
        "pass": data["passwd"],
    }

    CLIENTS.append(new_user)

    return new_user

@clientroute.route("/new")
def form_client():
    return render_template("form_clients.html")

@clientroute.route("/<int:client_id>/edit")
def form_edit_client(client_id):
    return render_template("form_clients.html")

@clientroute.route("/<int:client_id>/uodate", methods=['PUT'])
def update_client(client_id):
    return render_template("form_edit_clients.html")

@clientroute.route("/<int:client_id>/delete", methods=["DELETE"])
def delete_client(client_id ):
    return {"pagina": "lista_clients"}


