from flask import Flask, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from db_connection import session
from db_crud import get_ms_game_title


app = Flask(__name__)

@app.route("/games/parts", methods=["GET"])
def get_games():
    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 100))
        offset = (page - 1) * limit
        filters = request.args.to_dict()
        filters.pop("page", None)
        filters.pop("limit", None)
        games = get_ms_game_title(connection_session = session, limit = limit, offset = offset, **filters)
        result = []
        for game in games:
            result.append({
                "id": game.id,
                "game_title": game.game_title,
                "is_active": game.is_active,
                "create_timestamp": game.create_timestamp.isoformat() if game.create_timestamp else None,
                "update_timestamp": game.update_timestamp.isoformat() if game.update_timestamp else None
            })
        return jsonify({
            "page": page,
            "limit": limit,
            "data": result
        })
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)