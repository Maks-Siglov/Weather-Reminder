document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(loginForm);

        fetch(loginForm.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            if (response.status === 200) {
                window.location.href = '/';
            } else if (response.status === 401) {
                return response.json();
            } else {
                throw new Error('Unexpected response from server');
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