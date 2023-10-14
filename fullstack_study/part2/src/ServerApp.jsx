import DisplayPhonebook from "./component/server/phonebook";
import { useState, useEffect } from "react";
import personService from "./services/person";
import "./index.css";

const ServerApp = () => {
  const [persons, setPersons] = useState([]);
  useEffect(() => {
    personService.getAll().then((response) => {
      console.log("response", response);
      setPersons(response);
    });
  }, []);
  return (
    <div>
      <DisplayPhonebook persons={persons} setPersons={setPersons} />
    </div>
  );
};

export default ServerApp;
