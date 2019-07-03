var categoryListGlobal = {};

function check() {
    var categoryNameInput = $('#category-name');
    var categoryNameInvalid = $('#category-name-invalid');
    categoryNameInput.removeClass('is-invalid');
    var categoryName = categoryNameInput.val();
    var checked = true;
    if (categoryName.length < 1 || categoryName.length > 20) {
        checked = false;
        categoryNameInput.addClass('is-invalid');
        categoryNameInvalid.text('分类名长度在1-20个字符之间');
    }
    return checked;
}

function handleDeleteButton(id) {
    categoryListGlobal.categoryId = id;
    $('#delete-confirm-modal').modal('show');
}

function handleConfirmDeleteButton() {
    if (categoryListGlobal.categoryId !== undefined) {
        location.href = '/backend/categories/delete?id=' + categoryListGlobal.categoryId;
        $('#delete-confirm-modal').modal('hide');
    }
}