function check() {
    var protocolInput = $('#protocol');
    var domainInput = $('#domain');
    var domainInvalid = $('#domain-invalid');
    var usernameInput = $('#username');
    var usernameInvalid = $('#username-invalid');
    var emailInput = $('#email');
    var emailInvalid = $('#email-invalid');
    var avatarInput = $('#avatar');
    var avatarInvalid = $('#avatar-invalid');
    var mottoInput = $('#motto');
    var mottoInvalid = $('#motto-invalid');
    var passwordInput = $('#password');
    var passwordInvalid = $('#password-invalid');
    var repasswordInput = $('#repassword');
    var repasswordInvalid = $('#repassword-invalid');

    domainInput.removeClass('is-invalid');
    usernameInput.removeClass('is-invalid');
    emailInput.removeClass('is-invalid');
    avatarInput.removeClass('is-invalid');
    mottoInput.removeClass('is-invalid');
    passwordInput.removeClass('is-invalid');
    repasswordInput.removeClass('is-invalid');

    var protocol = protocolInput.val();
    var domain = domainInput.val();
    var username = usernameInput.val();
    var email = emailInput.val();
    var avatar = avatarInput.val();
    var motto = mottoInput.val();
    var password = passwordInput.val();
    var repassword = repasswordInput.val();

    var checked = true;

    if (domain.length < 1 || domain.length > 255) {
        checked = false;
        domainInput.addClass('is-invalid');
        domainInvalid.text('域名长度在1-255之间');
    }

    if(domain.indexOf('/') !== -1) {
        checked = false;
        domainInput.addClass('is-invalid');
        domainInvalid.text('输入域名不要带有/等字符');
    }

    if (username.length < 1 || username.length > 20) {
        checked = false;
        usernameInput.addClass('is-invalid');
        usernameInvalid.text('用户名长度在1-20个字符之间');
    }

    if(email.length > 0) {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (email.length > 255) {
            checked = false;
            emailInput.addClass('is-invalid');
            emailInvalid.text('邮箱长度不能超过255个字符');
        }
        if(!re.test(email)) {
            checked = false;
            emailInput.addClass('is-invalid');
            emailInvalid.text('邮箱格式不匹配');
        }
    }

    if(avatar.length > 255) {
        checked = false;
        avatarInput.addClass('is-invalid');
        avatarInvalid.text('该字段长度不能超过255个字符');
    }

    if(motto.length > 255) {
        checked = false;
        mottoInput.addClass('is-invalid');
        mottoInvalid.text('该字段长度不能超过255个字符');
    }
    if (password.length < 1 || password.length > 255) {
        checked = false;
        passwordInput.addClass('is-invalid');
        passwordInvalid.text('密码长度在1-255个字符之间');
    }
    if (repassword.length < 1 || repassword.length > 255) {
        checked = false;
        repasswordInput.addClass('is-invalid');
        repasswordInvalid.text('密码长度在1-255个字符之间');
    }
    if (password !== repassword) {
        checked = false;
        passwordInput.addClass('is-invalid');
        repasswordInput.addClass('is-invalid');
        passwordInvalid.text('两次输入不一致');
        repasswordInvalid.text('两次输入不一致');
    }

    return checked;
}