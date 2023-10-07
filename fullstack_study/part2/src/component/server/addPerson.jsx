import personService from "../../services/person";

const AddName = ({
  persons,
  newName,
  newNumber,
  setPersons,
  setNewName,
  setNewNumber,
}) => {
  const addName = (event) => {
    event.preventDefault();
    const nameObject = {
      name: newName,
      number: newNumber,
      // id: persons.length +1
    };
    const found = persons.filter((person) => person.name === newName);
    if (found.length > 0) {
      const objID = found[0].id;
      console.log("found", found);
      if (
        window.confirm(
          `${newName} is already add to phonebook, replace the old number with a new one?`
        )
      ) {
        personService.update(objID, nameObject).then((resp) => {
          console.log("resp", resp);
          persons.map((person) => {
            if (person.id === objID) {
              person.number = newNumber;
            }
          });
          setPersons(persons);
          setNewName("");
          setNewNumber(0);
        });
      }
      return;
    }
    personService.create(nameObject).then((returnedPerson) => {
      setPersons(persons.concat(returnedPerson));
      setNewName("");
      setNewNumber(0);
    });
  };

  const handleNameChange = (event) => {
    setNewName(event.target.value);
  };

  const handleNumberChange = (event) => {
    setNewNumber(event.target.value);
  };

  return (
    <div>
      <h2>Add a new</h2>
      <form onSubmit={addName}>
        <div>
          name: <input value={newName} onChange={handleNameChange} />
          <br />
          number: <input value={newNumber} onChange={handleNumberChange} />
        </div>
        <div>
          <button type="submit">add</button>
        </div>
      </form>
    </div>
  );
};

export default AddName;
