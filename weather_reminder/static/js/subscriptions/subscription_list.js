document.addEventListener('DOMContentLoaded', function () {
    const subscriptionListLink = document.getElementById('subscription-list');
    const subscriptionContainer = document.getElementById('subscription-container');

    fetch(subscriptionListLink.href, {
        method: "GET",
        headers: {
            'Authorization': `Bearer ${getCookie('access_token')}`
        }
    })
    .then(response => {

        if (response.status === 200) {
            response.json()
            .then(data => {
                data.forEach(subscription => {
                    const card = createSubscriptionCard(subscription);
                    subscriptionContainer.appendChild(card);
                });
            });
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
                    return response.json();
                } else {
                    window.location = '/users/login/';
                    throw new Error('Failed to refresh token');
                }
            })
            .then(data => {
                const newAccess = data.access;

                fetch(subscriptionListLink.href, {
                    method: "GET",
                    headers: {
                        'Authorization': `Bearer ${newAccess}`
                    }
                })
                .then(response => {
                    if (response.status === 200) {
                        response.json()
                        .then(data => {
                            data.forEach(subscription => {
                                const card = createSubscriptionCard(subscription);
                                subscriptionContainer.appendChild(card);
                            });
                        });
                    } else if (response.status === 401) {
                        window.location = '/users/login/';
                    }
                });
            })
            .catch(error => {
                console.error('Error refreshing token:', error);
            });
        }
    });
});




function createSubscriptionCard(subscription) {
    const card = document.createElement('div');
    card.classList.add('card', 'm-3', 'text-white', 'bg-primary');

    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body');

    const cityName = document.createElement('h5');
    cityName.classList.add('card-title');
    cityName.textContent = subscription.city;

    const notificationPeriod = document.createElement('p');
    notificationPeriod.classList.add('card-text');
    notificationPeriod.textContent = `Notification Period: ${subscription.notification_period} hours`;

    const editButton = document.createElement('button');
    editButton.textContent = 'Edit';
    editButton.classList.add('btn', 'btn-secondary', 'mr-2');
    editButton.addEventListener('click', function() {
    const existingInputField = cardBody.querySelector('input');
    const existingSaveButton = cardBody.querySelector('.save-button');

    if (!existingInputField && !existingSaveButton) {
        const [inputField, saveButton] = editButtonAction(subscription.pk);
        cardBody.appendChild(inputField);
        cardBody.appendChild(saveButton);
    }
});

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.classList.add('btn', 'btn-danger','mr-2');
    deleteButton.addEventListener('click', function() {
        deleteButtonAction(subscription.pk);
    });

    const sendButton = document.createElement('button');
    sendButton.textContent = 'Send';
    sendButton.classList.add('btn', 'btn-info', 'mr-2');
    sendButton.addEventListener('click', function() {
        sendButtonAction(subscription);
    });

    cardBody.appendChild(cityName);
    cardBody.appendChild(notificationPeriod);
    cardBody.appendChild(editButton);
    cardBody.appendChild(deleteButton);
    cardBody.appendChild(sendButton);

    if (subscription.is_enabled) {
        const disableButton = document.createElement('button');
        disableButton.textContent = 'Disable';
        disableButton.classList.add('btn', 'btn-warning', 'mr-2');
        disableButton.addEventListener('click', function () {
            disableButtonAction(subscription.pk);
            cardBody.removeChild(sendButton)
        });
        cardBody.appendChild(disableButton)
    } else if (!subscription.is_enabled){
        const enableButton = document.createElement('button');
        enableButton.textContent = 'Enable';
        enableButton.classList.add('btn', 'btn-success', 'mr-2');
        enableButton.addEventListener('click', function () {
            enableButtonAction(subscription.pk);
            cardBody.appendChild(sendButton);
        });
        cardBody.appendChild(enableButton)
    }


    card.appendChild(cardBody);

    return card;
}

function editButtonAction(subscriptionPk) {
    const inputField = document.createElement('input');
    inputField.type = 'number';
    inputField.placeholder = 'New notification period';
    inputField.classList.add('form-control', 'm-2');

    const saveButton = document.createElement('button');
    saveButton.textContent = 'Save';
    saveButton.classList.add('btn', 'btn-success', 'mr-2');
    saveButton.addEventListener('click', function () {
        const newNotificationPeriod = parseInt(inputField.value);
        if (!isNaN(newNotificationPeriod) && newNotificationPeriod > 0) {
            fetch(`/api/subscription/v1/${subscriptionPk}/edit`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "notification_period": newNotificationPeriod
                })
            })
                .then(response => {
                    if (response.ok){
                        window.location.reload()
                    }
                })
        } else {
            alert('Notification period should be a positive number of hours');
        }
    });

    return [inputField, saveButton];
}


function deleteButtonAction(subscriptionPk){
    fetch(`/api/subscription/v1/${subscriptionPk}/delete`, {
            method: 'DELETE'
        })
        .then(() => {
            window.location.reload();
        })
}


function sendButtonAction(subscription) {
    const city = subscription.city

    fetch(`/api/weather-data/v1/get_data/${city}`, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(data => {

            fetch(`/api/weather-data/v1/send_email/${subscription.user}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token
                },
                body: JSON.stringify({'city': city, weather_data: data})
            })
                .then(response => response.json())
                .then(result => {
                    console.log(result);
                })
        })
}

function disableButtonAction(subscription_pk) {
    fetch(`/api/subscription/v1/${subscription_pk}/disable`, {
            method: 'POST'
        })
        .then(() => {
            window.location.reload();
        })
}

function enableButtonAction(subscription_pk) {
    fetch(`/api/subscription/v1/${subscription_pk}/enable`, {
            method: 'POST'
        })
        .then(() => {
            window.location.reload();
        })
}


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
