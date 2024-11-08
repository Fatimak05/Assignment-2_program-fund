from datetime import date

class EBook:
  """This class represents an ebook with the attributes title, author, publication date,genre, and price."""
  #initializes EBook attributes
  def __init__(self,title,author,publicationDate,genre,price):
      self._title=title
      self._author=author
      self._publicationDate=publicationDate
      self._genre=genre
      self._price=price


  #Setter and getter methods
  def get_title(self):
      return self._title

  def set_title(self,title):
      self._title=title

  def get_author(self):
      return self._author

  def set_author(self,author):
      self._author=author

  def get_publicationDate(self):
      return self._publicationDate

  def set_publicationDate(self,publicationDate):
      self._publicationDate=publicationDate

  def get_genre(self):
      return self._genre

  def set_genre(self,genre):
      self._genre=genre

  def get_price(self):
      return self._price

  def set_price(self,price):
      self._price=price

  def __str__(self):
      return f"Title: {self._title}, Author: {self._author}, Genre: {self._genre}, Price: ${self._price}"

class Shoppingcart:
  # Initializes shopping cart with an empty list for eBook items
  def __init__(self):
      self._cartItems = []  # Aggregation because the Shoppingcart can exist independently of the EBook
      self._totalQuantity = 0

#Setters and getters
  def get_cartItems(self):
      return self._cartItems

  def set_cartItems(self, cartItems):
      self._cartItems = cartItems

  def get_totalQuantity(self):
      return self._totalQuantity

  def set_totalQuantity(self, totalQuantity):
      self._totalQuantity = totalQuantity

  def addItem(self, eBook):
      """Adds an eBook to the shopping cart."""
      self._cartItems.append(eBook)
      self._totalQuantity += 1

  def removeItem(self, eBook):
      """Removes an eBook from the shopping cart."""
      self._cartItems.remove(eBook)
      self._totalQuantity -= 1

  def updateQuantity(self):
      """Updates the total quantity of items in the cart."""
      self._totalQuantity = len(self._cartItems)

  def calculateTotal(self):
      """Calculates the total price of all eBooks in the cart."""
      return sum([eBook.get_price() for eBook in self._cartItems])

  def __str__(self):
      """Returns a string representation of the ShoppingCart."""
      return f"Shopping Cart: Items: {[eBook.get_title() for eBook in self._cartItems]}, Total Quantity: {self._totalQuantity}"


  #initilazes Order attributes
class Order:

  def __init__(self, orderID, orderDate, paymentID, paymentMethod="Credit Card"):
       self._orderID = orderID
       self._orderDate = orderDate
       self._items = []  # Aggregation with EBook
       self._totalAmount = 0.0
       self.payment = Payment(paymentID, orderDate, paymentMethod)  #Composition with Payment

#Setters and getters
  def get_orderID(self):
      return self._orderID

  def set_orderID(self, orderID):
      self._orderID = orderID

  def get_orderDate(self):
      return self._orderDate

  def set_orderDate(self, orderDate):
      self._orderDate = orderDate

  def get_items(self):
      return self._items

  def set_items(self, items):
      self._items = items

  def get_payment(self):
      return self.payment

  def get_totalAmount(self):
      return self._totalAmount

  def set_totalAmount(self, totalAmount):
      self._totalAmount = totalAmount

#Method to apply discounts
  def applyDiscounts(self, customer):
      """Apply discounts if the customer is a loyalty member."""
      if isinstance(customer, LoyaltyMembership):
          self._totalAmount -= customer.applyloyaltyDiscount(self)

#method to calculate Total
  def calculateTotal(self, customer=None):
      """Calculate the total cost of the order, including discounts if applicable."""
      self._totalAmount = sum(item.get_price() for item in self._items)
      if customer:
          self.applyDiscounts(customer)
      return self._totalAmount


  def __str__(self):
      item_details = ", ".join(item.get_title() for item in self._items)
      return f"Order ID: {self._orderID}, Date: {self._orderDate}, Items: [{item_details}], Total Amount: ${self._totalAmount:.2f}"


class Payment:
  """This class represents payment with attributes ."""

  #initializes Payment attributes
  def __init__(self,paymentID,paymentDate, paymentMethod, paymentStatus="Pending",vatRate=0.08 ):
      self._paymentID=paymentID
      self._paymentDate=paymentDate
      self._finalAmount= 0.0
      self._paymentMethod=paymentMethod
      self._paymentStatus=paymentStatus
      self._invoice= ""
      self._vatRate=vatRate

#Setters and getters
  def get_paymentID(self):
      """Return the payment ID."""
      return self._paymentID

  def get_paymentDate(self):
      """Return the payment date."""
      return self._paymentDate

  def get_finalAmount(self):
      """Return the final amount after VAT."""
      return self._finalAmount

  def get_paymentMethod(self):
      """Return the payment method."""
      return self._paymentMethod

  def get_paymentStatus(self):
      """Return the payment status."""
      return self._paymentStatus

  def get_Invoice(self):
      """Return the generated invoice."""
      return self._invoice

  def get_vatRate(self):
      """Return the VAT rate."""
      return self._vatRate

  # Setters
  def set_paymentDate(self, paymentDate):
      """Set the payment date."""
      self._paymentDate = paymentDate

  def set_finalAmount(self, finalAmount):
      """Set the final amount after VAT."""
      self._finalAmount = finalAmount

  def set_paymentMethod(self, paymentMethod):
      """Set the payment method."""
      self._paymentMethod = paymentMethod

  def set_paymentStatus(self, paymentStatus):
      """Set the payment status."""
      self._paymentStatus = paymentStatus

  def set_invoice(self, invoice):
      """Set the invoice string."""
      self._invoice = invoice

  def set_vatRate(self, vatRate):
      """Set the VAT rate."""
      self._vatRate = vatRate

  # Method to process the payment
  def processPayment(self):
      """Process the payment and return the final amount."""
      # In a real system, this would interact with a payment gateway
      # Here we just return the final amount as a placeholder.
      return self._finalAmount

#method to generate invoice
  def generateInvoice(self, order):
      """Generate the invoice based on the order details."""
      itemized_price = order.calculateTotal()
      vat_amount = round(itemized_price * self._vatRate, 2)  # Round VAT to 2 decimal places
      self._finalAmount = round(itemized_price + vat_amount, 2)  # Round final amount to 2 decimal places
      self._invoice = f"Invoice ID: {self._paymentID}, Amount: {self._finalAmount}, VAT: {vat_amount}, Status: {self._paymentStatus}"
      return self._invoice

  def __str__(self):
      """Returns a string representation of the Payment object."""
      return f"Payment ID: {self._paymentID}, Date: {self._paymentDate}, Method: {self._paymentMethod}, Status: {self._paymentStatus}"


class Customer:

  def __init__(self, customerID, name, contactInfo):
      self._customerID = customerID
      self._name = name
      self._contactInfo = contactInfo
      self.order = None  # Composition with Order: Customer contains an Order and None is inserted because at first, the customer has no order
      self.shopping_cart = Shoppingcart()  # Aggregation with Shoppingcart

#getters
  def get_customerID(self):
       """Return the customer ID."""
       return self._customerID

  def get_name(self):
      """Return the customer name."""
      return self._name

  def get_contactInfo(self):
       """Return the contact information of the customer."""
       return self._contactInfo

      # Setters
  def set_name(self, name):
      """Set the name of the customer."""
      self._name = name

  def set_contactInfo(self, contactInfo):
      """Set the contact information of the customer."""
      self._contactInfo = contactInfo

#method to create account
  def createAccount(self, name, contactInfo):
      """Creates a customer account."""
      self._name = name
      self._contactInfo = contactInfo
      return f"Account created for {self._name}."

#method to browse ebooks
  def browseEBooks(self):
      """Browse available e-books."""
      return "Browsing e-books..."

#method to purchase
  def purchaseEBook(self, order):
      """Customer purchases an eBook by creating an order and associating items."""
  # Customer directly creates an Order (composition)
      self.order = order  # Assuming the 'order' is already created (composition)
      # Add the eBook as an item to the Order (Order should handle adding items)
      self.order.set_items(self.shopping_cart.get_cartItems())  # 'order' here represents the actual eBook or item
      # Calculate total and return the result
      total_amount = self.order.calculateTotal()
      return total_amount

#method to check the invoice
  def checkInvoice(self, order):
      """Check invoice for a given order."""
      return order.get_invoice()


  def __str__(self):
      """Return a string representation of the Customer."""
      return f"Customer ID: {self._customerID}, Name: {self._name}, Contact Info: {self._contactInfo}"


class LoyaltyMembership(Customer):
  """This class extends Customer with loyalty membership benefits."""
  #initializes LoyaltyMembership attributes
  def __init__(self, customerID, name, contactInfo, loyaltyDiscount, membershipID):
      super().__init__(customerID, name, contactInfo) #inheritence
      self._loyaltyDiscount = loyaltyDiscount
      self._membershipID = membershipID

#setters and getters
  def get_loyaltyDiscount(self):
      return self._loyaltyDiscount

  def set_loyaltyDiscount(self, loyaltyDiscount):
      self._loyaltyDiscount = loyaltyDiscount

  def get_membershipID(self):
      return self._membershipID

#applies loyalty discount
  def applyloyaltyDiscount(self, order):
      return order.calculateTotal() * (self._loyaltyDiscount / 100)

#checks the status of the membership
  def checkMembershipStatus(self):
      return f"Membership ID: {self._membershipID}, Discount: {self._loyaltyDiscount}%"

  def bulk_discount(self, order):
      """Applies a bulk discount if the customer orders 5 or more e-books."""
      bulkDiscount = 0.0
      if len(order.get_items()) >= 5:  # If the customer orders 5 or more items
          bulkDiscount = 0.20  # 20% bulk discount for 5 or more items
      return bulkDiscount

  def calculate_total(self, order):
      """Calculates the final total for the order, including loyalty discount, bulk discount, and VAT."""
      # Get the  total from the order
      totalAmount = order.calculateTotal()
      # Apply the loyalty discount
      loyaltyDiscount = self.applyloyaltyDiscount(order)
      totalAmount -= loyaltyDiscount
      # Apply the bulk discount
      bulkDiscount = self.bulk_discount(order)
      totalAmount -= totalAmount * bulkDiscount
      # Access VAT rate from payment object
      vatRate = order.payment.get_vatRate()  # Use order.payment to get the vatRate
      vatAmount = totalAmount * vatRate
      totalAmount += vatAmount  # Add VAT to the total amount
      return totalAmount  # Return the final calculated amount after discounts and VAT

  def __str__(self):
       """Returns a string representation of the LoyaltyMembership."""
       return f"{super().__str__()}, Membership ID: {self._membershipID}, Loyalty Discount: {self._loyaltyDiscount}"




# Test Cases
def test_ebook_operations():
   # Add new e-books to the catalog
   title = input("Enter the title of the new eBook: ")
   ebook1 = EBook(title, "Mark Jacobs", "2020-10-13", "Fiction", 29.99)
   ebook2 = EBook("The Maze Runner", "Maria Sophie", "2018-09-18", "Non-Fiction", 49.99)
   print("Added eBooks:")
   print(ebook1)
   print(ebook2)


   # Modify an e-book's details
   ebook2.set_price(25.99)
   ebook2.set_title("The Maze Runner Updated")
   print("\nModified eBook:")
   print(ebook2)


   # Remove e-book
   del ebook1
   print("\neBook removed from catalog.")


def test_customer_account_management():
   # Add a new customer account
   customer = Customer(123, "Fatima Khaled", "Fatima@email.com")
   print("\nCreated Customer Account:")
   print(customer)


   # Modify customer account details
   customer.set_name("Fatima K.")
   customer.set_contactInfo("fatima.khaled@email.com")
   print("\nModified Customer Account:")
   print(customer)


   # Remove customer
   del customer
   print("\nCustomer account removed.")


def test_shopping_cart_operations():
   # Create a customer and add e-books to their shopping cart
   customer = Customer(123, "Fatima Khaled", "Fatima@email.com")
   ebook1 = EBook("intro to psychology", "Mark Jacobs", "2020-10-13", "Fiction", 25.99)
   ebook2 = EBook("The Maze Runner", "Maria Sophie", "2018-09-18", "Non-fiction", 49.99)


   cart = customer.shopping_cart
   cart.addItem(ebook1)
   cart.addItem(ebook2)
   print("\nShopping Cart After Adding Items:")
   print(cart)


   # Remove an item from the shopping cart
   cart.removeItem(ebook1)
   print("\nShopping Cart After Removing an Item:")
   print(cart)


def test_discounts_and_invoice_generation():
   # Create a loyalty member customer and an order
   loyalty_customer = LoyaltyMembership(456, "Mohammed Saeed", "mohammed@email.com", loyaltyDiscount=10, membershipID="AB002")
   order = Order(1, date.today(), paymentID="P0012")


   # Add e-books to the shopping cart and purchase them
   ebook1 = EBook("The housemaid", "Freida McFadden", "2018-01-02", "Fiction", 48.99)
   ebook2 = EBook("Atomic Habits", "James Clear", "2019-03-04", "Fiction", 48.99)
   ebook3 = EBook("Pillow thoughts", "Collen Hoover", "2020-05-06", "Fiction", 62.00)
   ebook4 = EBook("Diary of Wimpy Kids", "Jeff Kinney", "2021-07-08", "Non-Fiction", 54.99)
   ebook5 = EBook("The outsider", "Holly Jackson", "2020-09-10", "Fiction", 43.99)


   # Add items to the cart
   loyalty_customer.shopping_cart.addItem(ebook1)
   loyalty_customer.shopping_cart.addItem(ebook2)
   loyalty_customer.shopping_cart.addItem(ebook3)
   loyalty_customer.shopping_cart.addItem(ebook4)
   loyalty_customer.shopping_cart.addItem(ebook5)


   # Associate the shopping cart items with the order and calculate total with discounts
   loyalty_customer.purchaseEBook(order)
   total_with_discounts = loyalty_customer.calculate_total(order)
   print(f"\nTotal with Loyalty and Bulk Discounts: ${total_with_discounts:.2f}")


   # Generate the invoice
   payment = Payment("P1001", date.today(), "Credit Card")
   invoice = payment.generateInvoice(order)
   print("\nGenerated Invoice:")
   print(invoice)


# Run all test cases
test_ebook_operations()
test_customer_account_management()
test_shopping_cart_operations()
test_discounts_and_invoice_generation()

