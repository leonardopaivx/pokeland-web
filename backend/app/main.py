from flask import Flask, g
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from app.config.db import engine


def create_app(engine: Engine):
    app = Flask(__name__)

    app.config['FLASK_PYDANTIC_VALIDATION_ERROR_STATUS_CODE'] = 422

    @app.before_request
    def create_session():
        """Cria uma nova sessão antes de cada requisição."""
        g.db_session = Session(bind=engine)

    @app.teardown_request
    def close_session(exception=None):
        """Fecha a sessão após cada requisição."""
        db_session = g.pop('db_session', None)
        if db_session:
            if exception:
                db_session.rollback()
            db_session.close()

    @app.route('/')
    def health_check():
        g.db_session.execute(select(1))
        return {'status': True}

    from app.api.v1.api import api_v1_bp  # noqa: PLC0415, I001

    app.register_blueprint(api_v1_bp)

    return app


if __name__ == '__main__':
    app = create_app(engine)
    app.run(debug=True)
