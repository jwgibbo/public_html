
def plus_one(num):
    ans = num + 1
    return ans

def main():
    print("Program started")
    #user_num = int(input("Enter a number: "))
    #print("Here is your number plus one!: " + str(plus_one(user_num)))


    candies = ["almond joy", "twix", "snickers", "whoppers"]

    #print the candies:
    for candy in candies:
        for letter in candy:
            print(letter)
        print("-----")
    
    print("Program exiting...")
    



#One single call to our main
#function. 
main()
