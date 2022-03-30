from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

rest = Flask(__name__)

class Coordinator:
  def __init__(self,name,portnumber):
    self.hostname = name
    self.portnumber = portnumber

  # your code comes here

  @rest.route('/api/v1/hello', methods=['POST'])
  def hello():
    print("Hello Coordinator")
    return jsonify({'result':'Hello Coordinator'})

  def go(self):
    rest.run(host=self.hostname, port=self.portnumber)
