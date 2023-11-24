import json

def keyfind(json, key):
    if isinstance(json, dict):
        if key in json:
            return json[key]
        for dictionary_keys, element_dictionary in json.items():
            result = keyfind(element_dictionary, key)
            if result is not None:
                return result
 
json_code = '''
{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
'''

parsed_code = json.loads(json_code)

while True:
    found_key = input("Enter the key from json code: ")
    key_value = keyfind(parsed_code, found_key)
    if key_value is not None:
        print(f"Key value: '{found_key}': {key_value}")
    else:
        print("Key not found")