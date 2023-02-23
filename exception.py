
payrate = 10.0
paycheck = 0

while True:
    try:
        answer = float(input('how many hours did you work:'))
        paycheck = answer * payrate
        print(f"your paycheck is ${paycheck:,.2f}")
        break

    except ValueError as err:                         #if there is an error it will skip the else statement 
        #print('there was an error') 
        print(f"There was an error. the error code is: {err}")

    #else:                           #runs if the exception does not run     
        #pass                        #does nothing
        paycheck = answer * payrate

    print("It is done")