

from shoppingcart import *

import unittest


class Testshoppingcart(unittest.TestCase):
  
  def test_no_discount(self): #Unit test for testing cart with no discounted products 

    cart = Shoppingcart()
    cart.add_bill(["bread","milk","soup"])
    cart.get_bill()
    self.assertEqual(cart.get_bill_test(), 2.75)

  def test_apple_discount(self): #Unit test for testing cart with apples

    cart = Shoppingcart()
    cart.add_bill(["apple","apple","apple"])
    cart.get_bill()
    self.assertEqual(cart.get_bill_test(), 2.7)

  def test_bread_discount(self): #Unit test for testing cart with two soup and a bread

    cart = Shoppingcart()
    cart.add_bill(["soup","soup","bread"])
    cart.get_bill()
    self.assertEqual(cart.get_bill_test(), 1.7)

  def test_requirement_document(self): #Unit test for testing cart with items mentioned in mailed requirements document

    cart = Shoppingcart()
    cart.add_bill(["apple","milk","bread"])
    cart.get_bill()
    self.assertEqual(cart.get_bill_test(), 3.0)

