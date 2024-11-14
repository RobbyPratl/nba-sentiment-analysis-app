const express = require('express');
const sentimentRoutes = require('./routes/sentimentRoutes');

const app = express();
app.use('/api/sentiment', sentimentRoutes);

module.exports = app;
