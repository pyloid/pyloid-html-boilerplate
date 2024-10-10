document.addEventListener('pyloidReady', function () {
  console.log('pyloidReady');

  document.getElementById('myButton').addEventListener('click', function () {
    // Using the create_window method
    pyloid.CustomAPI.create_window().then((windowId) => {
      console.log('New window ID:', windowId); // "New window ID: [generated window ID]" output
    });
  });
});
