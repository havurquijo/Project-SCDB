/*
SCDB-ML-app is a deployed app to analize the U.S. Supreme Court Database
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
    const form = document.getElementById('myForm');
    const toastTrainedTree = document.getElementById('liveToast');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Mostrar o spinner e desativar o botão de envio
        document.getElementById('loading').classList.remove('invisible');
        document.querySelector('button[type="submit"]').disabled = true;
        document.getElementById('error-message').style.display = 'none';

        // Usar Fetch API para enviar o formulário
        fetch('/train_tree', {
            method: 'POST',
            body: new FormData(form)
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'success') {
                  // Redirecionar para a página de resultado
                  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastTrainedTree, { delay: 2000 }); // 10 seconds
                  toastTrainedTree.querySelector('.toast-body').textContent = data.message;
                  toastBootstrap.show();
                  // Redirect to the results page after showing the toast
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 2000); // Redirect after the toast has been visible for 3 seconds
              }else if (data.status === 'fail') {
                const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastTrainedTree, { delay: 2000 }); // 10 seconds
                toastTrainedTree.querySelector('.toast-body').textContent = data.message;
                toastBootstrap.show();
                    // Redirect to the results page after showing the toast
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 2000);
              }else {
                  throw new Error('Erro no envio do formulário');
              }
          })
          .catch(error => {
              console.error('Erro:', error);
              document.getElementById('loading').classList.add('invisible');
              document.querySelector('button[type="submit"]').disabled = false;
              document.getElementById('error-message').style.display = 'block';
          });
    });
});
