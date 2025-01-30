document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('travelForm');
  const responseMessage = document.getElementById('responseMessage');
  const formDataDisplay = document.getElementById('formDataDisplay');

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    // Get form data
    const formData = {
      name: document.getElementById('name').value,
      age: document.getElementById('age').value,
      phone: document.getElementById('phone').value,
      query: document.getElementById('query').value,
      email: document.getElementById('email').value,
    };

    // Log the form data to the console for debugging
    console.log('Form Data:', formData);

    // Display the form data on the webpage
    displayFormData(formData);

    // Send the form data to the backend using Fetch API
    fetch('https://test-cv-lm90.onrender.com/submit', {  // Updated fetch URL
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        console.log('Response from server:', data);
        responseMessage.textContent = 'Form submitted successfully!';
      })
      .catch((error) => {
        console.error('Error:', error);
        responseMessage.textContent = 'An error occurred. Please try again.';
      });
  });

  // Function to display form data on the webpage
  function displayFormData(data) {
    // Clear previous displayed data
    formDataDisplay.innerHTML = '';

    // Create HTML content to display the form data
    const htmlContent = `
      <h2>Submitted Data:</h2>
      <p><strong>Name:</strong> ${data.name}</p>
      <p><strong>Age:</strong> ${data.age}</p>
      <p><strong>Phone Number:</strong> ${data.phone}</p>
      <p><strong>Query:</strong> ${data.query}</p>
      <p><strong>Email:</strong> ${data.email}</p>
    `;

    // Insert the HTML content into the display area
    formDataDisplay.innerHTML = htmlContent;
  }
});