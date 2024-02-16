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
                } else if (response.status == 401) {

                    fetch('/api/auth/v1/token/refresh/', {
                        method: 'POST',
                        body: {
                            'refresh': getCookie('refresh_token')
                        }
                    })
                        .then(response => {
                            if (response.ok) {
                                const newAccess = response.access
                                console.log('newaccess', newAccess);

                                fetch(subscriptionForm.action, {
                                    method: 'POST',
                                    body: formData,
                                    headers: {
                                        'Authorization': `Bearer ${newAccess}`
                                    }
                                });

                            } else {
                                window.location = '/users/login/';
                            }
                        });
                }
            });
    });
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
