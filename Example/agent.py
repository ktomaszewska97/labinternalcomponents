from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

rest = Flask(__name__)

class Agent:
  def __init__(self,name,portnumber):
    self.hostname = name
    self.portnumber = portnumber

  # your code comes here
  json_agent2smbs=jsonify({"prosumerId": "e15017b1-f0b9-409c-961d-2cf409c12b31","timeSlot": "2022-02-17T10:30:00+00:00","energyInKwh": -500,"priceInEuroPerKwh": 0.5,  "gridLocation": "/G21/N17/E12",  "P2P-Clearings":"blablabla" })

  @rest.route('/api/v1/hello', methods=['GET'])
  def hello():
    print("Hello Agent")
    return jsonify({'result':'Hello from agent'})
  @rest.route('/api/v1/pp/agent2smbs')
  def agent2smbs():
    return json_agent2smbs


  def go(self):
    rest.run(host=self.hostname, port=self.portnumber)
