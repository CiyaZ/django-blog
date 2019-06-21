var blogEditGlobal = {};

function leaveConfirm(nextSrc) {
    blogEditGlobal.nextSrc = nextSrc;
    $('#leave-confirm-modal').modal('show');
}

function doLeave() {
    var iframe = $('#iframe', parent.document);
    iframe.attr('src', blogEditGlobal.nextSrc);
}

function postBlog() {
    var csrf = $('[name="csrfmiddlewaretoken"]');
    var action = $('#action');
    var blogId = $('#blog-id');
    var title = $('#title');
    var category = $('#category');
    var content = $('#content');

    title.removeClass('is-invalid');
    content.removeClass('is-invalid');

    // 表单校验
    var titleInvalid = $('#title-invalid');
    var contentInvalid = $('#content-invalid');
    var checked = true;

    var titleValue = title.val();
    var contentValue = content.val();
    if (titleValue.length < 1 || titleValue.length > 100) {
        title.addClass('is-invalid');
        titleInvalid.text('标题长度必须在1-100个字符之间');
        checked = false;
    }
    if (contentValue.length < 1 || contentValue.length > 20000) {
        content.addClass('is-invalid');
        contentInvalid.text('正文长度必须在1-20000个字符之间');
        checked = false;
    }

    if (checked) {
        // 提交表单
        if (action.val() === 'add') {
            var data = {
                'csrfmiddlewaretoken': csrf.val(),
                'title': title.val(),
                'category': category.val(),
                'content': content.val()
            };
            $.ajax({
                type: "POST",
                async: true,
                url: '/backend/blogs/add',
                data: data,
                dataType: "json",
                success: function (msg) {
                    $('#toast-success').toast('show');
                    // 转为编辑模式
                    var id = msg.id;
                    action.val('update');
                    blogId.val(id);
                },
                error: function (err) {
                    $('#toast-error').toast('show');
                }
            });
        } else if (action.val() === 'update') {
            var data = {
                'csrfmiddlewaretoken': csrf.val(),
                'id': blogId.val(),
                'title': title.val(),
                'category': category.val(),
                'content': content.val()
            };
            $.ajax({
                type: "POST",
                async: true,
                url: '/backend/blogs/update',
                data: data,
                success: function (msg) {
                    $('#toast-success').toast('show');
                },
                error: function (err) {
                    $('#toast-error').toast('show');
                }
            });
        }
    }
}