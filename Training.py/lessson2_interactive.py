rate_as_str = input("Оцените работу оператора от 1 до 5:") #str
rate = int(rate_as_str) #int

if (rate < 1):
    rate = 1

if (rate > 5):
    rate = 5

feedback = ''

if rate == 1:
    feedback = input("расскажите, что нам улучшить:")
elif rate == 2:
    feedback = input("расскажите, что вас смутило:")
elif rate == 3:
    feedback = input("можно и лучше:")
elif rate == 4:
    feedback = input("почти то самое:")
elif rate == 5:
    feedback = input("то, что надо:")
else:
    feedback = input("расскажите, за что похвалить оператора:")

print(feedback)