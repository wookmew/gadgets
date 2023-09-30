import ShowPerson from './showPerson'
import AddName from './addPerson'
import { useState } from 'react'
import PhoneFilter from './phoneFilter'

const DisplayPhonebook = ({persons, setPersons}) => {
  const [newPersons, setNewPersons] = useState([]) 
  const [newName, setNewName] = useState('')
  const [newNumber, setNewNumber] = useState(0)
  const [newFilter, setFilter] = useState('')
  return (
    <div>
      <h2>Phonebook</h2>
      <PhoneFilter newFilter={newFilter} persons={persons} newPersons={newPersons} setPersons={setPersons} setNewPersons={setNewPersons} setFilter={setFilter}/>
      <AddName persons={persons} newName={newName} newNumber={newNumber} 
      setPersons={setPersons} setNewName={setNewName} setNewNumber={setNewNumber}/>
      <ShowPerson persons={persons} newPersons={newPersons} newFilter={newFilter}/>
    </div>
  )
}

export default DisplayPhonebook
