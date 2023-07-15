import React from 'react';
import Search from './components/Search';

function App() {
  return (
    <div className="h-screen flex flex-col justify-center items-center">
      <Search classNames='w-1/2 h-fill'></Search>
      <a
        className="App-link"
        href="https://reactjs.org"
        target="_blank"
        rel="noopener noreferrer"
      >
        Learn React
      </a>
    </div>
  );
}

export default App;
