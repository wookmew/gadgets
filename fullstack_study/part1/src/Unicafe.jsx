import { useState } from 'react'

const Button = (props) => (
  <button onClick={props.handleClick}>
    {props.text}
  </button>
)

const StatisticLine = (props) => {
  return (
    <tr>
    <td>{props.text}</td>
    <td>value={props.value}</td>
   </tr>
   )
}

const Statistics = (props) => {
  const sum = props.good+props.neutral+props.bad
  if (props.good === 0 && props.neutral === 0 && props.bad === 0 ) {
    return (
      <div>
        <p>Statistics</p>
        <p>No feedback given</p>
      </div>
    )
  } 
  return (
    <div>
      <p>Statistics</p>
      <table>
      <StatisticLine value={props.good} text="good" />
      <StatisticLine value={props.neutral} text="neutral" />
      <StatisticLine value={props.bad} text="bad" />
      <StatisticLine value={(props.good-props.bad)/sum} text="average" />
      <StatisticLine value={props.good/sum} text="positive" />
      </table>
    </div>
    )
}


const Unicafe = () => {
  // save clicks of each button to its own state
  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)


  const setToGood = newValue => {
    console.log('good now', newValue)
    setGood(newValue)
  }

  const setToNeutral = newValue => {
    console.log('neutral now', newValue)
    setNeutral(newValue)
  }

  const setToBad = newValue => {
    console.log('bad now', newValue)
    setBad(newValue)
  }

  return (
    <div>
      <p>give feedback</p>
      <Button handleClick={() => setToGood(good+1)} text="good"/>
      <Button handleClick={() => setToNeutral(neutral+1)} text="neutral"/>
      <Button handleClick={() => setToBad(bad+1)} text="bad"/>
      {/* <button handleClick={() => setToGood(1)}>good</button><button>neutral</button><button>bad</button> */}
      <Statistics good={good} neutral={neutral} bad={bad} />
    </div>
  )
}

export default Unicafe