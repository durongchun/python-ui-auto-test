# 百度结果页的元素定位
class ErpLocator:
    # 首页的搜索 input 定位
    user_name = "username"
    pass_word = "password"

    # login btn 定位
    login_btn = "//button[@type='submit']"

    # dropdown list
    ecommerce = "Ecommerce"

    store = "//*[text()=' Store']"
    inventory_link = "//body/div[@id='subNavigation']/div[1]/ul[1]/li[3]/a[1]"
    next_link = "//*[contains(text(),'Next')]"

    client_resources = "li:nth-child(6) > h1"
    online_tools = "Online Tools"

