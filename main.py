import random
from replit import clear
import art

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  '''Takes in a list of cards and returns the sum of those cards.'''
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw."
  elif computer_score == 0:
    return "You lose."
  elif user_score == 0:
    return "You won!"
  elif user_score > 21:
    return "You lose."
  elif computer_score > 21:
    return "You won!"
  elif user_score > computer_score:
    return "You won!"
  else:
    return "You lose."

def play_blackjack():
  print(art.logo)

  user_cards = []
  computer_cards = []
  game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while game_over == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}. Your current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      hit_stay = input("Do you want another card? Type 'y' or 'n': ")
      if hit_stay.lower() == 'y':
        user_cards.append(deal_card())
        user_score = sum(user_cards)
        game_over = False
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
  print(f"Your final cards are: {user_cards}. Your final score is: {user_score}")
  print(f"Computer's final cards are: {computer_cards}. Their score is {computer_score}")
  print(compare(user_score, computer_score))

while input("Would you like to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
  clear()
  play_blackjack()
