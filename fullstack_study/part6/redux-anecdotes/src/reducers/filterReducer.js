const filterReducer = (state = "", action) => {
  console.log("filter action", action);
  switch (action.type) {
    case "CHANGE":
      return action.payload;
    default:
      return state;
  }
};

export const filterChange = (filter) => {
  console.log("wwwww", filter);
  return {
    type: "CHANGE",
    payload: filter,
  };
};

export default filterReducer;
