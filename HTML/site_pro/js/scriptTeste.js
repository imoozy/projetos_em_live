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

var nomeCompleto = prompt("Digite seu nome completo");
var partesNome = nomeCompleto.split(" ");
var primeiroNome = partesNome[0];

var email = prompt("Digite seu e-mail");
var temArroba = email.indexOf("@");

var mensagem = `Olá, ${primeiroNome}! Seu e-mail informado foi ${email}.`;

console.log("Nome completo:", nomeCompleto);
console.log("Primeiro nome:", primeiroNome);
console.log("Posição do @:", temArroba);

alert(mensagem);