message = input('>')


def convert_emoji(text):
    words = text.split(' ')
    output = ''
    emojis = {
        ":)": '😊',
        ':(': '😔'
    }
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


print(convert_emoji(message))
