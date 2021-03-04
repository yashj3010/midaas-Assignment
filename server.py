from flask import Flask, request
from flask.wrappers import Response

import prime
import store


######## FLASK APP ###########
app = Flask(__name__)
@app.route("/")
def index():
    return "Prime Number Generator"

####### PRIME ROUTE ###########
@app.route("/prime", methods=["GET","POST"])

def retrivePrimes():
    data = []

    ####### USER INPUT ###########
    params = request.json

    ####### CALLING PRIME MODULE ########        
    if (params != None):

        algo = params[0]
        lowerLimit = params[1]
        upperLimit = params[2]

        primes,executionTime = prime.giveOutput(algo, lowerLimit, upperLimit)

        data = {"primes": primes}
  
        ######## INJECT RESULTS INTO DATABASE ####### 
        store.injectDb([lowerLimit,upperLimit], executionTime, algo, len(primes))

    elif (params == None):
        data = "No Input Recieved"

    return data

def primeGen():
    try:
        app.run(debug=True, host='127.0.1.2', port= 1111)
    except Exception as e:
        print(e)    
  

######## RUN FLASK APP ###########
if __name__ == "__main__":
    primeGen()
