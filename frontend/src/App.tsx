import React from 'react';
import './App.css';

class OpenButton extends React.Component {
  handleClick = () => {
    console.log("Clicked");
  };
  render() {
    return (
      <button className="key-btn-open" onClick={this.handleClick}>
        Open
      </button>
    )
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>CED_KEY</p>
      </header>
      <main>
        <div className="key-name">
          temp
        </div>
        <OpenButton />
      </main>
    </div>
  );
}

export default App;
