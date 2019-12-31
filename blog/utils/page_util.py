"""和分页有关的工具函数
用到分页的模块对该文件都会有引用
"""


def calc_page_btn_list(paginator, current_page):
    """计算分页滑动窗口按钮组"""
    page_btn_list = []
    offset = 0
    if current_page - 2 in paginator.page_range:
        page_btn_list.append(current_page - 2)
    else:
        offset += 1
    if current_page - 1 in paginator.page_range:
        page_btn_list.append(current_page - 1)
    else:
        offset += 1
    page_btn_list.append(current_page)
    if current_page + 1 in paginator.page_range:
        page_btn_list.append(current_page + 1)
    if current_page + 2 in paginator.page_range:
        page_btn_list.append(current_page + 2)
    for i in range(1, offset + 1):
        if current_page + 2 + i in paginator.page_range:
            page_btn_list.append(current_page + 2 + i)
    return page_btn_list
