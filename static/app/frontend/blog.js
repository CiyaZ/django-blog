/**
 * hightlight.js 初始化应用代码高亮
 */
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('pre code').forEach((block) => {
        hljs.highlightBlock(block);
    });
});

$(document).ready(function () {
    // 返回顶部
    $.fn.showBacktop();
    // 页面默认展开评论
    $('.load-sub-reply').trigger('click');
});

/**
 * 异步加载子评论
 * @param node 父DOM节点
 * @param replyId 父评论ID
 */
function loadSubReplies(node, replyId) {
    var divNode = $('#sub-' + replyId + '-replies');
    if (divNode.children().length === 0) {
        $.ajax({
            type: "GET",
            async: true,
            url: '/replies/sub?replyId=' + replyId,
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            success: function (msg) {
                var data = msg.data;
                for (var i = 0; i < data.length; i++) {

                    var separator = '';
                    if (i !== data.length - 1) {
                        separator = '<div style="background-color: #eeeeee; height: 1px;margin-top: 1rem; margin-bottom: 1rem"></div>';
                    }

                    var subReplyNode = $('<div style="margin-top: 1rem; margin-left: 1rem; padding-left: 2rem; border-left: 3px solid #cbcbcb">' +
                        '                        <div class="row">' +
                        '                            <div class="col-lg-1"><img src="' + data[i].gravatarUrl + '" style="border-radius: 999px" /></div>' +
                        '                            <div class="col-lg-11">' +
                        '                                <div>' +
                        '                                    <span style="font-size: 16px">' + data[i].nickname + '</span>' +
                        '                                </div>' +
                        '                                <div style="color: #989898">' +
                        '                                    <span>' + data[i].createTime + '</span>' +
                        '                                </div>' +
                        '                            </div>' +
                        '                        </div>' +
                        '                        <div class="row">' +
                        '                            <div style="margin-top: 5px; color: #434343" class="col-lg-11 offset-lg-1">' + data[i].content + '</div>' +
                        '                        </div>' +
                        '                        <div style="text-align: right; margin-right: 2rem">' +
                        '                            <a style="text-decoration: none" href="#reply-content" onclick="initSubReply(\'' + data[i].id + '\', \'' + data[i].nickname + '\', \'' + data[i].rootReplyId + '\')">回复</a>' +
                        '                        </div>' + separator +
                        '                    </div>');
                    divNode.append(subReplyNode);
                    var str = $(node).text();
                    $(node).text('折叠' + str.substring(2, str.length));
                }
            },
            error: function (err) {
            }
        });
    } else {
        divNode.empty();
        var str = $(node).text();
        $(node).text('展开' + str.substring(2, str.length));
    }
}

/**
 * 提交子评论，在回复表单中初始化
 * @param parentReplyId 父评论ID
 * @param parentReplyName 父级评论的评论者名字
 * @param rootReplyId 当前评论树根节点ID
 */
function initSubReply(parentReplyId, parentReplyName, rootReplyId) {
    $('#parentReplyId').val(parentReplyId);
    $('#rootReplyId').val(rootReplyId);
    $('#rootReplyButton').hide();
    $('#subReplyButton').show();
    $('#reply-content').val('回复 ' + parentReplyName + '：');
}

/**
 * 提交根评论，在回复表单中初始化
 */
function initRootReply() {
    $('#parentReplyId').val('');
    $('#rootReplyId').val('');
    $('#rootReplyButton').show();
    $('#subReplyButton').hide();
    $('#reply-content').val('');
}

/**
 * 回复表单前端校验
 * @returns {boolean} 校验结果直接应用于页面表单提交
 */
function replyFormCheck() {
    var nicknameInput = $('#nickname');
    var nicknameInvalid = $('#nickname-invalid');
    var emailInput = $('#email');
    var emailInvalid = $('#email-invalid');
    var urlInput = $('#url');
    var urlInvalid = $('#url-invalid');
    var replyContentInput = $('#reply-content');
    var replyContentInvalid = $('#reply-content-invalid');

    nicknameInput.removeClass('is-invalid');
    emailInput.removeClass('is-invalid');
    urlInput.removeClass('is-invalid');
    replyContentInput.removeClass('is-invalid');

    var nickname = $.trim(nicknameInput.val());
    nicknameInput.val(nickname);
    var email = $.trim(emailInput.val());
    emailInput.val(email);
    var url = $.trim(urlInput.val());
    urlInput.val(url);
    var replyContent = $.trim(replyContentInput.val());
    replyContentInput.val(replyContent);

    var checked = true;

    if (nickname.length < 1 || nickname.length > 20) {
        checked = false;
        nicknameInput.addClass('is-invalid');
        nicknameInvalid.text('昵称长度在1-20个字符之间');
    }

    if (email.length < 1 || email.length > 50) {
        checked = false;
        emailInput.addClass('is-invalid');
        emailInvalid.text('邮箱长度在1-50个字符之间');
    }

    if (url.length > 255) {
        checked = false;
        urlInput.addClass('is-invalid');
        urlInvalid.text('网址长度不能超过255个字符');
    }

    if (replyContent.length < 1) {
        checked = false;
        replyContentInput.addClass('is-invalid');
        replyContentInvalid.text('回复不能为空');
    }

    if (replyContent.length > 1000) {
        checked = false;
        replyContentInput.addClass('is-invalid');
        replyContentInvalid.text('回复长度不能超过1000字');
    }

    return checked;
}