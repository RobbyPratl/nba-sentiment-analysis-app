require("dotenv").config();
module.exports = {
  X_API_KEY: process.env.X_API_KEY,
  X_API_SECRET: process.env.X_API_SECRET,
  X_BEARER_TOKEN: process.env.X_BEARER_TOKEN,
  API_RATE_LIMIT: process.env.API_RATE_LIMIT || 100,
};
