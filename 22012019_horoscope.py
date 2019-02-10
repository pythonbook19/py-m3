import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# import random
# course_by = "skillfactory"
# i = 0
# while i < 12:
#     index = random.randrange(0, len(course_by))
#     print(course_by[index])
#     i = i + 1


# # Для начала мы попробуем сгенерировать
#  просто несколько предложений по шаблону
#  «Время суток», «глагол-действие и интрига», «размытое обещание».

# import random
# times = ['Утром',
#             'Днем',
#             'Ровно в полдень',
#             'При наступлении сумерек',
#             'Вечером',
#             'Ночью']
# action = ['будьте осторожны с огнем',
#             'купите лотерейеый билет',
#             'сходите в кино',
#              'задумайтесь о вселенной',
#              'ложитесь спать',
#              'испеките хлеб',
#              'закажите пиццу']
#
#
# t = random.randrange(0, len(times))
# a = random.randrange(0, len(action))
# print(times[t], action[a] )
#
import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном", "на закате", "на рассвете", "в полночь", "посреди ночи"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для", "оглядитесь в поисках", "постарайтесь избежать", "будьте готовы для"]
promises = ["книг на финском языке", "встреч со старыми знакомыми", "мистического вызова судьбы", " сеанса гипноза", "необычайного события"]

generated_prophecies = []
i = 0
while i < 2:
    j = 0
    forecast = []
    while j < 3:
        ti = random.randrange(j, len(times))
        ai = random.randrange(0, len(advices))
        pi = random.randrange(j, len(promises))

        t = times[ti]
        a = advices[ai]
        p = promises[pi]
        full_sentence = t.title() + " " + a + " " + p + "."

        forecast.append(full_sentence)

        j = j + 1

    generated_prophecies.append(forecast[0] + " " + forecast[1] + " " + forecast[2])

    i = i + 1
print('%s' % ''.join(generated_prophecies))
