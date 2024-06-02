/*
SCDB-ML-app is a deployed app to analyze the U.S. Supreme Court Database
Copyright (C) 2024  HERMES A. V. URQUIJO

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('myForm_save');
    const toastSavingTree = document.getElementById('liveToast_saving');
    const toastErrorTree = document.getElementById('liveToast_error');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Disable the submit button and hide the error message
        document.querySelector('button[type="submit"]').disabled = true;
        document.getElementById('error-message_saving').style.display = 'none';

        // Use Fetch API to send the form
        fetch('/predicted_tree', {
            method: 'POST',
            body: new FormData(form)
        })
        .then(response => {
            console.log('Raw response:', response); // Log the raw response
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Attempt to parse JSON
        })
        .then(data => {
            console.log('Response data:', data); // Log response data for debugging

            if (data.status === 'success') {
                // Show success toast
                const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastSavingTree, { delay: 2000 });
                toastSavingTree.querySelector('.toast-body').textContent = data.message;
                toastBootstrap.show();

                // Redirect to the results page after showing the toast
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 2000); // Redirect after the toast has been visible for 2 seconds
            } else if (data.status === 'fail') {
                // Show error toast
                const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastErrorTree, { delay: 2000 });
                toastErrorTree.querySelector('.toast-body').textContent = data.message;
                toastBootstrap.show();

                // Re-enable the submit button
                document.querySelector('button[type="submit"]').disabled = false;
            } else {
                throw new Error('Unrecognized status in response');
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);

            // Show error message and re-enable the submit button
            document.getElementById('error-message_saving').style.display = 'block';
            document.querySelector('button[type="submit"]').disabled = false;
        });
    });
});
