function check() {
    var domainInput = $('#conf-domain');
    var domainInvalid = $('#domain-invalid');
    domainInput.removeClass('is-invalid');
    var domain = domainInput.val();
    var checked = true;
    if (domain.length < 1 || domain.length > 255) {
        checked = false;
        domainInput.addClass('is-invalid');
        domainInvalid.text('域名长度在1-255个字符之间');
    }
    return checked;
}