var replyListGlobal = {};

function fillReplyViewModal(id, title, content, checked) {
    $('#reply-modal-content').text(content);
    if (checked === 'True') {
        $('#reply-modal-title').text(title);
        $('#reply-modal-check-btn').hide();
    } else {
        $('#reply-modal-title').text(title + ' [待审核]');
        $('#reply-modal-check-btn').show();
    }
    replyListGlobal.replyId = id;
    $('#reply-view-modal').modal('show');
}

function handleConfirmCheckButton() {
        if (replyListGlobal.replyId !== undefined) {
            $('#reply-view-modal').modal('hide');
            location.href = '/backend/replies/check?id=' + replyListGlobal.replyId;
    }
}

function handleDeleteButton(id) {
    replyListGlobal.replyId = id;
    $('#delete-confirm-modal').modal('show');
}

function handleConfirmDeleteButton() {
    if (replyListGlobal.replyId !== undefined) {
        $('#delete-confirm-modal').modal('hide');
        location.href = '/backend/replies/delete?id=' + replyListGlobal.replyId;
    }
}

function navTo(blogId) {

    parent.window.location.href = '/blogs/' + blogId;
}
