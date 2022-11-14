# 百度结果页的元素定位
class ErpLocator:
    # 首页的搜索 input 定位
    user_name = "login"
    pass_word = "password"

    # login btn 定位
    login_btn = "//button[@type='submit']"
    inventory_app = "//div[text()='Inventory']"

    products = "//span[contains(text(),'Products')]"
    products_dropdown = "//a[contains(text(),'Products')]"

    create = "//span[contains(text(),'Create')]"
    product_name = "name"
    rfid_number = "rfid_number"
    save_button = "//span[contains(text(),'Save')]"

    update_quantity = "action_update_quantity_on_hand"
    create_qty = "//button[contains(text(),'Create')]"

    location_box = "//input[contains(@class,'ui-autocomplete-input') and contains(@xpath,'1')] "
    counted_qty = "//input[contains(@class,'o_quick_editable o_input')] "
    save_record_button = "//button[contains(text(),'Save')]"

    apply_button = "//span[text()='Apply' and contains(@xpath, '2')]"

    attributes_Variants = "//a[contains(text(), 'Attributes & Variants')]"

    add_line = "//tbody/tr[1]/td[1]/a[1]"
    attribute_box = "//tbody/tr[1]/td[1]/div[1]/div[1]/div[1]/input[1]"
    vintage = "//ul[contains(@class, 'ui-menu ui-widget ui-widget-content')]//li[5]//a"
    values_box = "//tbody/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    values2_box = "//tbody/tr[1]/td[2]/div[1]/div[2]/div[1]/div[1]/input[1]"

    edit_variant_button = "//span[contains(text(),'Edit')]"

    internal_reference_box = "//input[@name='default_code']"
    barcode_box = "//input[contains(@name, 'barcode') and contains(@class,'o_quick_editable o_input') ]"

    variants = "// span[contains(text(), 'Variants')]"

    variant_value = "//span[contains(text(),'Vintage: {}')]"

    warning = ".oe_edit_only.oe_grey"
    action = ".btn.btn-secondary.o-no-caret.d-flex.align-items-center"
    delete = "li.o_menu_item:nth-child(3) > a.dropdown-item"
    ok_confirm = "//span[contains(text(),'Ok')]"
    products = ".oe_kanban_details"


''
