function callGenerateSitemapAsync() {
    var btn = $('#sitemap-tool-generate-btn');
    var status = $('#sitemap-tool-status');

    btn.text('请稍后...');
    $.ajax({
        type: "GET",
        async: true,
        url: '/backend/tools/generate',
        success: function(msg) {
            btn.text('生成站点地图');
            status.text('生成站点地图成功');
            status.removeClass();
            status.addClass('text-success');
        },
        error: function(err) {
            btn.text('生成站点地图');
            status.text('出错了w(ﾟДﾟ)w');
            status.removeClass();
            status.addClass('text-danger');
        }
    });
}

function rootNavToSitemap() {
    parent.rootNavTo('/sitemap.xml');
}