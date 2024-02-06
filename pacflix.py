class pacflix():
    list_of_referral_code = []

    def __init__(self, user_name):
        self.user_name = user_name
        self.start_date = None
        self.end_date = None
        self.current_plan = None
        self.duration = 0

        pacflix.list_of_referral_code.append(self.user_name)
        print(f"Your successfully created, share this code '{self.user_name}' to your friend to get benefits.")
    
    def list_plan(self):
        print("List of Pacflix plan")
        print("1. Basic Plan")
        print("SD, 1 device, Movie, Rp 120.000,-")
        print()
        print("2. Basic Plan")
        print("HD, 2 device, Movie + Sport, Rp 160.000,-")
        print()
        print("1. Basic Plan")
        print("UHD, 3 device, Movie + Sport + Original, Rp 200.000,-")

    #Chek Plan  Yang Kita Pakai
    def check_plan(self):
        if(self.current_plan == None):
            print("You don't have any subscription")
        else: 
            print(f"Your current plan is {self.current_plan}.")

    # Purchase Plan
    def 
