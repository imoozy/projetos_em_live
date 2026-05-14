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

function retorno() {
    window.location.href = "/HTML/site_pro/index.html";
}

function addCorredor() {
    var numero = document.getElementById("posicao").value-1;
    var novo = document.getElementById("novo");
    var corredor = document.getElementsByClassName("corredor");

    corredor[numero].innerText = novo.value;
}

