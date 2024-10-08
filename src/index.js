document.addEventListener('pylonReady', function () {
  console.log('pylonReady');

  document.getElementById('myButton').addEventListener('click', function () {
    // Using the create_window method
    pylon.CustomAPI.create_window().then((windowId) => {
      console.log('New window ID:', windowId); // "New window ID: [generated window ID]" output
    });
  });
});
