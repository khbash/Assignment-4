def merge_guest_list(*lists):
    result = []

    for list in lists:
        for el in list:
            if el not in result:
                result.append(el)

    result.sort()
    return result

telegram = ["Kai", "Pavlo", "Irina", "Sonya"]
snapchat = ["Karuna", "Irina", "Alina", "Kai"]
print(merge_guest_list(telegram, snapchat))

instagram = ["Kai", "Pavlo", "Stas", "Jamala"]
youtube = ["Karuna", "Stas", "Alina", "Kai"]
print(merge_guest_list(instagram, youtube))


discord = ["Helen", "Vitaliy", "Irina", "Antonina"]
viber = ["Helen", "Irina", "Alina", "Vitaliy"]
print(merge_guest_list(discord, viber))