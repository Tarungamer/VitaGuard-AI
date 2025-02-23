const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

const healthTips = [
  "Drink plenty of water daily.",
  "Exercise at least 30 minutes a day.",
  "Maintain a balanced diet rich in vitamins.",
  "Ensure you get enough sleep every night."
];

app.get('/api/health-tips', (req, res) => {
  res.json(healthTips);
});

app.post('/api/ai-health-assistant', (req, res) => {
  const { query } = req.body;
  const reply = `This is an AI-generated response to your query: ${query}`;
  res.json({ reply });
});

app.listen(5000, () => {
  console.log('Server running on port 5000');
});