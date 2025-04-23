const express = require("express");
const app = express();
const port = 3000;

// Serve static files
app.use(express.static("public"));

app.get("/", (req, res) => {
	res.send(`
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Kubernetes Lab</title>
			<style>
				body {
					font-family: 'Arial', sans-serif;
					margin: 0;
					padding: 0;
					background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
					color: white;
					min-height: 100vh;
					display: flex;
					justify-content: center;
					align-items: center;
				}
				.container {
					text-align: center;
					padding: 2rem;
					background: rgba(255, 255, 255, 0.1);
					border-radius: 15px;
					backdrop-filter: blur(10px);
					box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
				}
				h1 {
					font-size: 2.5rem;
					margin-bottom: 1rem;
					color: #ffffff;
				}
				.name {
					font-size: 1.8rem;
					color: #ffd700;
					margin: 1rem 0;
				}
				.message {
					font-size: 1.2rem;
					margin: 1rem 0;
				}
				.footer {
					margin-top: 2rem;
					font-size: 0.9rem;
					color: rgba(255, 255, 255, 0.8);
				}
			</style>
		</head>
		<body>
			<div class="container">
				<h1>Welcome to Kubernetes Lab</h1>
				<div class="name">Raghav Agarwal</div>
				<div class="message">This application is running on Kubernetes!</div>
				<div class="footer">Deployed using Kubernetes</div>
			</div>
		</body>
		</html>
	`);
});

app.get("/health", (req, res) => {
	res.status(200).send("OK");
});

app.listen(port, () => {
	console.log(`App listening at http://localhost:${port}`);
});
