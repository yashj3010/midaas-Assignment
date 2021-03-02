from flask import Flask, request
import prime
import store
import time

######## FLASK APP ###########
app = Flask(__name__)
@app.route("/")
def index():
    return "Prime Number Generator"

####### PRIME ROUTE ###########
@app.route("/prime", methods=["GET","POST"])

def retrivePrimes():
    executionTime = 0

    ####### USER INPUT ###########
    params = request.json
    algo = params[0]
    lowerLimit = params[1]
    upperLimit = params[2]

    ####### CALLING PRIME MODULE ########
    if algo == 1:
        ticGenPrimes  = time.perf_counter()

        primeNumbers  = prime.generatePrimes(lowerLimit,upperLimit)

        tocGenPrimes  = time.perf_counter()
        executionTime = tocGenPrimes - ticGenPrimes

    elif algo == 2:
        ticGenSieve  = time.perf_counter()

        primeNumbers = prime.SieveOfEratosthenes(lowerLimit,upperLimit)

        tocGenSieve  = time.perf_counter()
        executionTime = tocGenSieve - ticGenSieve

    ######## INJECT RESULTS INTO DATABASE ####### 
    store.injectDb([lowerLimit,upperLimit], executionTime, algo,len(primeNumbers))

    ######## Returning The Answer ####### 
    return str(primeNumbers)     

######## RUN FLASK APP ###########
app.run(debug=True, host='127.0.1.2', port= 1111)
