(function ($) {
    $.fn.showBacktop = function () {
        var backtop = $('<div title="返回顶部" class="backtop-btn"><i class="fas fa-rocket"></i></div>');
        backtop.click(function () {
            $("html, body").animate({ scrollTop: 0 }, 100);
        });
        $('body').append(backtop);
    }
}(jQuery));
