document.addEventListener('DOMContentLoaded', function () {
    const subscriptionListLink = document.getElementById('subscription-list')
    const subscriptionContainer = document.getElementById('subscription-container')
    subscriptionListLink.addEventListener('click', function (event) {
        event.preventDefault();

        fetch(subscriptionListLink.href, {
            method: "GET",
        })
            .then(response => response.json())
            .then(data => {
                // window.location.href = '/subscriptions/';
                data.forEach(subscription => {
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

                    cardBody.appendChild(cityName);
                    cardBody.appendChild(notificationPeriod);
                    card.appendChild(cardBody);

                    subscriptionContainer.appendChild(card);
                })

            })
    })
})