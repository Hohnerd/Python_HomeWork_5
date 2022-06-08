# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
#  Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами. 
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
#  Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С помощью reduce сложите получившиеся числа и верните из функции 
# в качестве ответа.


languages = ['JavaScript','C#','Python','PHP','TypeScript','Kotlin','Swift','C++','Go','Ruby','Dart']
ids = list(range(1,len(languages)+1))

def list_of_tuples(ids,languages):
      return list(zip(ids,languages))

def filter_of_tuples(ids,languages):
    summ=[(sum([ord(i[r]) for r in range(0,len(i))])) for i in languages]
    summ=[(summ[i],languages[i]) for i in range(len(ids)) if summ[i]%ids[i] == 0]
    return summ

print(list_of_tuples(ids,languages))
print(filter_of_tuples(ids,languages))
