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

function navTo(src) {

    var iframe = $('#iframe', parent.document);

    if (iframe.attr('src').startsWith('/backend/blogs/edit')) {
        // 针对文章编辑功能，进行一下离开页面的确认
        iframe.get(0).contentWindow.leaveConfirm(src);
    } else {
        iframe.attr('src', src);
    }
}