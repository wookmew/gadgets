const Notification = ({ message, ok }) => {
  if (message === null) {
    return null;
  }
  if (ok) {
    return <div className="success">{message}</div>;
  } else {
    return <div className="failure">{message}</div>;
  }
};

export default Notification;
