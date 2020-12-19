from selenium import webdriver

DRIVER = None
CALC_BUTTONS = None
SYMBOL_TO_INDEX = {'AC': 0, '%': 2, '/': 3,
                   '7': 4, '8': 5, '9': 6,
                   '*': 7, '4': 8, '5': 9,
                   '6': 10, '-': 11, '1': 12,
                   '2': 13, '3': 14, '+': 15,
                   '0': 16, '.': 17, '=': 18}


def initiate_browser(url):
    local_driver = webdriver.Chrome()
    local_driver.get(url)
    return local_driver


def validate_and_execute(expr):
    if expr == 'exit':
        return None
    CALC_BUTTONS[SYMBOL_TO_INDEX['AC']].click()

    # break down the expression into characters/symbols
    for symbol in expr:
        # if symbol is a space, skip
        if symbol == ' ':
            continue

        # get the button element index for a symbol in the expression
        btn_index = SYMBOL_TO_INDEX.get(symbol, None)

        # if there's no index available for entered symbol, return
        if not btn_index:
            print('\tInvalid expression')
            return None

        # click on the mapped element
        CALC_BUTTONS[btn_index].click()

    # evaluate the expression
    CALC_BUTTONS[SYMBOL_TO_INDEX['=']].click()

    # return the evaluated answer
    answer = DRIVER.find_element_by_css_selector(
        'div.component-display div').text
    return answer


def program_loop():
    print("\n\n\n\n\n")
    print("Keep entering mathematical expressions to solve or type 'exit' to terminate.")
    print("Some examples of expressions:")
    print("\t12+15")
    print("\t42-5")
    print("\t5*5")
    print("\t25/5")
    print("\n\n")
    expr = ""
    while(expr != 'exit'):
        expr = input("Enter expression or type 'exit':")
        answer = validate_and_execute(expr)
        if answer:
            print(f"{expr}={answer}")


def main():
    global DRIVER
    global CALC_BUTTONS

    DRIVER = initiate_browser("https://ahfarmer.github.io/calculator/")
    CALC_BUTTONS = DRIVER.find_elements_by_css_selector(
        "div.component-button button")

    program_loop()
    DRIVER.quit()


if __name__ == "__main__":
    main()
