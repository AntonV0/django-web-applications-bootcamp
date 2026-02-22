document.addEventListener("DOMContentLoaded", () => {
  // Only run if the datepicker library + inputs exist on this page
  if (typeof datepicker === "function") {
    const checkin = document.querySelector(".js-checkin");
    const checkout = document.querySelector(".js-checkout");

    if (checkin) datepicker(checkin, { startDay: 1 });
    if (checkout) datepicker(checkout, { startDay: 1 });
  }
});