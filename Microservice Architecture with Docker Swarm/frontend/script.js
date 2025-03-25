const BACKEND_URL = "http://localhost:3000";

// Function to save the note
async function saveNote() {
	const noteInput = document.getElementById("noteInput");
	const note = noteInput.value;

	try {
		const response = await fetch(`${BACKEND_URL}/api/note`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ note }),
		});

		if (response.ok) {
			updateNoteDisplay();
			alert("Note saved successfully!");
		} else {
			throw new Error("Failed to save note");
		}
	} catch (error) {
		console.error("Error saving note:", error);
		alert("Failed to save note. Please try again.");
	}
}

// Function to update the note display
async function updateNoteDisplay() {
	const noteDisplay = document.getElementById("noteDisplay");

	try {
		const response = await fetch(`${BACKEND_URL}/api/note`);
		if (response.ok) {
			const data = await response.json();
			noteDisplay.textContent = data.note || "No note available";
		} else {
			throw new Error("Failed to fetch note");
		}
	} catch (error) {
		console.error("Error fetching note:", error);
		noteDisplay.textContent = "Error loading note. Please try again.";
	}
}

// Update display when page loads
document.addEventListener("DOMContentLoaded", updateNoteDisplay);

// Poll for updates every 2 seconds
setInterval(updateNoteDisplay, 2000);
