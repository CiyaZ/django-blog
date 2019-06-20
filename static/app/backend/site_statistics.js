$(document).ready(function () {
    loadBlogData();
    loadAccessData();
});

function loadBlogData() {
    $.ajax({
        type: "GET",
        async: true,
        url: '/backend/statistics/blog_query',
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
    for (var i = 0; i < 7; i++) {
        xAxis.push(blogsCnt[i].date);
        value.push(blogsCnt[i].value);
    }
    option = {
        title: {
            text: '近7日文章量统计',
            x: 'center'
        },
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

function loadAccessData() {
    $.ajax({
        type: "GET",
        async: true,
        url: '/backend/statistics/access_query',
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function (msg) {
            loadAccessTable(msg.access_cnt_today);
            loadAccessChart(msg.access_cnt);
        }
    });
}

function loadAccessTable(accessCntToday) {
    $('#access-count').text(accessCntToday);
}

function loadAccessChart(accessCnt) {
    var accessChart = echarts.init($('#access-chart').get(0));
    var xAxis = [];
    var value = [];
    for (var i = 0; i < 7; i++) {
        xAxis.push(accessCnt[i].date);
        value.push(accessCnt[i].value);
    }
    option = {
        title: {
            text: '近7日后端请求量统计',
            x: 'center'
        },
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
    accessChart.setOption(option);
}