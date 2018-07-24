#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)

tasks = [{
    'id': 1,
    'title': u'Comprar Coisas',
    'description': u'Leite, Queijo, Pizza, Sorvete, Roupas',
    'done': False,
    }, {
    'id': 2,
    'title': u'Aprender Python',
    'description': u'Você precisa procurar um bom tutorial de Python na Web',
    'done': False,
    }]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

