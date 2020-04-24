# Refactored Fill-in-the-Blank Quiz

## Summary

Adding a prior Udacity project to my portfolio, but refactored it first.

## Methodology
This program was a quiz I created when I was taking my Intro to Programming classes at Udacity in 2017. I wanted to include it in my portfolio so I decided to go through the process of refactoring code and brining it in more line with PEP8 standards. The code was originally entered using Python 2.7, so I also had to go through and bring it up to Python 3 standards.

This was also a gauge for me to see how far I have come in my programming skills, and I was pleasantly surprised. When I first started I remember how hard it was for me to grasp the concept of inheritance and I remember that trying to do a dictionary was impossible. I remember using the error messages as a guide to force my way in making my code work. This time around I found myself being more intuitive to the process. For instance when I looked at the if statements below my first thought was, this needs a dictionary. I wrote out a dictionary initially putting the key and value pair in parentheses, but it didn't look right, so I searched to see how I could refine it, and discovered that I needed to do is put the values in the parentheses.  

The result was going from:

```
def difficulty_level():
    level = input(
    r'Please select the level of difficulty of easy, medium or hard: ')
    if level.lower() == 'easy':
        return easy_question, easy_answer
    elif level.lower() == 'medium':
        return medium_question, medium_answer
    elif level.lower() == 'hard':
        return difficult_question, difficult_answer
    else:
        print (
        'Please type easy, medium or hard\n')
        difficulty_level()
```

To:

```
def difficulty_level():
    level = input(
    r'Please select the level of difficulty of easy, medium or hard: ')
    level = level.lower()
    if level in level_of_difficulty_dictionary:
        return level_of_difficulty_dictionary[level]
    else:
        print ('Please type easy, medium or hard\n')
        difficulty_level()
```

I also standardized the input by adding *.lower()* to make sure it matched on all the cases. I also made it more user friendly by giving the option to terminate rather than just continuing.

I had a lot of nested *IF* statements that I had to refactor into more efficient code. So what I did was took the code from:

```
while blank_space < len(blank_index):            
      if turns > 0:
          current_blank = blank_index[blank_space]
          user_answer = input("Please fill in {}: ".format(current_blank))
          if user_answer == fill_in_blank_answer[blank_space]:
              print ("Correct! It is {}".format(user_answer))
              blank_space+=1
          else:
              print ("Incorrect. Please try again.\n")
              turns-=1
      else:
          print ('''
          You have run out of turns!
          You completed {0} questions in {1} turn(s).'''.format(blank_index,
              turns))
          continue_question()

  else:
      (blank_space > len(blank_index)) and (turns > 0):
      print ('''
      Congratulations!!!
      You have successfully completed the quiz!
      ''')
```

To...

```
while turns > 0 and blank_space < number_of_questions:
      current_blank = blank_index[blank_space]
      user_answer = input("Please fill in {}: ".format(current_blank))

      if user_answer == fill_in_blank_answer[blank_space]:
          print ("Correct! It is {}".format(user_answer))
          blank_space+=1
      else:
          print ("Incorrect. Please try again.\n")
          turns-=1
  else:
      outcome(blank_space)

def outcome(blank_space):
  if blank_space == number_of_questions:
      print ('Congratulations!!!')
      print(' You have successfully completed the quiz!')
  else:
      print ('You have run out of turns!')
      print('You completed {0} questions in {1} turn(s).'.format(blank_index,
          turns))
      continue_question()
```

As you can see I created another function to go from three conditional statements in a function to two.


## Reference
https://github.com/kristendavis/fill-in-blanks-quiz/blob/master/fill-in-the-blanks.py,
https://github.com/LaLaLottie/fillintheblanksgame/blob/master/fill-in-the-blanks.py
