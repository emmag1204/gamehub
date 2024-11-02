from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/games.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/images')

    db.init_app(app)
    Migrate(app, db)

    from .routes import main
    app.register_blueprint(main)

    @ app.cli.command('seed')
    def seed_db():
        from .models import Section, Game

        if not Section.query.first():
            sections = [
                Section(name='Competitive', image='competitive.jpg'),
                Section(name='Multiplayer', image='multiplayer.jpg'),
                Section(name='Adventure', image='adventure.jpg'),
            ]
            db.session.bulk_save_objects(sections)
            db.session.commit()

        if not Game.query.first():
            games = [
                Game(section='Competitive', name='League of Legends', description='MOBA game', platform='PC', image='lol.jpg'),
                Game(section='Multiplayer', name='Among Us', description='Social deduction game', platform='PC, Mobile', image='amongus.jpg'),
                Game(section='Adventure', name='Zelda', description='Action-adventure', platform='Switch', image='zelda.jpg'),
            ]
            db.session.bulk_save_objects(games)
            db.session.commit()

        print('Database seeded!')
        
    return app