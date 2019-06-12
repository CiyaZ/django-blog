function showLoading() {
    if ($('#loading').length === 0) {
        var loading = $(
            '<div id="loading">' +
            '<div class="loading-circle"></div>' +
            '<div class="loading-txt"><span>Loading</span></div>' +
            '<div class="loading-overlay"></div>' +
            '</div>'
        );
        $('body').append(loading);
    }
}

function hideLoading() {
    if ($('#loading').length !== 0) {
        $('#loading').remove();
    }
}