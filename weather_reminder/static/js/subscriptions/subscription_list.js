document.addEventListener('DOMContentLoaded', function () {
    const subscriptionListLink = document.getElementById('subscription-list');
    const subscriptionContainer = document.getElementById('subscription-container');

    fetch(subscriptionListLink.href, {
        method: "GET",
    })
        .then(response => response.json())
        .then(data => {
            data.forEach(subscription => {
                const card = createSubscriptionCard(subscription)
                subscriptionContainer.appendChild(card)
            })
        })
});


function createSubscriptionCard(subscription) {
    const card = document.createElement('div');
    card.classList.add('card', 'm-2');

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
    editButton.classList.add('btn', 'btn-primary', 'mr-2');
    editButton.addEventListener('click', function() {
        console.log('Edit button clicked');
    });

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.classList.add('btn', 'btn-danger');
    deleteButton.addEventListener('click', function() {
        fetch(`/api/subscription/v1/${subscription.pk}/delete`, {
            method: 'DELETE'
        })
        .then(() => {
            window.location.reload();
        })
    });

    cardBody.appendChild(cityName);
    cardBody.appendChild(notificationPeriod);
    cardBody.appendChild(editButton);
    cardBody.appendChild(deleteButton);
    card.appendChild(cardBody);

    return card;
}
