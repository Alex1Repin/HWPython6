
import zlib
# создадим массив данных
text = 'Почему оно не работает?'
data = []
#for i in range(10):
#     data.append(text *20)
lst = map(lambda data : data.append(text * 20), range (10))
# преобразование текста в байты
byte_data =  '\n\n'.join(data).encode('utf-8')
# сжимаем данные
compress = zlib.compress(byte_data, level=-1)
print(compress)

# распаковываем сжатые 'compress' из буфера
decompress = zlib.decompress(compress)
# преобразуем байты в текст
text = decompress.decode('utf-8')
# выведем на печать первые 22 символа
print(text[0:22])
# 'Всё равно не работает'

