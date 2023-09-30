const ShowPerson = ({persons, newPersons, newFilter}) => {
  console.log('persons', persons, typeof(persons))
  return (
    <div>
    <h2>Numbers</h2>
    <ul>
        {(newPersons.length > 0 || newFilter.length > 0) ? (
          newPersons.map(person => <li key={person.id}>{person.name} {person.number}</li>)
         ): (
          persons.map(person => <li key={person.id}>{person.name} {person.number}</li>)
        )}
    </ul>
    </div>
  )
}

export default ShowPerson