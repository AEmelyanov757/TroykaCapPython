# библиотеки для работы с расширителем портов и работы со временем
import gpioexp, time

exp = gpioexp.gpioexp() # создаём объект для работы с расширителем портов 
pot = 0 # положение сервопривода начальное

while True:
    # меняем положение сервопривода на порте 0 каждые 5 секунд
    exp.analogWrite(0, pot)
    if pot < 255:
        pot = pot + 1
    else:
        pot = 0
    time.sleep(5)
