//script para entender o uso de cráse

// var nome = "lucas";
// var mensagem = `Olá, meu nome é ${nome} e este é o meu portfólio!`;
// console.log(mensagem);
// var lugarOrigem = "MASP";
// var lugarDestino = "Museu do Ipiranga";
// var meioTransporte = "Táxi";
// var novaString = `Vamos sair do ${lugarOrigem} para ${lugarDestino}. Só que vamos de ${meioTransporte}, beleza?`;
// console.log(novaString);

// -----------------------------------------------------------------------------

//localizar a posição de uma palavra em uma string

//var texto = "lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
// console.log(texto.indexOf("ipsum")); // Retorna a posição da primeira ocorrência de "ipsum"
// console.log(texto.indexOf("dolor"));

// -----------------------------------------------------------------------------

//separação de palavras em uma string usando split

// var textoCardapio = "hamburger;cheeseburger;misto-quente;cachorro-quente;hamburguer vegano;master blaster plus;mastodonte ultimate";
// var listaDePalavras = textoCardapio.split(";");
// console.log(listaDePalavras);

// -----------------------------------------------------------------------------

//exemplo de separação itens do pedido

// var pedido = "hamburger;cheeseburger;misto-quente;cachorro-quente;hamburguer vegano;master blaster plus;mastodonte ultimate";
// var itens = pedido.split(";");
// console.log("Itens do pedido:");
// console.log(itens);
// console.log(itens[0]); // Acessa o primeiro item do pedido
// console.log(itens[3]); // Acessa o quarto item do pedido

// -----------------------------------------------------------------------------

//exemplo de verificação de e-mail

// var email = "lucal7421@gmail.com"

// console.log(email.includes("@")); // Verifica se o e-mail contém o caractere "@"
// console.log(email.includes(".com")); // Verifica se o e-mail contém o domínio ".com"
// console.log(email.includes("hotmail")); // Verifica se o e-mail contém o domínio "hotmail"

// -----------------------------------------------------------------------------

//exemplo prático de uso de cráse, indexOf e split

// var nomeCompleto = prompt("Digite seu nome completo");
// var partesNome = nomeCompleto.split(" ");
// var primeiroNome = partesNome[0];

// var email = prompt("Digite seu e-mail");
// var temArroba = email.indexOf("@");

// var mensagem = `Olá, ${primeiroNome}! Seu e-mail informado foi ${email}.`;

// console.log("Nome completo:", nomeCompleto);
// console.log("Primeiro nome:", primeiroNome);
// console.log("Posição do @:", temArroba);

// alert(mensagem);

// -----------------------------------------------------------------------------


// operadores lógicos &&AND ||OR !NOT

// var fazSol = true;
// var temCombustivel = true;

// if (fazSol && temCombustivel) {
//     console.log("Vamos dar um passeio de carro!");
// } if (fazSol || temCombustivel) {
//     console.log("Podemos dar um passeio, mas precisamos verificar o combustível.");
// } if (!fazSol) {
//     console.log("Não podemos dar um passeio, pois não está fazendo sol.");
// }


// -----------------------------------------------------------------------------

// Intervalo numérico usando operadores lógicos

// var inputNumero = parseInt(prompt("Digite um número entre 1 e 10"));

// if (inputNumero >= 1 && inputNumero <= 10) {
//     console.log("seu número está dentro do intervalo permitido.");
// } else {
//     console.log("seu número está fora do intervalo permitido.");
// }


// -----------------------------------------------------------------------------

//else if para verificar o número de visitantes no site

// var visitantes = Number(prompt("Digite o número de visitantes no site"));

// if (visitantes <= 5) {
//     alert("Poucos visitantes no site");
// } else if (visitantes > 5 && visitantes <= 15) {
//     alert("Número moderado de visitantes no site");
// } else {
//     alert("Muitos visitantes no site");
// }


// -----------------------------------------------------------------------------


//switch case para verificar o dia da semana

// var diaSemana = prompt("Digite o dia da semana (ex: segunda, terça, quarta, etc.)").toLowerCase();

// switch (diaSemana) {
//     case "segunda":
//         console.log("Hoje é segunda-feira.");
//         break;
//     case "terça":
//         console.log("Hoje é terça-feira.");
//         break;
//     case "quarta":
//         console.log("Hoje é quarta-feira.");
//         break;
//     case "quinta":
//         console.log("Hoje é quinta-feira.");
//         break;
//     case "sexta":
//         console.log("Hoje é sexta-feira.");
//         break;
//     case "sábado":
//         console.log("Hoje é sábado.");
//         break;
//     case "domingo":
//         console.log("Hoje é domingo.");
//         break;
//     default:
//         console.log("Dia da semana inválido.");
// }


// -----------------------------------------------------------------------------

//exemplo prático de switch case para verificar média de nota do usuário

// var nota1 = parseFloat(prompt("Digite sua nota (0 a 10)"));
// var nota2 = parseFloat(prompt("Digite sua segunda nota (0 a 10)"));
// var media = (nota1 + nota2) / 2;

// switch (true) {
//     case (media >= 9 && media <= 10):
//         console.log("Excelente! Sua média é " + media.toFixed(2));
//         break;
//     case (media >= 7 && media < 9):
//         console.log("Bom! Sua média é " + media.toFixed(2));
//         break;
//     default:
//         console.log("você não está aprovado. Sua média é " + media.toFixed(2));
// }


// -----------------------------------------------------------------------------


//function com case switch para verificar o tipo de conta bancária

// function verificarTipoConta() {
//     var tipoConta = prompt("Digite o tipo de conta (corrente, poupança, salário)").toLowerCase();
//     switch (tipoConta) {
//         case "corrente":
//             console.log("Você selecionou uma conta corrente.");
//             break;
//         case "poupança":
//             console.log("Você selecionou uma conta poupança.");
//             break;
//         case "salário":
//             console.log("Você selecionou uma conta salário.");
//             break;
//         default:
//             console.log("Tipo de conta inválido.");
//     }
// }

// verificarTipoConta();


// -----------------------------------------------------------------------------


//usando return para calcular a média de notas

function calcularMedia(nota1, nota2) {
    var media = (nota1 + nota2) / 2;
    return media;
}

var nota1 = parseFloat(prompt("Digite sua nota (0 a 10)"));
var nota2 = parseFloat(prompt("Digite sua segunda nota (0 a 10)"));
var mediaFinal = calcularMedia(nota1, nota2);
console.log("Sua média é: " + mediaFinal.toFixed(2));

