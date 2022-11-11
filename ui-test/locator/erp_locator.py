# 百度结果页的元素定位
class ErpLocator:
    # 首页的搜索 input 定位
    user_name = "login"
    pass_word = "password"

    # login btn 定位
    login_btn = "//button[@type='submit']"

    products = "//span[contains(text(),'Products')]"
    products_dropdown = "Products"

    create = "//span[contains(text(),'Create')]"
    product_name = "name"
    attributes_Variants = "// a[contains(text(), 'Attributes & Variants')]"
    add_line = "Add a line"
    attribute_box = "//tbody/tr[1]/td[1]/div[1]/div[1]/div[1]/input[1]"
    values_box = "//tbody/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/input[1]"





''