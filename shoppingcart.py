
from collections import Counter

class Shoppingcart:

    def __init__(self):
        
        self.total = 0 
        self.discount_amount = 0
        self.subtotal = 0
        self.discount = "" #String that is used to construct discount message
        self.products = {"apple":1,"milk":1.3,"bread":0.8,"soup":0.65} #Taking products and its price as a dictionary
        

    def add_bill(self,cart_list): #Function to calculate bill amount
                          
      self.cart_list = Counter(cart_list) #Taking list of items in the cart as dictionary {Productname : Quantity}

      for i,j in self.cart_list.items(): #Traversing through the cart dictionary

      
          self.subtotal += (self.products[i]*j)  #Finding Subtotal of all products

          if i.lower() == "apple":  #If apple is present discount amount will be added up

            self.discount_amount += (self.products[i] * 0.1) * j  #Discount amount calculation 
            
            self.discount += "Apple 10% 0ff -" + str(round(((self.products[i] * 0.1)*j),2)) +"$\n"    #Discount message
            

          elif i.lower() == "soup" and j == 2 and "bread" in self.cart_list: #Discount check for 2 soup + bread case

              self.discount_amount += (self.products["bread"] * self.cart_list["bread"] *0.5)   #Discount amount calculation 

              self.discount += "Breads at Half price -" + str(self.products["bread"] * self.cart_list["bread"] *0.5) + "$\n"  #Discount Message

              

    def get_bill(self)  : #Function to display bill

        if len(self.discount) == 0:   #If cart doen't have any discounted items

          self.discount = "(no offers available)"
          self.total = self.subtotal
        
        else:

          self.total = self.subtotal - self.discount_amount  #If cart have discounted items reduce the discount and subtotal to arrive into total
        

        final_bill =  "\n" + "Subtotal : " + str(round((self.subtotal),2))+"$" +"\n" + str(self.discount) +"\n" + "Total : " + str(round((self.total),2)) +"$"

        
        
        return final_bill

    def get_bill_test(self): #Function for unittestesting
      
      return round(float(self.total),2)

      


        
def main():

  print("Welcome to Shopping Mart \n\n Available products and prices are below: \n 1.Apple - 1$\n 2.Bread - 0.8$\n 3.Milk - 1.3$\n 4.Soup - 0.65$")
  print("\nAvailable discounts below:")
  print("\nBuy Apples at 10% off")
  print("\nBuy Two Soups and Get Bread at Half price")
  
  
  input_list = input("\nEnter the items you wish to buy with spaces inbetween: PriceBasket ")
  
  if len(input_list) == 0:
    print("Please add items to cart")
    input_list = input("\nEnter the items you wish to buy with spaces inbetween: PriceBasket ")

  input_list = input_list.split() # converting input string with spaces to a list

  available_products = {"apple":100,"bread":100,"milk":100,"soup":100} #Products with random quantity that can be used in future if a function comes up to reduce the quantity of the product when customer buys it

  
  
  input_list = [x.lower() for x in input_list]  #Changing input to lower case to avoid case related issues
 
  for i in input_list:

    try:

      if available_products[i]:
        pass #Checking if inputted items are available else printing not available also to subtract quantity of the product in future
        
    except KeyError as e:

      print("\n" +str(e) + " not available, Billing other available products")


  input_list = [x for x in input_list if x in available_products] #Making final input list with products that are only available 
  
  
  
  
  cart = Shoppingcart() #Creating object

  cart.add_bill(input_list)

  print(cart.get_bill())  #Printing output

  
  

if __name__ == "__main__":
    main()

