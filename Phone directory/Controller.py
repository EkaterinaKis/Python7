import View
import Model
import Logger


def run():
    turn = View.choose()
    if turn == '1':
        contact = View.new()
        Logger.add_new(contact)
    if turn == '2':
        contact = View.what_to_search()
        data = Logger.get_contact()
        result = Model.search_contact(data, contact)
        View.show_result(result)
