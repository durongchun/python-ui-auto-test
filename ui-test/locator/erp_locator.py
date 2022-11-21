# 百度结果页的元素定位
class ErpLocator:
    # 首页的搜索 input 定位
    user_name = "login"
    pass_word = "password"

    # login btn 定位
    login_btn = "//button[@type='submit']"
    inventory_app = "//div[text()='Inventory']"

    # ----------------------create product pages--------------------------------------------

    products = ".o-dropdown--no-caret:nth-child(3) button.dropdown-toggle > span:nth-child(1)"
    products_dropdown = "//a[contains(text(),'Products')]"

    create = "//span[contains(text(),'Create')]"
    product_name = "name"
    rfid_number = "rfid_number"
    barcode = "barcode"
    save_button = "//span[contains(text(),'Save')]"

    update_quantity = "action_update_quantity_on_hand"
    create_qty = "//button[contains(text(),'Create')]"

    location_box = "div.o_field_widget.o_field_many2one.o_quick_editable.o_with_button.o_required_modifier"
    location_search_box = ".o_searchview_quick div.o_searchview_input_container > input.o_searchview_input"
    location_search_result = "tr.o_data_row.text-danger:nth-child(1)"
    counted_qty = "//input[contains(@class,'o_quick_editable o_input')]"
    save_record_button = "//button[contains(text(),'Save')]"

    apply_button = "//td[@name='inventory_diff_quantity']/following-sibling::td//span[text()='Apply']"

    attributes_Variants = "//a[contains(text(), 'Attributes & Variants')]"

    add_line = "//tbody/tr[1]/td[1]/a[1]"
    attribute_box = "//tbody/tr[1]/td[1]/div[1]/div[1]/div[1]/input[1]"
    vintage = "//ul[contains(@class, 'ui-menu ui-widget ui-widget-content')]//li[5]//a"
    values_box = "//tbody/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    values2_box = "//tbody/tr[1]/td[2]/div[1]/div[2]/div[1]/div[1]/input[1]"

    edit_variant_button = "//span[contains(text(),'Edit')]"

    internal_reference_box = "//input[@name='default_code']"
    barcode_box = "//input[contains(@name, 'barcode') and contains(@class,'o_quick_editable o_input') ]"

    variants = ".o_form_sheet div.oe_button_box.o_full:nth-child(1) > button.btn.oe_stat_button:nth-child(2)"

    variant_value = ".o_field_widget.o_readonly_modifier > div.badge.badge-pill.o_tag_color_0"

    warning = ".oe_edit_only.oe_grey"
    action = ".btn.btn-secondary.o-no-caret.d-flex.align-items-center"
    delete = "li.o_menu_item:nth-child(3) > a.dropdown-item"
    ok_confirm = "//span[contains(text(),'Ok')]"
    products_details = ".o_image_64_contain"

    products_input = ".o_searchview_input"
    no_products_show = ".o_view_nocontent_smiling_face"
    vintage_options = "//ul[@id='ui-id-58']/li"
    attribute_dropdown_options = "//ul[contains(@class,'ui-autocomplete dropdown-menu ui-front')]//li//a"
    vintage_dropdown_options = "//ul[contains(@class,'ui-autocomplete dropdown-menu ui-front')]//li//a[1]"
    year_select_button = "button.btn.btn-primary.o_select_button"
    check_boxes = "//tr/td[1]/div[@class='custom-control custom-checkbox'][1]"
    year_options = "//td[contains(@class, 'o_data_cell o_field_cell o_list_char o_required_modifier')]"

    product_breadcrumb = "li.breadcrumb-item.o_back_button:nth-child(2) > a:nth-child(1)"
    qty_on_hand = "//div[@name='qty_available']//span[@class='o_stat_value']"

    # vintage_values = "//span[contains(@title, {})]"
    vintage_values = "//tr[@class='o_data_row']//span[contains(text(), 'Vintage')]"
    vintage_update_quantity = ".btn.btn-secondary:nth-child(2) > span:nth-child(1)"
    vintage_qty_on_hand = "//span[contains(text(), 'Vintage: {}')]/../../../../" \
                          "following-sibling::td[@name='qty_available']"

    # -------------------------transfer pages ------------------------------------
    operations_menu = "//span[contains(text(),'Operations')]"
    transfer_dropdown_option = "//a[contains(text(),'Transfers')]"
    operation_type = "tr:nth-child(2) td:nth-child(2) > div.o_field_widget.o_field_many2one"
    source_location = "tr:nth-child(3) td:nth-child(2) > div.o_field_widget.o_field_many2one"
    destination_location = "tr:nth-child(5) td:nth-child(2) > div.o_field_widget.o_field_many2one"
    operation_type_dropdown_options = "//ul[contains(@class,'ui-autocomplete dropdown-menu ui-front')]//li//a"

