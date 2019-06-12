$(document).ready(function () {

});

function check() {
    var usernameInput = $('#username');
    var usernameInvalid = $('#username-invalid');
    var passwordInput = $('#password');
    var passwordInvalid = $('#password-invalid');

    usernameInput.removeClass('is-invalid');
    passwordInput.removeClass('is-invalid');

    var username = usernameInput.val();
    var password = passwordInput.val();

    var checked = true;

    if (username.length < 1 || username.length > 20) {
        checked = false;
        usernameInput.addClass('is-invalid');
        usernameInvalid.text('用户名长度在1-20个字符之间');
    }

    if (password.length < 1 || password.length > 255) {
        checked = false;
        passwordInput.addClass('is-invalid');
        passwordInvalid.text('密码长度在1-255个字符之间');
    }

    return checked;
}