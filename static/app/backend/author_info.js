function check() {
    var usernameInput = $('#username');
    var usernameInvalid = $('#username-invalid');
    var emailInput = $('#email');
    var emailInvalid = $('#email-invalid');
    var avatarInput = $('#avatar');
    var avatarInvalid = $('#avatar-invalid');
    var mottoInput = $('#motto');
    var mottoInvalid = $('#motto-invalid');

    usernameInput.removeClass('is-invalid');
    emailInput.removeClass('is-invalid');
    avatarInput.removeClass('is-invalid');
    mottoInput.removeClass('is-invalid');

    var username = usernameInput.val();
    var email = emailInput.val();
    var avatar = avatarInput.val();
    var motto = mottoInput.val();

    var checked = true;

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

    return checked;
}