from flask import Blueprint, render_template
from database.client import CLIENTS


clientroute = Blueprint("client", __name__)

@clientroute.route("/")
def list_clients():
    return render_template("list_clients.html", clients=CLIENTS)
@clientroute.route("client", methods=["PUT"])
def inserir_client():
    pass

@clientroute.route("/new")
def form_client():
    return {"pagina": "lista_clients"}


@clientroute.route("/<int:client_id>/edit")
def form_edir_client(client_id):
    return render_template("form_clients.html")


@clientroute.route("/<int:client_id>/uodate", methods=['PUT'])
def update_client(client_id):
    return render_template("form_edit_clients.html")


@clientroute.route("/<int:client_id>/delete", methods=["DELETE"])
def delete_client(client_id ):
    return {"pagina": "lista_clients"}


