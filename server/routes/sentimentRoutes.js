const express = require("express");
const {
  getTeamSentiment,
  getAllTeamsSentiment,
} = require("../controllers/sentimentController");

const router = express.Router();

router.get("/all", getAllTeamsSentiment);

router.get("/:teamName", getTeamSentiment);

module.exports = router;
