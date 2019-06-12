$(document).ready(function () {
    //
});

var blogListGlobal = {};

function handleDeleteButton(id) {
    blogListGlobal.blogId = id;
    $('#delete-confirm-modal').modal('show');
}

function handleConfirmDeleteButton() {
    if (blogListGlobal.blogId !== undefined) {
        location.href = '/backend/blogs/delete?id=' + blogListGlobal.blogId;
        $('#delete-confirm-modal').modal('hide');
    }
}