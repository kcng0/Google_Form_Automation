import automate_function
DRIVER_PATH = "chromedriver.exe"
auto_submit = automate_function.FormAutomate(DRIVER_PATH)


for i in range(10):
    auto_submit.open_browser("https://forms.gle/5z1NtErAioMQZDhd6")
    yes_button = auto_submit.get_button('//*[@id="i5"]/div[3]/div')
    no_button = auto_submit.get_button('//*[@id="i8"]/div[3]/div')
    submit_button = auto_submit.get_button('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    button_list = [no_button, 
                   submit_button]

    auto_submit.click_buttons(button_list)

# close the browser
auto_submit.browser.close()
    

