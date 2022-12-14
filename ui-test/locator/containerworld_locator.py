# ContainerWorld首页的元素定位
class ContainerWorldMainLocator:
    # 首页的搜索 input 定位
    user_name = "username1"
    pass_word = "#userpassword1"
    user_name2 = "username2"
    pass_word2 = "#userpassword2"

    # login btn 定位
    login_btn = "logon_button"

    # dropdown list
    client_resources = "li:nth-child(6) > h1"
    menu_list = "menuList"
    online_tools = "Online Tools"

    pds = "//div[@id='accordion']/h3[3]"

    download_file = "//img[@name='download_file']"
    rust_wine_co = "//div[contains(text(),'RUST WINE CO')]"
    download_complete = "//html/body/center/h1[1]"
