function changePasswordVisibility() {
    const password = document.getElementById('password');
    const togglePassword = document.getElementById('togglePassword');

    if (password.getAttribute('type') === 'password') {
        //change to text
        password.setAttribute('type', 'text');
        togglePassword.classList.add('fa-eye-slash');
    } else {
        //change to password
        password.setAttribute('type', 'password');
        togglePassword.classList.remove('fa-eye-slash');
    }
}