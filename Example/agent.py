from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

rest = Flask(__name__)

class Agent:
  def __init__(self,name,portnumber):
    self.hostname = name
    self.portnumber = portnumber


  @rest.route('/api/v1/hello', methods=['GET'])
  def hello():
    print("Hello Agent")
    return jsonify({'result':'Hello from agent'})
  @rest.route('/api/v1/agent/agent2smbs')
  def agent2smbs():
    return jsonify({'prosumerId': 'e15017b1-f0b9-409c-961d-2cf409c12b31','timeSlot': '2022-02-17T10:30:00+00:00','energyInKwh': -500,'priceInEuroPerKwh': 0.5,  'gridLocation': '',  'P2P-Clearings':'blablabla' })


  def go(self):
    rest.run(host=self.hostname, port=self.portnumber)
