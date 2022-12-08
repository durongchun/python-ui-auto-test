# 百度结果页的元素定位
class ErpLocator:
    # 首页的搜索 input 定位
    user_name = "login"
    pass_word = "password"

    # login btn 定位
    login_btn = "//button[@type='submit']"
    inventory_app = "//div[text()='Inventory']"

    # ----------------------create product pages--------------------------------------------
    products = "//span[contains(text(),'Products')]"
    products_dropdown = "//a[contains(text(),'Products')]"

    create = "//button[@title='Create record']"
    product_name = "name"
    rfid_number = "rfid_number"
    barcode = "barcode"
    save_button = "div.o_form_buttons_edit > button.btn.btn-primary.o_form_button_save:nth-child(1)"

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
    action = "//button[@data-original-title='Additional actions']"
    delete = "li.o_menu_item:nth-child(3) > a.dropdown-item"
    ok_confirm = "//button[@class='btn btn-primary']"
    products_details = ".o_kanban_record.oe_kanban_global_click.oe_kanban_card"
    search_result = "//div[@class='o_content']//span[contains(text(),'{}')]/../../../.."

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
    vintage_qty_on_hand = "//span[contains(text(), '{}')]/../../../../" \
                          "following-sibling::td[@name='qty_available']"
    product_item = "div.oe_kanban_card.oe_kanban_global_click.o_kanban_record:nth-child(1) > div.oe_kanban_details"

    # -------------------------transfer pages ------------------------------------
    operations_menu = "//span[contains(text(),'Operations')]"
    transfer_dropdown_option = "//a[contains(text(),'Transfers')]"
    deliver_address = "tr:nth-child(1) td:nth-child(2) > div.o_field_widget.o_field_many2one"
    operation_type = "tr:nth-child(2) td:nth-child(2) > div.o_field_widget.o_field_many2one"
    operation_type_search_result = "//td[contains(text(), '{}')]/..//*[contains(text(), '{}')]"
    source_location = "tr:nth-child(3) td:nth-child(2) > div.o_field_widget.o_field_many2one"
    destination_location = "tr:nth-child(5) td:nth-child(2) > div.o_field_widget.o_field_many2one"
    deliver_address_dropdown_options = "//ul[contains(@class,'ui-menu ui-widget ui-widget-content')][1]//li//a"
    operation_type_dropdown_options = "//ul[contains(@class,'ui-autocomplete dropdown-menu ui-front')]//li//a"
    source_location_dropdown_options = "//ul[contains(@id, 'ui-id-')][3]//li//a"
    destination_location_dropdown_options = "//label[contains(text(),'Destination Location')]/../../../../../../.." \
                                            "/../../../../following-sibling::ul[4]//li/a"
    transfer_add_line = "//td[@colspan='8']//a[contains(text(), 'Add a line')]"
    transfer_product_box = "//div[@name='product_id']"
    transfer_demand_box = "//input[contains(@name,  'product_uom_qty') and contains(@type, 'text') ]"
    transfer_unit_box = "//div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/div[1]/div[1]/div[1]/input[1]"
    deliver_address_search_results = "tr.o_data_row:nth-child(1) > td.o_data_cell.o_field_cell.o_list_char" \
                                     ".o_readonly_modifier:nth-child(1)"
    contact_create_button = "div.modal-content footer.modal-footer > button.btn.btn-primary:nth-child(1)"
    product_box_options = "//ul[contains(@class, 'dropdown-menu ui-front') ][6]//li//a"
    unit_box_options = "//ul[contains(@class, 'dropdown-menu ui-front') ][8]//li//a"
    product_search_result = "tr.o_data_row:nth-child(1) > td.o_data_cell.o_field_cell." \
                            "o_list_char.o_readonly_modifier:nth-child(2)"
    product_vintage_search_result = "//span[contains(text(), '{}')]/../../../.."
    transfer_create_highlight = "div.o_list_buttons.d-flex > button.btn.btn-primary.o_list_button_add:nth-child(3)"
    create_button = "//span[contains(text(),'Create')]"
    make_as_to_do = "div.o_form_sheet_bg div.o_form_statusbar div.o_statusbar_buttons > " \
                    "button.btn.btn-primary:nth-child(1)"
    check_available = "div.o_form_statusbar div.o_statusbar_buttons > button.btn.btn-primary:nth-child(2)"
    validate = "div.o_form_statusbar div.o_statusbar_buttons > button.btn.btn-primary:nth-child(3)"
    apply = "div:nth-child(1) footer:nth-child(1) > button.btn.btn-primary:nth-child(1)"

    # --------------------------------Reporting-------------------------------------------
    reporting = "//span[contains(text(),'Reporting')]"
    inventory_report_option = "//a[contains(text(),'Inventory Report')]"
    top_category = "tr.o_group_header.o_group_has_content > th.o_group_name:nth-child(1)"
    location_category = "//*[contains(text(), '{}')]"
    available_quantity = "//td[contains(text(), '{}')]//following-sibling::td[@name='available_quantity']"

    # --------------------------------Configuration-------------------------------------------
    configuration = "//span[contains(text(), 'Configuration')]"
    warehouse_option = "//a[contains(text(),'Warehouses')]"
    warehouse_create = "div.o_list_buttons.d-flex > button.btn.btn-primary.o_list_button_add:nth-child(3)"
    warehouse_name = "name"
    short_name = "code"
    address = "//table[2]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/input[1]"
    address_dropdown_options = "//ul[contains(@class, 'ui-menu ui-widget')][1]//li//a"
    location_option = "//a[contains(text(),'Locations')]"
    parent_location = "location_id"
    location_type = "usage"
    validation_error = "//h4[contains(text(),'Validation Error')]"
    warning = ".o_dialog_warning"
    ok_button = "div.modal-content footer.modal-footer > button.btn.btn-primary"
    discard_button = "div.o_form_buttons_edit > button.btn.btn-secondary.o_form_button_cancel:nth-child(2)"
    location_type_option = "//option[contains(text(),'{}')]"
    location_result = "//td[(text()='{}')]"
    location_name = "//span[contains(text(), '{}') and (@name='name')]"
