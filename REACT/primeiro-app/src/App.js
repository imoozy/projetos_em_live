import logo from './logo.svg';
import Saudacao from './components/saudacao';
import MeusDados from './components/MeusDados';
import './App.css';

function App() {
  const nome = "Lucas Magalhães de Lima";
  return (
    <div className="App">
      <header className="App-header">

        <Saudacao nome="Lucas" />
        <MeusDados />
        <p>2 + 2 = {2 + 2} o resultado 4 foi gerado via JS, no arquivo app.js para entender</p>
      </header>
      <main>
        <img src={logo} className="App-logo" alt="logo" />
      </main>
      <footer>
          <p>Desenvolvido por {nome.toUpperCase()}</p>
      </footer>
    </div>
  );
}

export default App;
