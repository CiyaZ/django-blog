function navTo(src) {

    var iframe = $('#iframe');

    if (iframe.attr('src').startsWith('/backend/blogs/edit')) {
        // 针对文章编辑功能，进行一下离开页面的确认
        iframe.get(0).contentWindow.leaveConfirm(src);
    } else {
        iframe.attr('src', src);
    }
}