# ContainerWorld首页的元素定位
class WineDirectLocator:
    # 首页的搜索 input 定位
    user_name = "username"
    pass_word = "password"

    # login btn 定位
    login_link = ".login.nav-link"
    login_btn = "btn-login"

    # dropdown list
    ecommerce = "Ecommerce"

    store = "//*[text()=' Store']"
    inventory_link = "//body/div[@id='subNavigation']/div[1]/ul[1]/li[3]/a[1]"
    next_link = "//*[contains(text(),'Next')]"
