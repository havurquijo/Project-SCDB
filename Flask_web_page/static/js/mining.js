document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('myForm_mining');
    const toastTrainedTree = document.getElementById('liveToast_mining');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Mostrar o spinner e desativar o botão de envio
        document.getElementById('loading').classList.remove('invisible');
        document.querySelector('button[type="submit"]').disabled = true;
        document.getElementById('error-message').style.display = 'none';

        // Usar Fetch API para enviar o formulário
        fetch('/mine_tree', {
            method: 'POST',
            body: new FormData(form)
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'success') {
                  // Redirecionar para a página de resultado
                  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastTrainedTree, { delay: 3000 }); // 10 seconds
                  toastTrainedTree.querySelector('.toast-body').textContent = data.message;
                  toastBootstrap.show();
                  // Redirect to the results page after showing the toast
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 3000); // Redirect after the toast has been visible for 10 seconds
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
if (data.status === 'success') {
    // Redirecionar para a página de resultado
    const toast_trained_tree = document.getElementById('liveToast');
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toast_trained_tree);
    //toastBootstrap.body(data.message)
    toastBootstrap.show()
} else {
    throw new Error('Erro no envio do formulário');
};
