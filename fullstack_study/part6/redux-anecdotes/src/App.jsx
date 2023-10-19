import AnecdoteForm from "./components/AddAnecdote";
import Anecdotes from "./components/Anecdotes";

const App = () => {
  return (
    <div>
      <Anecdotes />
      <AnecdoteForm />
    </div>
  );
};

export default App;
