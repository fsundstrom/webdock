import os
import requests
import json
import re
import pprint
from flask import request, abort, render_template
from app import app

# create index page
#########################
@app.route('/')
def index():
 
  # we are getting the info provied by flask for the conneciton 
  # ref http://werkzeug.pocoo.org/docs/wrappers/#werkzeug.wrappers.BaseRequest.remote_addr

  # get remote ip
  ip = request.environ['REMOTE_ADDR']
  head = request.headers
 
  # retirm template with info 
  return render_template("index.html", lookup_ip=ip, headers=head)

# Get Host info
##########################
@app.route('/host/<host>', methods=["GET"])
def get_host(host):
 
  # demo showing how to make a call 

  call = 'dig '+host+' +noall +answer |tail -1'
  output = os.popen(call).read()
  ip = re.sub(r'^.*\t','',output)
  return render_template("index.html", lookup_ip=ip)

####################################################################################
# Private methods, helpers and error handlers                                      #
####################################################################################

# default error handler
@app.errorhandler(400)
def bad_request(error):
  return "Bad request: %s" % error, 400

