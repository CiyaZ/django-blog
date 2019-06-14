function check() {
    var passwordInput = $('#password');
    var newPasswordInput = $('#new-password');
    var rePasswordInput = $('#re-password');

    var passwordInvalid = $('#password-invalid');
    var newPasswordInvalid = $('#new-password-invalid');
    var rePasswordInvalid = $('#re-password-invalid');

    var password = passwordInput.val();
    var newPassword = newPasswordInput.val();
    var rePassword = rePasswordInput.val();

    var checked = true;

    // 表单校验
    if (password.length < 1 || password.length > 255) {
        checked = false;
        passwordInput.addClass('is-invalid');
        passwordInvalid.text('密码长度在1-255个字符之间');
    }
    if (newPassword.length < 1 || newPassword.length > 255) {
        checked = false;
        newPasswordInput.addClass('is-invalid');
        newPasswordInvalid.text('密码长度在1-255个字符之间');
    }
    if (rePassword.length < 1 || rePassword.length > 255) {
        checked = false;
        rePasswordInput.addClass('is-invalid');
        rePasswordInvalid.text('密码长度在1-255个字符之间');
    }
    if (newPassword !== rePassword) {
        checked = false;
        newPasswordInput.addClass('is-invalid');
        rePasswordInput.addClass('is-invalid');
        newPasswordInvalid.text('两次输入不一致');
        rePasswordInvalid.text('两次输入不一致');
    }

    return checked;
}
