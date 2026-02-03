from flask import Blueprint, request, jsonify
from models.chamado import Chamado
from database import database

chamados_bp = Blueprint("chamados", __name__)

# POST /chamados
@chamados_bp.route("/chamados", methods=["POST"])
def criar_chamado():
    dados = request.json

    chamado = Chamado(
        titulo=dados["titulo"],
        descricao=dados.get("descricao"),
        prioridade=dados["prioridade"]
    )
    chamado.save()

    return jsonify(chamado.to_dict()), 201


# PATCH /atribuir
@chamados_bp.route("/atribuir", methods=["PATCH"])
def atribuir_tecnico():
    dados = request.json
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE chamados
        SET tecnico_id = ?, status = 'Em Andamento'
        WHERE id = ?
    """, (dados["tecnico_id"], dados["chamado_id"]))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Chamado atribuído com sucesso"})


# PATCH /finalizar/<id>
@chamados_bp.route("/finalizar/<int:id>", methods=["PATCH"])
def finalizar_chamado(id):
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT tecnico_id FROM chamados WHERE id = ?", (id,))
    resultado = cursor.fetchone()

    if resultado is None or resultado[0] is None:
        return jsonify({"erro": "Chamado sem técnico atribuído"}), 400

    cursor.execute("""
        UPDATE chamados SET status = 'Fechado' WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Chamado finalizado"})


# GET /chamados/prioridade/<nivel>
@chamados_bp.route("/chamados/prioridade/<nivel>", methods=["GET"])
def filtrar_prioridade(nivel):
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM chamados WHERE prioridade = ?
    """, (nivel,))

    registros = cursor.fetchall()
    conn.close()

    chamados = []
    for c in registros:
        chamados.append({
            "id": c[0],
            "titulo": c[1],
            "descricao": c[2],
            "prioridade": c[3],
            "status": c[4],
            "tecnico_id": c[5]
        })

    return jsonify(chamados)
