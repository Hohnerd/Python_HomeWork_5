# Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. 
# Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

text = 'сушёнабвый Все проходятабв это глупости, мой тщатабвельный мальчик, забвение — говорил Миклухо-Маклай, \
           задумчиво самозабвенно ковыряя улетучабвиваются  дырку на абвисключительно колене'

def delWords(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = delWords(text)
print(text)

