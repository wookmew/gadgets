import personService from "../../services/person";

const DeletePerson = ({ id, name, persons, setNewPersons }) => {
  const del = () => {
    if (window.confirm(`delete ${name}`)) {
      personService
        .deletePersonByID(id)
        .then((resp) => {
          if (resp.status === 200) {
            setNewPersons(persons.filter((person) => person.id != id));
          }
          console.log("resp", resp, resp.status, resp.response);
        })
        .catch((err) => {
          console.log("err", err);
        });
    }
  };

  return <button onClick={del}>delete</button>;
};

export default DeletePerson;
