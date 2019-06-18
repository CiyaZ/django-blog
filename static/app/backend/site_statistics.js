$(document).ready(function () {
    loadData();
});

function loadData() {
    $.ajax({
        type: "GET",
        async: true,
        url: '/backend/statistics/query',
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function (msg) {
            loadBlogTable(msg.blog_cnt, msg.category_cnt);
            loadBlogChart(msg.blogs_cnt);
        }
    });
}

function loadBlogTable(blogCnt, categoryCnt) {
    $('#category-count').text(categoryCnt);
    $('#blog-count').text(blogCnt);
}

function loadBlogChart(blogsCnt) {
    var blogChart = echarts.init($('#blog-chart').get(0));
    var xAxis = [];
    var value = [];
    for(var i = 0; i < 7; i++) {
        xAxis.push(blogsCnt[i].date);
        value.push(blogsCnt[i].value);
    }
    option = {
        xAxis: {
            type: 'category',
            data: xAxis
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: value,
            type: 'line'
        }]
    };
    blogChart.setOption(option);
}
