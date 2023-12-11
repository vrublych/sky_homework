def word_upper(string):
    """
    принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return string.upper()

def my_function(string):
    """
    принимает на вход строку,
    которая делает заглавными первые буквы
    каждого слова в строке
    """
    result = ""
    for word in string.split():
        result += word.capitalize() + " "
    return result
