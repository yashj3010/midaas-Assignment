import requests

api_url = 'http://127.0.1.2:1111/prime'

if __name__ == '__main__':
    
    try:
        while True:

            ######## MENU ####### 
            print("\n")
            print("1) For Native Algo, Takes Upper & Lower Limit")
            print("2) Sieve Of Eratosthenes Method, Faster Method")
            print("\n")
            
            ######## USER INPUTS ####### 
            n1 = int(input("Algo Number: "))
            n2 = int(input("Enter lower limit: "))
            n3 = int(input("Enter Upper limit(Less Than 10 Million): "))

            params = [n1,n2,n3]

            ######## POST USER DATA ####### 
            response = requests.post(url= api_url, json= params)

            ######## PROCESSING DATA ####### 
            primeNumbers = response.text.strip('][').split(', ')
            primeNumbers = [int(i) for i in primeNumbers] 

            ######## PRINT OUTPUT ####### 
            print("\n")
            print("################# ANSWER RECIEVED ###############")
            print("prime Numbers:",primeNumbers)
            print("No Of prime numbers:",len(primeNumbers))
            print("#################################################")
            
    except:
        print("Server Error, Run Server Script")








