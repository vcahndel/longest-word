# wsgi.py
from flask import Flask, render_template, request

# [...]

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)
