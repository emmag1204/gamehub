import os
from flask import Blueprint, request, jsonify, url_for, render_template, current_app
from werkzeug.utils import secure_filename
from .models import Game, Section
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    sections = Section.query.all()  
    return render_template('index.html', sections=sections)  

@main.route('/games/<section_name>', methods=['GET'])
def get_games_by_section(section_name):
    games = Game.query.filter_by(section=section_name).all() 
    return render_template('games.html', games=games, section_name=section_name)  

@main.route('/game', methods=['POST'])
def add_game():
    data = request.form  
    file = request.files['image']  

    if file:
        filename = secure_filename(file.filename)  
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename)) 

    new_game = Game(
        section=data['section'],
        name=data['name'],
        description=data['description'],
        platform=data['platform'],
        image=filename
    )

    db.session.add(new_game)  
    db.session.commit()  

    return jsonify({'message': 'Game created successfully!'})  

@main.route('/add-game', methods=['GET'])
def add_game_page():
    return render_template('add_game.html') 