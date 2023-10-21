import AnecdoteForm from "./components/AddAnecdote";
import Anecdotes from "./components/Anecdotes";
import FilterAnecdote from "./components/FilterAnecdote";

const App = () => {
  return (
    <div>
      <FilterAnecdote />
      <Anecdotes />
      <AnecdoteForm />
    </div>
  );
};

export default App;
