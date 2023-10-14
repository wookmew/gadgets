import personService from "../../services/person";

const DeletePerson = ({ id, name, persons, setNewPersons, setOK, setMsg }) => {
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
          if (err.response.status == 404) {
            setOK(false);
            setMsg(`${name} has already been removed from server`);
            setTimeout(() => {
              setMsg(null);
            }, 1000);
          }
        });
    }
  };

  return <button onClick={del}>delete</button>;
};

export default DeletePerson;
