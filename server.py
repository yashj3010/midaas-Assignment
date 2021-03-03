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
    if (params == None):
        data = "No Data Recieved"
        
    elif (params != None):

        algo = params[0]
        lowerLimit = params[1]
        upperLimit = params[2]

        primes,executionTime = prime.giveOutput(algo, lowerLimit, upperLimit)

        data = {"primes": primes}
    ######## Returning The Answer ####### 
    return data

    ######## INJECT RESULTS INTO DATABASE ####### 
    store.injectDb([lowerLimit,upperLimit], executionTime, algo,len(primeNumbers))

def primeGen():
    app.run(debug=True, host='127.0.1.2', port= 1111)    
  

######## RUN FLASK APP ###########
if __name__ == "__main__":
    try:
        primeGen()
    except Exception as e:
        print(e)