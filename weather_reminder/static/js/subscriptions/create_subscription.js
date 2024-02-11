document.addEventListener('DOMContentLoaded', function () {
    const subscriptionForm = document.getElementById('subscription-form');
    subscriptionForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(subscriptionForm);

        fetch(subscriptionForm.action, {
            method: 'POST',
            body: formData,
        })
            .then(response => {
                if (response.ok) {
                    window.location = '/subscriptions/';
                } else {
                    alert('Failed to create subscription. Please try again.');
                }
            })
    });
});