import sys, getopt

try:
    from apiclient.discovery import build
except ImportError:
    print("No module named 'apiclient.discovery' found")


def create_dict(query, length = 10):
    items = []
    _dict = {}
    api_key = "AIzaSyBHwpXkAjLDdcmDxkxCFnRUcEGsyAXCcr8"
    search_engine_id = '55cb869d93d02a2cc'
    resource = build("customsearch", 'v1', developerKey=api_key).cse()
    for i in range(1, length, 10):
        result = resource.list(q=query, cx=search_engine_id, start=i).execute()
        items += result['items']
    for item in items:
        if len(_dict) < length:
            _dict[item['title']] = item['link']
    return _dict


def display_dict(_table):
    for record in _table:
        print(record, ":", _table.get(record))


def main(argv):
    query = ''
    length = ''
    try:
        opts, args = getopt.getopt(argv, "hq:l:", ["query=", "length="])
    except getopt.GetoptError:
        print('test.py -q <query> -l <length>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -q <query> -l <length>')
            sys.exit()
        elif opt in ("-q", "--query"):
            query = arg
        elif opt in ("-l", "--length"):
            try:
                length = int(arg)
            except ValueError:
                print('Value that was set is not a number')
            except TypeError:
                print('Value should be integer')
            except:
                print('Ups, something wrong...')

    if query == '':
        print('Query parameter should be set!')
        sys.exit(2)

    print('Your Query:', query)
    print('Length of dictionary:', length)
    if length == '':
        _dict = create_dict(query)
    else:
        _dict = create_dict(query, length)

    display_dict(_dict)
    print(len(_dict))


main(sys.argv[1:])


