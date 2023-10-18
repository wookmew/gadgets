const initialState = {
  good: 0,
  ok: 0,
  bad: 0,
};

const counterReducer = (state = initialState, action) => {
  console.log(action);
  const objCopy = { ...state };
  switch (action.type) {
    case "GOOD":
      objCopy.good += 1;
      return objCopy;
    case "OK":
      objCopy.ok += 1;
      return objCopy;
    case "BAD":
      objCopy.bad += 1;
      return objCopy;
    case "ZERO":
      return initialState;
    default:
      return objCopy;
  }
};

export default counterReducer;
