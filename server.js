// server.js (Node.js/Express)
const express = require('express');
const User = require('./models/User');
const app = express();

app.use(express.json()); // To parse JSON bodies

// Route 1: Initial Mobile Number Check (Login/Signup Entry point)
app.post('/api/auth/check-mobile', async (req, res) => {
    const { mobileNumber } = req.body;

    try {
        let user = await User.findOne({ mobileNumber });

        if (user && user.isRegistered) {
            // Scenario 2 & 3: User already exists and is registered.
            return res.json({
                success: true,
                message: "Login successful",
                action: "login",
                user
            });
        }

        if (!user) {
            // Create a temporary user record before they fill details
            user = await User.create({ mobileNumber });
        }

        // Scenario 1: New customer, needs to fill details
        return res.json({
            success: true,
            message: "Please complete profile",
            action: "signup",
            userId: user._id
        });

    } catch (err) {
        res.status(500).json({ error: "Server error" });
    }
});

// Route 2: Complete Profile (Finish Signup)
app.post('/api/auth/complete-profile', async (req, res) => {
    const { userId, name, address } = req.body;

    try {
        // Update user with their details and mark as registered
        const user = await User.findByIdAndUpdate(
            userId,
            { name, address, isRegistered: true },
            { new: true }
        );

        res.json({ success: true, message: "Signup complete", user });
    } catch (err) {
        res.status(500).json({ error: "Server error" });
    }
});
