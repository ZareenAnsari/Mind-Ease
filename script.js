// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
    // Get the form element
    const appointmentForm = document.querySelector('.appointment-form');

    // Add event listener for form submission
    appointmentForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the default form submission

        // Get form field values
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const doctor = document.getElementById('doctor').value;
        const date = document.getElementById('date').value;
        const time = document.getElementById('time').value;
        const message = document.getElementById('message').value;

        // Validate form fields (example: ensure all fields are filled)
        if (!name || !email || !phone || !doctor || !date || !time) {
            alert('Please fill out all required fields.');
            return;
        }

        // Prepare appointment data
        const appointmentData = {
            name,
            email,
            phone,
            doctor,
            date,
            time,
            message,
        };

        // Store appointment data in localStorage (for demonstration purposes)
        let appointments = JSON.parse(localStorage.getItem('appointments')) || [];
        appointments.push(appointmentData);
        localStorage.setItem('appointments', JSON.stringify(appointments));

        // Confirmation alert
        alert('Your appointment has been booked successfully!');

        // Clear the form
        appointmentForm.reset();

        // Log the saved data to the console (optional)
        console.log('Saved Appointments:', appointments);
    });


});
