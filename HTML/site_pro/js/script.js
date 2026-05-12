function changeTextButton() {
    var nome = document.getElementById("nome").value;
    var mensagem = `Olá, ${nome}! Bem-vindo ao nosso site!`;

    document.getElementById("resultado").innerText = mensagem;
}

function approvalAge() {
    var idade = parseInt(document.getElementById("idade").value);
    var resultado = idade >= 18 ? "Aprovado" : "Reprovado";

    document.getElementById("resultado").innerText = resultado;

    if (idade < 18) {
        setTimeout(function() {
            window.location.href = "/HTML/site_pro/index.html";
        }, 2000);
    }
}
