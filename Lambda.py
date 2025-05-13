#Elements! They combine and change into compounds!
#this_sa_list = [1,2,3]#example
#this_sa_list.append('Molecules!') #instead of using plus , you can use append. Remember it as attend, because thats your favorited word
#this_sa_list[0] = 0 #manipulating inside the list
#this_sa_list.insert(3, 'electrons') #The structure is simple , the first argument is where you will add it inside the list. Count it up. Second arguement is what you add into it.
#this_sa_list.pop() #Pop automatically pops the last value of your list. Very simplicity
#print(this_sa_list)
#Now you get comfortable about making even more functions from now on.
def add_expense(expenses , sum , pigeonhole ):
    expenses.append({'sum':sum , 'pigeonhole': pigeonhole}) # Inside the () is 2 dictionaries that is new learned , it is a built in data type of key value pairs.
def print_expenses(expenses):
    for expensive in expenses:
        #print(f'Sum : {sum} , Pigeonhole: {pigeonhole}' )
        print(f'Sum: {expensive["sum"]} , pigeonhole: {expensive["pigeonhole"]}')  #I only can explain this by giving an example : Dictionary['amount'] is equivalent to dictionary = {'amount' : 50}  
#In Python, an important thing to know is that the same type of quote used to define a string cannot be used inside it. For example, the string 'I'm a string!' is not valid. To use the single quote inside that string you should either
def total_expenses(expenses):
    #test = lambda x: x * 2 #Learn lambda. Seriously.
    #print(list(map(test , [2,3,5,8]))) #THis is a vary.
    #print(sum(map(test, [2,3,5,8])))
    return sum(map(lambda expensive: expensive['sum'], expenses)) #this will obtain the total of expenses. Make sure to return it. I didnt return. You have to. LMAO
def filter_expenses_by_pigeonhole(expenses , pigeonhole):
#The filter() function allows you to select items from an iterable, such as a list, based on the output of a function:
#Example Code
#filter(my_function, my_list)
#filter() takes a function as its first argument and an iterable as its second argument. It returns an iterator, which is a special object that enables you to iterate over the elements of a collection, like a list.
    return filter(lambda expensive: expensive['pigeonhole'] == pigeonhole , expenses) #The filter() function allows you to select items from an iterable, such as a list, based on the output of a function
#filter() takes a function as its first argument and an iterable as its second argument. It returns an iterator, which is a special object that enables you to iterate over the elements of a collection, like a list.
#The results of example above is iterator contains element of expenses for whiuch my pigeonhole returns true
def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by pigeonhole')
        print('5. Exit')
        choice = input('Enter Your Choice: ')
    #This will be confusing if you are not prone to python knowledges. Print('1. add an expense') is equivalent to only the number '1' when put into if. The print command is merely a text. WHen you want to execute it , follow its ordinal number      
        if choice == '1':
            amount = float(input('Enter amount: '))
            pigeonhole = input('Enter pigeonhole: ')
            add_expense(expenses, amount, pigeonhole)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
        
        elif choice == '4':
            pigeonhole = input('Enter pigeonhole to filter: ')
            print(f'\nExpenses for {pigeonhole}:')
            expenses_from_pigeonhole = filter_expenses_by_pigeonhole(expenses, pigeonhole)
            print_expenses(expenses_from_pigeonhole)
        
        elif choice == '5':
            print('Exiting the program.')
            break
main()