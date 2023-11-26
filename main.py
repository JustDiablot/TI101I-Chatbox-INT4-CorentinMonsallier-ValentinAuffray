import functions
import features


speeches = './speeches-20231109'
cleaned = './cleaned'

functions.create_folder()
functions.create_file(functions.files_list(cleaned, '.txt'))
functions.copy_text(functions.files_list(cleaned, '.txt'))



def main():
    print('\t\tWhat do you want to do ? (Enter a number form 1 to 7)\n\n\n\t1 - Display the list of unimportant words\n\n\t2 - Display the list of the most important words\n\n\t3 - Indicate the list of most repeted words said by a chosen president\n\n\t4 - Indicate the president that used a chosen word and the one who repeted it the most\n\n\t5 - Display the first president that talked about the two chosen word\n\n\t6 - Display the list of all the important words that all of the president used\n\n\t7 - Exit\n\n\n\n\t\t\tYour choice : ')

    choice = int(input())
    while choice>7 and choice<1:
        choice = int(input())

    if choice == 1:
        print('The least important word(s) in the whole corpus of txt is(are) :', features.unimportant(functions.files_list(cleaned, '.txt')))

    elif choice == 2:
        print('The most important word(s) in the whole corpus of txt is(are) :', features.important(functions.files_list(cleaned, '.txt')))

    elif choice == 3:
        print('\tEnter the name of the president : Must be one of these names : Chirac, Giscard dEstaing, Hollande, Macron, Mitterrand, Sarkozy ')
        namelist = ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']
        pres_name = input().capitalize()
        while pres_name not in namelist:
            pres_name = input('\t\tMust be one of these names : Chirac, Giscard dEstaing, Hollande, Macron, Mitterrand, Sarkozy : ')
        print('The word(s) that have been the most used by', pres_name, ' is : ',features.most_repeat(functions.files_list(cleaned, '.txt'), pres_name))

    elif choice == 4:
        pass 
        print('\tEnter the word you want to look for : (a single word, without ponctuation)')
        research = input().lower()
        if len(features.unique_research(functions.files_list(cleaned, '.txt'), research)) > 1:
            print('The speeches that most talked about', research, 'are : ', features.unique_research(functions.files_list(cleaned, '.txt'), research), ' (they use the same amout of times the word', research, ')')
        else:        
            print('The speech that most talked about', research, 'is : ',  features.unique_research(functions.files_list(cleaned, '.txt'), research))
        print('Here is the list of all the one that talked of', research, ' : ', features.global_research(functions.files_list(cleaned, '.txt'), research))

    elif choice == 5:
        print('Enter the first word you want to look for (a single word, without ponctuation) : ')
        x = input().lower()
        print('Enter the second word you want to look for (a single word, without ponctuation) : ')
        y = input().lower()
        if features.multiple_research(x, y, functions.files_list(speeches, '.txt')) == 0:
            print('There is no president who talked about', x, 'and', y)
        else:
            print('The first president to talk about', x, 'and', y, 'is :', features.multiple_research(x, y, functions.files_list(speeches, '.txt')))
    elif choice == 6:
        print('The list of the word used in every speeches sont : ', features.all_in(functions.files_list(cleaned, '.txt')))

    elif choice == 7:
        print('GoodBye !')
        return

    else:
        print('error in the process\n')
        return


    question = 'p'
    while question != 'n' and question != 'y':
        question = input('Anything else ? (y/n)')
    if question == 'y':
        main()
    elif question == 'n':
        print('Bye')
        return
    else:
        print('error in the process\n')
    return


if __name__ == '__main__':
    print('\t\t\t\t\tWelcome into our first chatbot \n\n')
    main()
