

console.log("Sanity check!");

// new
// Get Stripe publishable key
fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // new
  // Event handler
  document.querySelector('#sumbitBtn').addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/")
    .then((result) => {return result.json(); })
    .then((data) =>{
        console.log(data);
        return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) =>{
        console.log(res);
    })
  })
});