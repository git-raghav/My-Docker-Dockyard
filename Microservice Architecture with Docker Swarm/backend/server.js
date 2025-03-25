const express = require("express");
const cors = require("cors");
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// In-memory storage (in a real app, this would be a database)
let sharedNote = "";

// Routes
app.get("/api/note", (req, res) => {
	res.json({ note: sharedNote });
});

app.post("/api/note", (req, res) => {
	sharedNote = req.body.note;
	res.json({ success: true, note: sharedNote });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
	console.log(`Backend service running on port ${PORT}`);
});
