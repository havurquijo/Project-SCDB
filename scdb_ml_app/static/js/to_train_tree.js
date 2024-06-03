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
    const form = document.getElementById('formPredict');
    const toastTrainedTree = document.getElementById('liveToast_FileNotFound');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // desativar o botão de envio
        document.querySelector('button[type="submit"]').disabled = true;
        document.getElementById('error-message').style.display = 'none';

        // Usar Fetch API para enviar o formulário
        fetch('/predict_tree', {
            method: 'POST',
            body: new FormData(form)
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'success') {
                  // Redirect to the results page
                  window.location.href = data.redirect;
              }if(data.status==='fileNotFound'){
                // Redirecionar para a página de resultado
                const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastTrainedTree, { delay: 2500 }); // 10 seconds
                toastTrainedTree.querySelector('.toast-body').textContent = data.message;
                toastBootstrap.show();
                // Redirect to the results page after showing the toast
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 2500); // Redirect after the toast has been visible for 10 seconds
              }else {
                  throw new Error('Erro no envio do formulário');
              }
          })
          .catch(error => {
              console.error('Erro:', error);
              document.querySelector('button[type="submit"]').disabled = false;
              document.getElementById('error-message').style.display = 'block';
          });
    });
});
