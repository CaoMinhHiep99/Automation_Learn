from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SetupDropdown:
    def __init__(self) -> None:
        # Initialize browser and open page
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get('https://the-internet.herokuapp.com/dropdown')
        # Find the dropdown element and create a Select object
        dropdown_element = self.browser.find_element(By.XPATH, "//select[@id='dropdown']")
        self.select = Select(dropdown_element)


    def select_and_check_option(
            self,
            xpath,
            text: int = None,
            index: int = None,
            value: str = None
            ):
        """
        """
        try:
            # Select the value by Visible Text
            if text:
                self.select.select_by_visible_text(text)
            # Select the value by Index
            elif index:
                self.select.select_by_index(index)
            # Select the value by Value
            elif value:
                self.select.select_by_value(value)
            # Check the value selected after select the option
            check_sellect = self.browser.find_element(By.XPATH, f"//option[@value='{xpath}']")
            if check_sellect.is_selected():
                print(f"the Option {xpath} is selected")
            else:
                raise Exception(f"Can not to select the Option {xpath}")    
        except Exception as ex:
            print(f"Error: {str(ex)}")


if __name__ == "__main__":
    # Create instance of class
    dropdown_test = SetupDropdown()

    # Call method to select option 1 (by text)
    dropdown_test.select_and_check_option(1, text="Option 1")

    # Call method to select option 2 (by index)
    dropdown_test.select_and_check_option(2, index=2)

    dropdown_test.select_and_check_option(2, value="2")