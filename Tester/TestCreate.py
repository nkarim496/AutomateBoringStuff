# тест на знание столиц штатов США
# скрипт создает 35 тестов по 50 вопросов с четырьмя вариантами ответов
# к каждому тесту прилагается файл с ответами

import random

capitals = {'Alabama': 'Montgomery',
 'Alaska': 'Juneau',
 'Arizona': 'Phoenix',
 'Arkansas': 'Little Rock',
 'California': 'Sacramento',
 'Colorado': 'Denver',
 'Connecticut': 'Hartford',
 'Delaware': 'Dover',
 'Florida': 'Tallahassee',
 'Georgia': 'Atlanta',
 'Hawaii': 'Honolulu',
 'Idaho': 'Boise',
 'Illinois': 'Springfield',
 'Indiana': 'Indianapolis',
 'Iowa': 'Des Moines',
 'Kansas': 'Topeka',
 'Kentucky': 'Frankfort',
 'Louisiana': 'Baton Rouge',
 'Maine': 'Augusta',
 'Maryland': 'Annapolis',
 'Massachusetts': 'Boston',
 'Michigan': 'Lansing',
 'Minnesota': 'Saint Paul',
 'Mississippi': 'Jackson',
 'Missouri': 'Jefferson City',
 'Montana': 'Helena',
 'Nebraska': 'Lincoln',
 'Nevada': 'Carson City',
 'New Hampshire': 'Concord',
 'New Jersey': 'Trenton',
 'New Mexico': 'Santa Fe',
 'New York': 'Albany',
 'North Carolina': 'Raleigh',
 'North Dakota': 'Bismarck',
 'Ohio': 'Columbus',
 'Oklahoma': 'Oklahoma City',
 'Oregon': 'Salem',
 'Pennsylvania': 'Harrisburg',
 'Rhode Island': 'Providence',
 'South Carolina': 'Columbia',
 'South Dakota': 'Pierre',
 'Tennessee': 'Nashville',
 'Texas': 'Austin',
 'Utah': 'Salt Lake City',
 'Vermont': 'Montpelier',
 'Virginia': 'Richmond',
 'Washington': 'Olympia',
 'West Virginia': 'Charleston',
 'Wisconsin': 'Madison',
 'Wyoming': 'Cheyenne'}

# начинаем цикл в диапазоне 35 ( можно установить по желанию )
for testNum in range(35):
    
    # создаем файл теста и файл ответов
    testFile = open('test_%s.txt' % (testNum + 1), 'w', encoding='utf-8')
    answersFile = open('test_%s_answers.txt' % (testNum + 1), 'w', encoding='utf-8')
    
    # для каждого теста создаем загаловок и поля для ФИО студента
    testFile.write('Тест №' + str(testNum + 1) + '\n\n')
    testFile.write(' ' * 2 + 'Имя:\n')
    testFile.write(' ' * 2 + 'Фамилия:\n\n')
    
    # создаем лист штатов в рандомном порядке
    states = list(capitals.keys())
    random.shuffle(states)
    
    # write down to file questions with four choices
    for stateNum in range(50):
        testFile.write('%d. What is a capital of %s?\n' % (stateNum + 1, states[stateNum]))

        # записываем варианты ответов:
        # отбираем правильный ответ
        correct = capitals[states[stateNum]]

        # create list of answers
        answers = list(capitals.values())

        # delete correct answer from possible answers
        answers.remove(correct)

        # create list of four possible choices
        choices = random.sample(answers, 3)
        choices.append(correct)
        random.shuffle(choices)

        # write down choices
        for choiceNum in range(4):
            testFile.write("  %s. %s\n" % ("ABCD"[choiceNum], choices[choiceNum]))
        testFile.write("\n")

        # write correct choice in answers file
        answersFile.write("%d. %s\n" % (stateNum + 1, "ABCD"[choices.index(correct)]))

    # закрываем файлы
    testFile.close()
    answersFile.close()

    # completing status
    print("%d. Test is done." % (testNum + 1))

# The end.
