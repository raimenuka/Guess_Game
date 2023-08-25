import random



def main():
    generated_Number= random.randrange(1000, 10000)
    print("\n........................................\n")
    print("..........Welcome to the game.............\n")
    print("Menu.........................................\n")
    print("..Select an option..")
    print ("  1....quit")
    print ("  Else guess a 4 digit number")
    n = 0
    while True:
        number_value=int(input("Enter the number: "))
        if number_value==1:
            print(".........Thanks for playing the game welcome again...........")
            break
        inputr= [number_value]
        input1 = [generated_Number]

        # Converting to string
        input_str = str(inputr[0])
        input_str2 = str(input1[0])

        output = []
        output1 = []
        list = ["_","_","_","_"]

        for char in input_str:
            output.append(int(char))

        for char in input_str2:
            output1.append(int(char))
        # Printing output
        for i in output:
            for r in output1:
                p=output.index(i)
                y=output1.index(r)
                if i==r and p==y:
                    list[p]="0"
                elif i==r:
                    list[p]="X"
        print(list)

        print("...Clue...\n")
        print(' '.join(list))
        print("\n")

        if generated_Number==number_value:
            print("\n...........Congratulations you worn the game............\n")
            print("Number of attempts:" ,n)
            print("......1.Play again")
            print("......2.Quit game")
            option=input("Select an option: ")
            if option=="1":
                main()
            elif option=="2":
                print(".........Thanks for playing the game welcome again...........")
                print("Number of attempts:" ,n)
                break
            else:
                print("Invalid option")
                main()

        n +=1
main()
