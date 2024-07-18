for item in element:
    if len(element[item:0])>2 and str(element[item])isinstance(element[item], str):

if len(element)>2 and isinstance(element[0], str):



>>> ["foo", "bar", "baz"].index("bar")


float(element[((element.index(item))+1)].strip(' '))