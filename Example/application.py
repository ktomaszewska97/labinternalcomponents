from osbd import Osbd
from coordinator import Coordinator
from agent import Agent

from threading import Thread
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth


rest = Flask(__name__)


api = Api(rest, prefix="/api/v1")
auth = HTTPBasicAuth()
USER_DATA = {
        "admin": "SupErSecretP!?"
}
@auth.verify_password
def verify(username, password):
        if not(username and password):
                return False
        return USER_DATA.get(username) == password


#iterate through all components running on this machine
def f():
   print("OSBD start")
   osbd = Osbd("0.0.0.0",5000)
   osbd.go()

def c():
  coord = Coordinator("0.0.0.0",5001)
  coord.go()

def a():
  agent = Agent("0.0.0.0",5002)
  agent.go()

x = Thread(target=f, args=())
x.start()

y = Thread(target=c, args=())      
y.start()

z = Thread(target=a, args=())      
z.start()

