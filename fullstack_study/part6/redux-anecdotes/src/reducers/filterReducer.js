const filterReducer = (state = "", action) => {
  switch (action.type) {
    case "CHANGE":
      return action.payload;
    default:
      return state;
  }
};

export const filterChange = (filter) => {
  return {
    type: "CHANGE",
    payload: filter,
  };
};

export default filterReducer;
