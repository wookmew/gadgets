import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Unicafe from './unicafe.jsx'
import Anecdotes from './Anecdotes.jsx'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* <App /> exercises 1.1.-1.5 */}
  {/* <Unicafe /> exercises 1.6.-1.14 */}
  <Anecdotes/>
  </React.StrictMode>,
)
