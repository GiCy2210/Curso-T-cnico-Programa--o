<script>
    function validarLogin() {
        // Captura os campos do formulário
        const usuarioInput = document.getElementById("usuario");
        const senhaInput = document.getElementById("senha");
        const erroMsg = document.getElementById("erro");

        // Verifica se os campos existem (segurança contra falhas no HTML)
        if (!usuarioInput || !senhaInput || !erroMsg) {
            alert("Erro ao carregar os campos. Verifique se os IDs estão corretos.");
            return;
        }

        // Pega os valores digitados e normaliza
        const usuario = usuarioInput.value.trim().toLowerCase();
        const senha = senhaInput.value.trim();

        // Define os valores corretos
        const usuarioCorreto = "nobody";
        const senhaCorreta = "2210";

        // Verifica se estão corretos
        if (usuario === usuarioCorreto && senha === senhaCorreta) {
            const loginDiv = document.getElementById("login");
            const conteudoDiv = document.getElementById("conteudo");

            if (loginDiv && conteudoDiv) {
                // Esconde a tela de login e mostra o conteúdo
                loginDiv.style.display = "none";
                conteudoDiv.style.display = "block";
                erroMsg.innerText = ""; // limpa mensagem de erro
            }
        } else {
            // Mostra mensagem de erro
            erroMsg.innerText = "Música ou data incorretas! 🥲";
        }
    }
</script>