def convert_to_uah(amount, rate=41.5 ):
    return(amount*rate)
standart = convert_to_uah(100, 41.5)
other = convert_to_uah(100, 38.0)
print("курс 100$ за стандартним курсом:", standart, "грн")
print("курс 100$ за іншим курсом:", other, "грн")


