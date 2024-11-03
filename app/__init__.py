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

    @app.cli.command('seed')
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
               Game(section='Competitive', name='League of Legends', description='A team strategy game where players control unique characters and try to destroy the enemy’s base.', platform='PC', image='lol.jpg'),
                Game(section='Multiplayer', name='Super Smash Bros.', description='A fighting game where famous Nintendo characters battle in different arenas.', platform='Switch', image='smash.jpg'),
                Game(section='Multiplayer', name='Mario Kart', description='A racing game with Nintendo characters who use special powers to win.', platform='Switch', image='mariokart.jpg'),
                Game(section='Multiplayer', name='Mario Party', description='A party game full of mini-games where players compete on boards to earn stars and coins.', platform='Switch', image='marioparty.jpg'),
                Game(section='Adventure', name='Minecraft', description='A building and adventure game where players explore and create worlds made of blocks.', platform='PC, Mobile, Console', image='minecraft.jpg'),
                Game(section='Multiplayer', name='Roblox', description='An online platform where users can create and play a variety of games made by the community.', platform='PC, Mobile', image='roblox.jpg'),
                Game(section='Competitive', name='Valorant', description='A shooting game where teams use unique character abilities to compete.', platform='PC', image='valorant.jpg'),
                Game(section='Adventure', name='Genshin Impact', description='An action game where players explore a fantasy world with magical characters.', platform='PC, Mobile', image='genshin.jpg'),
                Game(section='Competitive', name='Clash of Clans', description='A mobile strategy game where players build villages and battle others to gather resources.', platform='Mobile', image='clashofclans.jpg'),
                Game(section='Competitive', name='Fortnite', description='A game where players compete to be the last one standing on a large island.', platform='PC, Console', image='fortnite.jpg'),
                Game(section='Competitive', name='Apex Legends', description='A survival game where teams of unique characters compete to be the last standing.', platform='PC, Console', image='apex.jpg'),
                Game(section='Multiplayer', name='Overcooked 2', description='A cooking game where players work together to prepare meals under time pressure.', platform='PC, Console', image='overcooked2.jpg'),
                Game(section='Adventure', name='Pokemon', description='An adventure game where players catch and train creatures called Pokémon to battle others.', platform='Switch', image='pokemon.jpg'),
                Game(section='Adventure', name='Animal Crossing', description='A life simulation game where players develop an island into a community of animal friends.', platform='Switch', image='animalcrossing.jpg'),
                Game(section='Multiplayer', name='Rocket League', description='A game that combines soccer and cars, where players use rocket-powered cars to score goals.', platform='PC, Console', image='rocketleague.jpg')
            ]
            db.session.bulk_save_objects(games)
            db.session.commit()

        print('Database seeded!')
        
    return app