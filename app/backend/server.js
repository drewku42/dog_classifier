// server.js
const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();
const port = 3000;

// Configure multer for image upload
const storage = multer.diskStorage({
  destination: function(req, file, cb) {
    cb(null, path.join(__dirname, 'uploads')); // Set the destination folder for uploaded files
  },
  filename: function(req, file, cb) {
    cb(null, Date.now() + path.extname(file.originalname)); // Use the file's original extension
  }
});

const upload = multer({ storage: storage });

// Serve static files from 'frontend' directory
app.use(express.static(path.join(__dirname, '..', 'frontend')));

// Route for file upload
app.post('/upload', upload.single('dogImage'), (req, res) => {
  // Handle the uploaded file
  console.log(req.file); // You can see the uploaded file details

  // Send back a JSON response
  res.json({ breed: mockBreed, probability: mockProbability });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
