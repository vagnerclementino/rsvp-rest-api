#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

rsvps = [
    {
        'id': 1,
        'nome': u'Vagner Clementino dos Santos',
        'email': u'vagner.clementino@gmail.com',
        'evento': u'Cerimônia e Recepção',
        'acompanhante': u'1 Acompanhante',
        'observacao': u'Não se aplica'
        },
    {
        'id': 2,
        'nome': u'Andreza Vieira Lelis da Silva',
        'email': u'a.vieiralelis@gmail.com',
        'evento': u'Cerimônia e Recepção',
        'acompanhante': u'1 Acompanhante',
        'observacao': u'Não se aplica'
        }
]

def make_public_rsvp(rsvp):
    new_rsvp = {}
    for field in rsvp:
        if field == 'id':
            new_rsvp['uri'] = url_for('get_rsvp',
                                      rsvp_id = rsvp['id'],
                                      _external = True
                                      )
        else:
            new_rsvp[field] = rsvp[field]
    return new_rsvp

@app.route('/rsvp/api/v1.0/rsvps', methods = ['GET'])
# @auth.login_required
def get_rsvps():

    json_response = jsonify( { 'rsvps': list(map(make_public_rsvp, rsvps)) })
    return make_response(json_response)

@app.route('/rsvp/api/v1.0/rsvps/<int:rsvp_id>', methods = ['GET'])
# @auth.login_required
def get_rsvp(rsvp_id):
    rsvp = list(filter(lambda t: t['id'] == rsvp_id, rsvps))
    if len(rsvp) == 0:
        abort(404)
    return jsonify( { 'rsvp': make_public_rsvp(rsvp[0]) } )

@app.route('/rsvp/api/v1.0/rsvps', methods = ['POST'])
    # @auth.login_required
def create_rsvp():
    if not request.form or 'nome' not in request.form:
         abort(400)
    rsvp = {
        'id': rsvps[-1]['id'] + 1,
        'acompanhante': request.form['acompanhante'],
        'email': request.form['email'],
        'evento': request.form['evento'],
        'nome': str(request.form['nome']),
        'observacao': request.form.get('observacao', None)
    }
    rsvps.append(rsvp)
    return jsonify({'rsvp': make_public_rsvp(rsvp) } ), 201

@app.route('/rsvp/api/v1.0/rsvps/<int:task_id>', methods = ['PUT'])
# @auth.login_required
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify( { 'task': make_public_task(task[0]) } )

@app.route('/rsvp/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
# @auth.login_required
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify( { 'result': True } )


if __name__ == '__main__':
    app.run(debug=True)
