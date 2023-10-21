def pick_a_card(list_cards, card_number):
    mid = len(list_cards)//2
    first_pos = 0
    last_pos = len(list_cards)-1

    while first_pos <= last_pos:
        if list_cards[mid] > card_number:
            last_pos = mid
            new_cards = list_cards[first_pos,last_pos+1]
            if mid == card_number:
                return mid
          
        else:
            first_pos = mid
            list_cards = list_cards[first_pos,last_pos+1]
            if mid == card_number:
                return mid
           