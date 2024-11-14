const axios = require("axios");
const { X_BEARER_TOKEN } = require("../config/apiConfig");

const fetchTweets = async (teamName) => {
  const url = `https://api.x.com/2/tweets/search/recent?query=${encodeURIComponent(
    teamName
  )}`;
  const headers = { Authorization: `Bearer ${X_BEARER_TOKEN}` };

  try {
    const response = await axios.get(url, { headers });
    return response.data.data || [];
  } catch (error) {
    console.error("Error fetching tweets:", error);
    return [];
  }
};

module.exports = fetchTweets;
