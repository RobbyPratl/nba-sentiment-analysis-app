const { spawn } = require("child_process");

const analyzeSentiment = (teamName, maxResults = 100) => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python3", [
      "utils/analyze_sentiment.py",
      teamName,
      maxResults.toString(),
    ]);

    pythonProcess.stdout.on("data", (data) => {
      const result = JSON.parse(data.toString());
      resolve(result.average_sentiment);
    });

    pythonProcess.stderr.on("data", (error) => {
      console.error(`Error: ${error}`);
      reject(error.toString());
    });
  });
};

module.exports = analyzeSentiment;
