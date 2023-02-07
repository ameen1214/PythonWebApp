from app import app
from models import db, Users, Memberships, Products


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Users=Users, Memberships=Memberships, Products=Products)
