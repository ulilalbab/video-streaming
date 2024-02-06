from datetime import datetime
from dateutil.relativedelta import relativedelta

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
        print("2. Standard Plan")
        print("HD, 2 device, Movie + Sport, Rp 160.000,-")
        print()
        print("1. Premium Plan")
        print("UHD, 3 device, Movie + Sport + Original, Rp 200.000,-")

    #Chek Plan  Yang Kita Pakai
    def check_plan(self):
        if(self.current_plan == None):
            print("You don't have any subscription")
        else: 
            print(f"Your current plan is {self.current_plan}.")
            print(f"Start subs at {self.start_date}.")
            print(f"End subs at {self.end_date}.")
    # Purchase Plan
    def purchase(self, new_plan, ref_code, duration):
        total_price = 0
        
        if((ref_code != None) and (ref_code in pacflix.list_of_referral_code)):
            self.duration = duration    # Durasi digunakan saat kondisi dibawah valid
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(month=duration)                 # Akhir langganan

            if(new_plan == "Basic Plan"):
                self.current_plan = "Basic Plan"
                total_price = (120_000 - (0.04 * 120_000))
                print(f"You're selected Basic Plan with referral code from {ref_code},  Price {total_price}")

            elif(new_plan == "Standard Plan"):
                self.current_plan = "Standard Plan"
                total_price = (160_000 - (0.04 * 160_000))
                print(f"You're selected Standard Plan with referral code from {ref_code},  Price {total_price}")
               
                
            elif(new_plan == "Premium Plan"):
                self.current_plan = "Premium Plan"
                total_price = (200_000 - (0.04 * 200_000))
                print(f"You're selected Premium Plan with referral code from {ref_code},  Price {total_price}")

            else:
                self.duration = 0
                self.start_date = None
                self.end_date = None                
                print("Your selected plan is invalid")


        elif((ref_code != None) and (ref_code not in pacflix.list_of_referral_code)):
            print("Your referral code is invalid")

        elif(ref_code == None):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)

            if(new_plan == "Basic Plan"):
                self.current_plan = "Basic Plan"
                total_price = 120_000
                print(f"You're selected Basic Plan,  Price {total_price}")

            elif(new_plan == "Standard Plan"):
                self.current_plan = "Standard Plan"
                total_price = 160_000
                print(f"You're selected Standard Plan,  Price {total_price}")
               
                
            elif(new_plan == "Premium Plan"):
                self.current_plan = "Premium Plan"
                total_price = 200_000
                print(f"You're selected Premium Plan,  Price {total_price}")

            else:
                self.duration = 0
                self.start_date = None
                self.end_date = None
                print("Your selected plan is invalid")
        else:
            print("We miss you to use our services")


#Upgrade Plan
    def upgrade_plan(self, new_plan):
        subs_time = self.end_date - datetime.now()
        total_price = 0


        if(subs_time.days > 360):
            if(self.current_plan == "Basic Plan"):
                if(new_plan == "Standard Plan"):
                    self.current_plan = "Standard Plan"
                    total_price = (160_000 - (160_000 *0.05))
                    print(f"Upgrade to {self.current_plan}, price + discount {total_price}")
                
                elif(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = (200_000 - (200_000 *0.05))
                    print(f"Upgrade to {self.current_plan}, price + discount {total_price}")
                else:
                print("Your selected new plan is invalid!.")


            elif(self.current_plan == "Standard Plan"):
                if(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = (200_000 - (200_000 * 0.05))
                    print(f"Upgrade to {self.current_plan}, price + discount = {total_price}.")
            
                else:
                    print("Your selected new plan is invalid")
            else:
                print("You're in the highest tier, you can't dowgrade!.")
    
        else:
            if(self.current_plan == "Basic Plan"):
                if(new_plan == "Standard Plan"):
                    self.current_plan = "Standard Plan"
                    total_price = 160_000
                    print(f"Upgrade to {self.current_plan},price {total_price}.")
        
                elif(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = 200_000
                    print(f"Upgrade to {self.current_plan},price {total_price}.")

                else:
                    print("Your selected new plan is invalid")

            elif(self.current_plan == "Standard Plan"):
                if(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = 200_000
                    print(f"Upgrade to {self.current_plan},price {total_price}.")
                
                else:
                    print("Your selected in highest new plan is invalid.")    

            else:
                print("You're in highest tier, you can't downgrade!.")
