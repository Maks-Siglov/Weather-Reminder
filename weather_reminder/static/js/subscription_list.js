// Find the "List" link by its id
const subscriptionListLink = document.getElementById("subscriptionListLink");

// Attach an event listener to the link
subscriptionListLink.addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the default link behavior

    // Fetch subscription data when the link is clicked
    fetch(this.href)
        .then(response => response.json())
        .then(data => {
            const subscriptionListContainer = document.getElementById("subscriptionList");

            // Clear existing content in the subscription list container
            subscriptionListContainer.innerHTML = '';

            // Iterate over the subscription data and create HTML elements
            data.forEach(subscription => {
                const subscriptionDiv = document.createElement("div");
                subscriptionDiv.classList.add("subscription");
                subscriptionDiv.innerHTML = `
                    <p>User: ${subscription.user}</p>
                    <p>City: ${subscription.city}</p>
                    <p>Notification Period: ${subscription.notification_period}</p>
                `;
                subscriptionListContainer.appendChild(subscriptionDiv);
            });
        })
        .catch(error => {
            console.error("Error fetching subscription data:", error);
        });
});
