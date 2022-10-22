import automate_function
import random
DRIVER_PATH = "chromedriver.exe"
auto_submit = automate_function.FormAutomate(DRIVER_PATH)

# E.G.
# for i in range(10):
#     # Page 1
#     auto_submit.open_browser("Your google form link here.")
#     yes_button = auto_submit.get_button('//*[@id="i5"]/div[3]/div')
#     no_button = auto_submit.get_button('//*[@id="i8"]/div[3]/div')
#     next_button = auto_submit.get_button('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
#     button_list = []
#     if random.randint(0, 1) == 0:
#         button_list = [yes_button,
#                        next_button]
#     else:
#         button_list = [no_button,
#                        next_button]

#     auto_submit.click_buttons(button_list)
    
#     # Page 2
    
#     textbox = auto_submit.get_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     textbox.send_keys("Hello World" + str(random.randint(1, 10)))
    
#     submit_button = auto_submit.get_button('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    
#     button_list = [submit_button]
    
#     auto_submit.click_buttons(button_list)

# close the browser
auto_submit.browser.close()

