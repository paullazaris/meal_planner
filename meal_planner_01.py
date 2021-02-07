import pyinputplus as pyip
import webbrowser


print('MEAL PLANNER')


print("""Hello! Welcome to So Fresh And Cuisine's Weekly Meal Planner!\n

It is very simple! All you have to do is enter your weekly budget for 6 dinners, 
and choose what types of cuisine you would like.\n
Let's get started!""")

budget = pyip.inputNum(prompt = "What is your budget for 6 dinners?")

print("Great! Let's find some meals for under $" + str(budget) + ' a week.')

cuisine = pyip.inputMenu(['American', 'Italian', 'Mexican', 'Asian', 'Middle Eastern'], prompt=("""Please choose your first recipe! (Enter a number)\n"""))

if cuisine == 'Italian':
    first_meal = pyip.inputMenu(['Chicken Parm', 'Spaghetti with Meatballs', 'Sausage with Peppers and Onions', 'italian_link4', 'italian_link5', 'italian_link6', 'italian_link7', 'italian_link8', 'italian_link9', 'italian_link10'], numbered = True, prompt=("Please choose your first recipe! (Enter a number:)"))
    if first_meal == "Chicken Parm" or 1:
        webbrowser.open('https://barefootcontessa.com/recipes/parmesan-chicken')
    
    elif first_meal == 'Spaghetti with Meatballs' or 2:
        webbrowser.open('https://www.foodnetwork.com/recipes/ina-garten/real-meatballs-and-spaghetti-recipe-1946027')

    elif first_meal == 'Sausages with Peppers and Onions' or 3:
        webbrowser.open("https://www.foodnetwork.com/recipes/giada-de-laurentiis/sausage-peppers-and-onions-recipe-1916837")
    





#if budget >= 60 and <= 90:
    #print('Great! Let\'s find you some meals to plan for under $60 a week. But first we need a little more information.')
    
    
#cuisine = pyip.inputMenu(['American', 'Italian', 'Mexican', 'Asian', 'Middle Eastern', prompt = 'What type of cuisine would you like to start with?'])
