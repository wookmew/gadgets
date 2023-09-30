const AddName = ({persons, newName, newNumber, setPersons, setNewName, setNewNumber}) => {
  const addName = (event) => {
    event.preventDefault()
    const nameObject = {
      name: newName,
      number: newNumber,
      id: persons.length +1
    }
    const found = persons.filter((person) => person.name === newName)
    if (found.length > 0) {
      alert(`${newName} is already added to phonebook`)
      return
    }
    setPersons(persons.concat(nameObject))
    setNewName('')
    setNewNumber(0)
  }

  const handleNameChange = (event) => {
    setNewName(event.target.value)
  }

  const handleNumberChange = (event) => {
    setNewNumber(event.target.value)
  }

  return (
    <div>
    <form onSubmit={addName}>
      <div>
        name: <input 
        value={newName}
        onChange={handleNameChange}
        />
        <br/>
        number: <input 
        value={newNumber}
        onChange={handleNumberChange}
        />
      </div>
      <div>
        <button type="submit">add</button>
      </div>
    </form>
  </div>
  )
}

export default AddName