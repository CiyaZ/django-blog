var blogEditGlobal = {
    'changed': false
};

$(document).ready(function () {
    // 挂载修改退出提示钩子
    $('#title').keyup(function () {
        blogEditGlobal.changed = true;
    });
    $('#content').keyup(function () {
        blogEditGlobal.changed = true;
    });
    $('#category').change(function () {
        blogEditGlobal.changed = true;
    });
    // 加载CodeMirror编辑器
    var cmEditor = CodeMirror.fromTextArea(document.getElementById('content'), {
        mode: 'text/x-markdown',
        lineNumbers: true,
        lineWrapping: true
    });
    cmEditor.on('change', function () {
        // CodeMirror虽然挂到textarea上，但实际不是textarea实现的，
        // 这里要把修改同步到原来的textarea上
        blogEditGlobal.changed = true;
        $('#content').val(cmEditor.getValue());
    });
});

function leaveConfirm(nextSrc) {
    blogEditGlobal.nextSrc = nextSrc;
    if (blogEditGlobal.changed) {
        $('#leave-confirm-modal').modal('show');
    } else {
        doLeave();
    }
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

function previewBlog() {
    var content = $('#content');
    var csrf = $('[name="csrfmiddlewaretoken"]');
    $.ajax({
        type: "POST",
        async: true,
        url: '/backend/blogs/preview',
        data: {
            'csrfmiddlewaretoken': csrf.val(),
            'content': content.val()
        },
        success: function (msg) {
            if (msg.result === '') {
                $('#content-preview').html('（无内容）');
            } else {
                $('#content-preview').html(msg.result);
            }
            $('#preview-modal').modal('show');
        },
        error: function (err) {
            $('#toast-error').toast('show');
        }
    });
}
