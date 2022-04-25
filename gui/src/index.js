import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Python from './components/Python';
import {BrowserRouter, Routes, Route, HashRouter } from 'react-router-dom';

if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
  ReactDOM.render(
    <React.StrictMode>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<App />} />
          <Route path='/python' element={<Python />} />
        </Routes>
      </BrowserRouter>
    </React.StrictMode>,
    document.getElementById('root')
  );
} else {
  ReactDOM.render(
    <React.StrictMode>
      <HashRouter>
        <Routes>
          <Route path='/' element={<App />} />
          <Route path='/python' element={<Python />} />
        </Routes>
      </HashRouter>
    </React.StrictMode>,
    document.getElementById('root')
  );
}
// ReactDOM.render(
//   <React.StrictMode>
//     <BrowserRouter>
//       <Routes>
//         <Route path='/' element={<App />} />
//         <Route path='/python' element={<Python />} />
//       </Routes>
//     </BrowserRouter>
//   </React.StrictMode>,
//   document.getElementById('root')
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
