import ShowPerson from "./showPerson";
import AddName from "./addPerson";
import { useState } from "react";
import PhoneFilter from "./phoneFilter";

const DisplayPhonebook = ({ persons, setPersons }) => {
  const [newPersons, setNewPersons] = useState([]);
  const [newName, setNewName] = useState("");
  const [newNumber, setNewNumber] = useState(0);
  const [newFilter, setFilter] = useState("");
  const [msg, setMsg] = useState(null);
  const [ok, setOK] = useState(true);

  return (
    <div>
      <PhoneFilter
        msg={msg}
        ok={ok}
        newFilter={newFilter}
        persons={persons}
        newPersons={newPersons}
        setPersons={setPersons}
        setNewPersons={setNewPersons}
        setFilter={setFilter}
      />
      <AddName
        persons={persons}
        newName={newName}
        newNumber={newNumber}
        setPersons={setPersons}
        setNewName={setNewName}
        setNewNumber={setNewNumber}
        setMsg={setMsg}
      />
      <ShowPerson
        persons={persons}
        newPersons={newPersons}
        setNewPersons={setNewPersons}
        setOK={setOK}
        setMsg={setMsg}
        newFilter={newFilter}
      />
    </div>
  );
};

export default DisplayPhonebook;
