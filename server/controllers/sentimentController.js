const analyzeSentiment = require("../utils/sentimentAnalyzer");
const teams = [
  "atlanta hawks",
  "boston celtics",
  "brooklyn nets",
  "charlotte hornets",
  "chicago bulls",
  "cleveland cavaliers",
  "dallas mavericks",
  "denver nuggets",
  "detroit pistons",
  "golden state warriors",
  "houston rockets",
  "indiana pacers",
  "los angeles clippers",
  "los angeles lakers",
  "memphis grizzlies",
  "miami heat",
  "milwaukee bucks",
  "minnesota timberwolves",
  "new orleans pelicans",
  "new york knicks",
  "oklahoma city thunder",
  "orlando magic",
  "philadelphia 76ers",
  "phoenix suns",
  "portland trail blazers",
  "sacramento kings",
  "san antonio spurs",
  "toronto raptors",
  "utah jazz",
  "washington wizards",
];
const cache = {};
const CACHE_EXPIRATION_TIME = 7.2 * 60 * 60 * 1000; // 7.2 hours in milliseconds

// Single team sentiment handler
const getTeamSentiment = async (req, res) => {
  const teamName = req.params.teamName.toLowerCase(); // Normalize team name for consistent cache keys
  const now = Date.now();

  // Check if data is in cache and still valid
  const cachedData = cache[teamName];
  if (cachedData && now - cachedData.timestamp < CACHE_EXPIRATION_TIME) {
    console.log(`Serving cached data for ${teamName}`);
    return res.json({
      teamName,
      averageSentiment: cachedData.averageSentiment,
    });
  }

  // Fetch new data and update cache if cache is expired or not available
  try {
    const averageSentiment = await analyzeSentiment(teamName);
    cache[teamName] = {
      averageSentiment,
      timestamp: now,
    };

    console.log(`Updated cache for ${teamName}`);
    res.json({ teamName, averageSentiment });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Error processing sentiment" });
  }
};

// All teams sentiment handler

const getAllTeamsSentiment = async (req, res) => {
  const now = Date.now();
  const results = [];

  for (const teamName of teams) {
    const cachedData = cache[teamName];
    if (cachedData && now - cachedData.timestamp < CACHE_EXPIRATION_TIME) {
      console.log(`Serving cached data for ${teamName}`);
      results.push({ teamName, averageSentiment: cachedData.averageSentiment });
    } else {
      try {
        const averageSentiment = await analyzeSentiment(teamName);
        cache[teamName] = {
          averageSentiment,
          timestamp: now,
        };
        results.push({ teamName, averageSentiment });
        console.log(`Updated cache for ${teamName}`);
      } catch (error) {
        console.error(`Error fetching sentiment for ${teamName}:`, error);
      }
    }
  }

  // Sort teams by averageSentiment in descending order (optional)
  results.sort((a, b) => b.averageSentiment - a.averageSentiment);

  res.json(results);
};

module.exports = { getTeamSentiment, getAllTeamsSentiment };
