import DisplayPhonebook from  './component/server/phonebook'
import axios from 'axios'
import { useState, useEffect } from 'react'

const ServerApp = () => {
  const [persons, setPersons] = useState([]) 
  useEffect(() => {
  axios
    .get('http://localhost:3001/persons')
    .then(response => {
      console.log('response', response.data)
      setPersons(response.data)
  })}, [])
  return (
    <div>
    <DisplayPhonebook persons={persons} setPersons={setPersons}/>
    </div>
  )
}

export default ServerApp