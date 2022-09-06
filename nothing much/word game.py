def game(word):
    guesses = 5
    while guesses>0:
        x = 0
        answer = input("duma:")
        if answer == word and len(answer) == 5:
            print('you win')
            break
        elif answer != word and len(answer) == 5:
            try:
                for i in range(5):
                  if answer[x] == word[x] and x <= 4:
                       print(answer[x],end="")
                  elif answer[x] != word[x] and x <= 4:
                       print("_", end="")
                  x += 1
                guesses -= 1
                print(" "+ str(guesses))
            except:
                "nana"

game("heart")