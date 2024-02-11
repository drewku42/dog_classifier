// Import express
const express = require('express');

// Create a new express application
const app = express();

// Define a port to listen for incoming requests
const PORT = process.env.PORT || 3000;

// Define a route for HTTP GET requests to the root '/'
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Make the server listen on the defined PORT
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
