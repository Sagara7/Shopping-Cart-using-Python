import unittest
from Sagara_app import CartItem, Shoppingcart

class TestCartItem(unittest.TestCase):     

  def test_init(self):
    item = CartItem('apel', 3000)
    self.assertEqual(item.nama, 'apel')
    self.assertEqual(item.harga, 3000)

class TestShoppingcart(unittest.TestCase):
  
  def setUp(self):
    self.cart = Shoppingcart()

  def test_add_data(self):
    self.cart.add_data('apel', 3000)
    self.assertEqual(len(self.cart.items),1)

  def test_remove_data(self):
    nama_barang = 'apel'
    self.cart.add_data(nama_barang, 3000)
    self.cart.remove_data(nama_barang)
    self.assertEqual(len(self.cart.items),0)

  def test_cal_total(self):
    self.cart.add_data('apel', 3000)
    self.cart.add_data('jeruk', 2000)
    self.assertEqual(self.cart.cal_total(), 5000)

if __name__ == "__main__":    
    unittest.main()     