const PhoneFilter = ({
  newFilter,
  persons,
  setPersons,
  setNewPersons,
  setFilter,
}) => {
  const handleFilterChange = (event) => {
    setFilter(event.target.value);
    if (event.target.value.length > 0) {
      setNewPersons(
        persons.filter((person) =>
          person.name.toLowerCase().startsWith(event.target.value.toLowerCase())
        )
      );
    } else {
      setNewPersons([]);
      setPersons(persons);
    }
  };

  return (
    <div>
      <h2>Phonebook</h2>
      filter shown with:{" "}
      <input value={newFilter} onChange={handleFilterChange} />
    </div>
  );
};

export default PhoneFilter;
