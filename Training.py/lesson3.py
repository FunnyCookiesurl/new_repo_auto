from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card("1234 5678 9876 5432", "12/26", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)
