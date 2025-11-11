



class Converter():
      def __init__(self,exchange_rate):
        self.exchange_rate = exchange_rate
        
      def convert_to_naira(self,dollar):
        return dollar * self.exchange_rate
  
  
