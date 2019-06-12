var categoryListGlobal = {};

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