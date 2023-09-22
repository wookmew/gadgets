import { useState } from 'react'

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

const Button = (props) => (
  <button onClick={props.handleClick}>
    {props.text}
  </button>

)

const Anecdotes = () => {

  const anecdotes = [
    'If it hurts, do it more often.',
    'Adding manpower to a late software project makes it later!',
    'The first 90 percent of the code accounts for the first 10 percent of the development time...The remaining 10 percent of the code accounts for the other 90 percent of the development time.',
    'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.',
    'Premature optimization is the root of all evil.',
    'Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.',
    'Programming without an extremely heavy use of console.log is same as if a doctor would refuse to use x-rays or blood tests when diagnosing patients.',
    'The only way to go fast, is to go well.'
  ]
  let len = anecdotes.length
  const voted = {}
  anecdotes.map(function(_, i) {voted[i]=0})
  const [selected, setSelected] = useState(0)
  const [votes, setPoint] = useState(Array(len).fill(0))

  


  const setToSelected = newValue => {
    newValue = getRandomInt(len)
    console.log('selected now', newValue)
    setSelected(newValue)
  }

  const setToVote = () => {
    const voteCopy = [...votes]
    voteCopy[selected] += 1
    console.log('voted', voteCopy)
    setPoint(voteCopy)
  }

  const highestVotes = Math.max(...votes);

  return (
    <div>
      <h1>Anecdote of the day</h1>
      <p>{anecdotes[selected]}</p>
      <p>has {votes[selected]} votes</p>
      <Button handleClick={() => setToVote(selected)} text="vote" />
      <Button handleClick={() => setToSelected(selected)} text="next anecdote" />
      <h1>Anecdote with most votes</h1>
      <p>{anecdotes[votes.indexOf(highestVotes)]}</p>
      <p>has {highestVotes} votes</p>
    </div>
  )
}

export default Anecdotes