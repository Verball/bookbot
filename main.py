def sort_on(dict):
    return dict["count"]
def main():
    res = {}
    res_list = []
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            for letter in word.lower():
                if letter.isalpha():
                    if letter not in res:
                        res[letter] = 0
                    res[letter] +=1
        for key in res:
            res_list.append({"character": key, "count": res[key]})
        res_list.sort(reverse = True, key = sort_on)
        print(res_list)
        print("--- Begin report of books/franenstein.txt---")
        print(f"{len(words)} words found in the document")
        for small_dictionary in res_list:
            #print(f"{small_dictionary['character']}")
            print(f"The '{small_dictionary['character']}' character was found {small_dictionary['count']} times")
        print("---End Report---")
            
main()