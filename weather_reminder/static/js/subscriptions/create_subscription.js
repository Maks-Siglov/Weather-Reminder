document.addEventListener('DOMContentLoaded', function () {
    const subscriptionForm = document.getElementById('subscription-form');
    subscriptionForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(subscriptionForm);

        fetch(subscriptionForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'Authorization': `Bearer ${getCookie('access_token')}`
            }
        })
            .then(response => {
                if (response.ok) {
                    window.location = '/subscriptions/';
                } else if (response.status === 400) {
                    displayErrors(response)
                } else if (response.status === 401) {

                    fetch('/api/auth/v1/token/refresh/', {
                        method: 'POST',
                        body: JSON.stringify({
                            'refresh': getCookie('refresh_token')
                        }),
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                        .then(response => {
                            if (response.ok) {
                                const newAccess = response.access
                                document.cookie = `access_token=${newAccess}; path=/`

                                fetch(subscriptionForm.action, {
                                    method: 'POST',
                                    body: formData,
                                    headers: {
                                        'Authorization': `Bearer ${newAccess}`
                                    }
                                })
                                    .then(response => {
                                        window.location = '/subscriptions/'
                                    })

                            } else if (response.status === 401) {
                                window.location = '/users/login/';
                            }
                        });
                }
            });
    });
});

function displayErrors(response) {
    response.json().then(data => {
        const errors = data.non_field_errors;
        const errorContainer = document.getElementById('error-display');
        console.log(errorContainer)
        errors.forEach(error => {
            const errorListItem = document.createElement('li');
            errorListItem.textContent = error;
            errorContainer.appendChild(errorListItem);
        });
    });
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
