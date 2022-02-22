import re
def to_camel_case(text):
    separate = re.split('_|-',text)
    camleCased = separate[0]
    for i in separate[1::]:
        camleCased +=i.capitalize()
    print (camleCased)


to_camel_case('abra-ka_dabra')

    