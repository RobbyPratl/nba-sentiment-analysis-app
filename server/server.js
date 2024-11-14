const express = require("express");
const cors = require("cors"); // Importing the CORS middleware
const sentimentRoutes = require("./routes/sentimentRoutes"); // Importing the routes for sentiment analysis

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware to enable CORS for requests from your React app at http://localhost:3000
app.use(cors({ origin: "http://localhost:3000" }));

// Middleware to parse JSON requests
app.use(express.json());

// Route handling for sentiment analysis
app.use("/api/sentiment", sentimentRoutes);

// Basic route to check if server is running
app.get("/", (req, res) => {
  res.send("Server is running");
});

// Starting the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
