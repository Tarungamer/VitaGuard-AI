const express = require("express");
const app = express();

app.use(express.json());

let appointments = [];

app.post("/book-appointment", (req, res) => {
    const { patient, doctor, date, time } = req.body;
    appointments.push({ patient, doctor, date, time });
    res.json({ message: "Appointment booked successfully!" });
});

app.get("/appointments", (req, res) => {
    res.json(appointments);
});

app.listen(5003, () => console.log("✅ Appointment Booking API running on http://localhost:5003"));
