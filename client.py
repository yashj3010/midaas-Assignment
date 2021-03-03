import requests
import requests.exceptions as e
import json


def primeAPI(params):
    try:
        api_url = 'http://127.0.1.2:1111/prime'

        response = requests.post(url= api_url, json= params)
        responseDict = json.loads(response.text)

    except e.ConnectionError as err :
        print(err)
        responseDict = "No Response"

    return responseDict
    
def takeInput():
  
    while True:

        ######## MENU ####### 
        print("\n")
        print("Please Select An Algorithm")
        print("1) Navtive, Slower but lower memory use")
        print("2) Sieve Of Eratosthenes Method, Faster but higher memory use")
        print("\n")
        
        ######## USER INPUTS ####### 
        n1 = int(input("Algo Number: "))
        n2 = int(input("Enter lower limit: "))
        n3 = int(input("Enter Upper limit(Less Than 10 Million): "))

        params = [n1,n2,n3]

        ######## CALLING API #########
        response = primeAPI(params)
        
        ######## PROCESSING RESPONSE #########
        if response != "No Response":
            primeNumbers = response['primes']

            print("\n")
            print("################# ANSWER RECIEVED ###############")
            print("prime Numbers:",primeNumbers)
            print("No Of prime numbers:",len(primeNumbers))
            print("#################################################")     
        else:
            print("FAILED TO GET A RESPONSE FROM SERVER")
  
if __name__ == '__main__':
    takeInput()
   








