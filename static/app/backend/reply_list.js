var replyListGlobal = {};

function fillReplyViewModal(title, content) {
    $('#reply-modal-title').text(title);
    $('#reply-modal-content').text(content);
    $('#reply-view-modal').modal('show');
}

function handleDeleteButton(id) {
    replyListGlobal.replyId = id;
    $('#delete-confirm-modal').modal('show');
}

function handleConfirmDeleteButton() {
    if (replyListGlobal.replyId !== undefined) {
        location.href = '/backend/replies/delete?id=' + replyListGlobal.replyId;
        $('#delete-confirm-modal').modal('hide');
    }
}

function navTo(blogId) {

    parent.window.location.href = '/blogs/' + blogId;
}
