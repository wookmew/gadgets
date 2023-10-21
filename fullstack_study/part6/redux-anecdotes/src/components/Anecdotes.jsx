import { useSelector, useDispatch } from "react-redux";
import { voteAnecdot } from "../reducers/anecdoteReducer";

const Anecdotes = () => {
  const dispatch = useDispatch();
  const anecdotes = useSelector((state) => {
    if (state.filter === "") {
      return state.anecdotes;
    }
    return state.anecdotes.filter((item) => item.content.match(state.filter));
  });
  console.log("anecdotes", anecdotes);
  const voteAnecdotes = (id) => {
    dispatch(voteAnecdot(id));
  };

  return (
    <div>
      <h2>Anecdotes</h2>
      {anecdotes.map((anecdote) => (
        <div key={anecdote.id}>
          <div>{anecdote.content}</div>
          <div>
            has {anecdote.votes}
            <button onClick={() => voteAnecdotes(anecdote.id)}>vote</button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Anecdotes;
