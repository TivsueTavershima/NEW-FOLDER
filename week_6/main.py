
from eurconverter import Eurconverter
from usdconverter import Converter



class  Main():
    def __init__(self, name):
            self.name = name
            self.usdconverter = Converter(1436)
            self.eurconverter = Eurconverter(1661.50)
            
            
    def run(self):
        print(f"{"==" * 13}\nWelcome,{self.name}\n{"==" * 13}")
        while True:
            option = input("1. USD to NGN\n2. EUR to NGN\nWhat do you want to onvert: ")
            amount = float(input("How much do you want to convert?: "))
            
            match option:
                            
                case "1":
                    result = self.usdconverter.convert_to_naira(amount)
                    print(f"your {amount} to NGN is {result}.")
                
                case "2":
                    result = self.eurconverter.convert_to_naira(amount)
                    print(f"your {amount} to NGN is {result}.")
                
            
                case _:
                    print("Invalid option")    
            break      

if __name__ == "__main__":
    app = Main("Currency Converter")
    app.run()


