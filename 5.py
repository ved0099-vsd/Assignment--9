def Division(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("not Divisible by 3 & 5")

def main():
    Division(15)

if __name__ == "__main__":
   main()