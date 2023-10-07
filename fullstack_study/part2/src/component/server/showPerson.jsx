import DeletePerson from "./deletePerson";

const ShowPerson = ({ persons, newPersons, newFilter, setNewPersons }) => {
  return (
    <div>
      <h2>Numbers</h2>
      <ul>
        {newPersons.length > 0 || newFilter.length > 0
          ? newPersons.map((person) => (
              <li key={person.id}>
                {person.name} {person.number}{" "}
                <DeletePerson
                  id={person.id}
                  name={person.name}
                  persons={persons}
                  setNewPersons={setNewPersons}
                />
              </li>
            ))
          : persons.map((person) => (
              <li key={person.id}>
                {person.name} {person.number}{" "}
                <DeletePerson
                  id={person.id}
                  name={person.name}
                  persons={persons}
                  setNewPersons={setNewPersons}
                />
              </li>
            ))}
      </ul>
    </div>
  );
};

export default ShowPerson;
