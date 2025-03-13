const express = require('express');
const router = express.Router();
const axios = require('axios');

// Endpoint to get employees from employee-service
router.get('/', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5001/api/employees'); // Change port if needed
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching employees', error: error.message });
    }
});

module.exports = router;
