import os
from flask import Blueprint, request, jsonify, url_for
from werkzeug.utils import secure_filename
from .models import Game, Section
from . import db

main = Blueprint('main', __name__)

@main.route('/sections', methods=['GET'])
def get_sections():
    sections = Section.query.all()
    return jsonify([{'name': section.name, 'image': url_for('static', filename=f'images/{section.image}')} for section in sections])

@main.route('/games', methods=['GET'])
def get_games_by_section():
    section = request.args.get('section')
    games = Game.query.filter_by(section=section).all()
    return jsonify([{'name': game.name, 'description': game.description, 'platform': game.platform, 'image': url_for('static', filename=f'images/{game.image}')} for game in games])

@main.route('/game/<int:id>', methods=['GET'])
def get_game(id):
    game = Game.query.get_or_404(id)
    return jsonify({
        'name': game.name,
        'description': game.description,
        'platform': game.platform,
        'image': url_for('static', filename=f'images/{game.image}')
    })

@main.route('/game', methods=['POST'])
def add_game():
    data = request.form
    file = request.files['image']

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(request.app.config['UPLOAD_FOLDER'], filename))

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