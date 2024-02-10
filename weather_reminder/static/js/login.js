document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(loginForm);

        fetch(loginForm.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            if (response.status === 200) {
                window.location.href = '/';
            } else {
                console.log(response);
            }
        })
        .then(data => {
            Swal.fire({
                icon: 'error',
                title: 'Authentication Failed',
                text: data.error,
            }).then(() => {
                window.location.href = '/users/login/';
            });
        })
    });
});