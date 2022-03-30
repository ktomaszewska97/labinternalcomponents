from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

rest = Flask(__name__)

class Osbd:
  def __init__(self,name,portnumber):
    self.hostname = name
    self.portnumber = portnumber

  def __call__(self):
    print("Instance is called via special method")


  # your code comes here

  @rest.route('/api/v1/hello', methods=['POST'])
  def hello():
    print("Hello world")
    return jsonify({'result':'Hello World'})

  def go(self):
    rest.run(host=self.hostname, port=self.portnumber)
