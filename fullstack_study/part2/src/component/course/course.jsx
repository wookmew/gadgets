const Header = ({title}) => {
  return (
    <h1>
      {title}
    </h1>
  )
}

const Content = ({content}) => {
  return (
    <ul>
        {content.map(node => <Part node={node}/>)}
    </ul>
  )
}

const Part = ({node}) => {
  return (
    <li key={node.id}>{node.name} {node.exercises}</li>
  )
}

const Total = ({contentArr}) => {
  const sumExercises = contentArr.reduce(function (acc, obj) { return acc + obj.exercises;}, 0);
  return (
  <p>total of {sumExercises} exercises</p>
  )
}

const Course = ({course}) => {
  return (
    <div>
    <Header title={course.name}/>
    <Content content={course.parts}/>
    <Total contentArr={course.parts} />
    </div>
  )
}

export default Course